import sys

import cv2
import numpy as np

import config


class ImageBlender:
    def __init__(self, image_path=config.IMAGE_PATH,
                 projector_width=config.PROJECTOR_WIDTH,
                 projector_height=config.PROJECTOR_HEIGHT,
                 target_overlap_width=config.TARGET_OVERLAP_WIDTH):
        self.image_path = image_path
        self.projector_width = projector_width
        self.projector_height = projector_height
        self.target_overlap_width = target_overlap_width

    def load_image(self):
        input_image = cv2.imread(self.image_path)
        if input_image is None:
            print(f"Error: Could not load image '{self.image_path}'!")
            sys.exit(1)
        return input_image

    def get_overlap_width(self, img_width):
        overlap_width = self.target_overlap_width

        # Safety check if the image is too small for the target overlap
        if img_width <= overlap_width:
            overlap_width = img_width // 3
            print(f"Note: Image width ({img_width}px) is smaller than {self.target_overlap_width}px. "
                  f"Adjusting overlap to {overlap_width}px.")
        return overlap_width

    def show(self, window_name, frame):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(window_name, frame)

        print(f"{window_name} feed running. Press any key to exit.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # --- LEFT PROJECTOR ---
    def blend_left(self, input_image):
        img_height, img_width = input_image.shape[:2]
        overlap_width = self.get_overlap_width(img_width)

        half_width = img_width // 2
        overlap_end = half_width + (overlap_width // 2)
        left_feed = input_image[:, :overlap_end].copy()

        # Create linear alpha gradient mask for edge blending
        left_mask = np.ones((img_height, left_feed.shape[1]), dtype=np.float32)
        for i in range(overlap_width):
            alpha = 1.0 - (i / overlap_width)
            col_idx = left_feed.shape[1] - overlap_width + i
            if 0 <= col_idx < left_feed.shape[1]:
                left_mask[:, col_idx] = alpha

        left_mask_3ch = cv2.merge([left_mask, left_mask, left_mask])
        blended_left = (left_feed.astype(np.float32) * left_mask_3ch).astype(np.uint8)

        # Right-align for the Left Projector
        target_w, target_h = self.projector_width, self.projector_height
        h, w = blended_left.shape[:2]
        canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
        new_w = int(w * (target_h / h))
        resized = cv2.resize(blended_left, (new_w, target_h))

        if new_w <= target_w:
            canvas[:, target_w - new_w:] = resized
        else:
            canvas = cv2.resize(blended_left, (target_w, target_h))
        return canvas

    def left(self):
        self.show(config.LEFT_WINDOW_NAME, self.blend_left(self.load_image()))

    # --- RIGHT PROJECTOR ---
    def blend_right(self, input_image):
        img_height, img_width = input_image.shape[:2]
        overlap_width = self.get_overlap_width(img_width)

        half_width = img_width // 2
        overlap_start = half_width - (overlap_width // 2)
        right_feed = input_image[:, overlap_start:].copy()

        # Create linear alpha gradient mask for edge blending
        right_mask = np.ones((img_height, right_feed.shape[1]), dtype=np.float32)
        for i in range(overlap_width):
            alpha = i / overlap_width
            if i < right_feed.shape[1]:
                right_mask[:, i] = alpha

        right_mask_3ch = cv2.merge([right_mask, right_mask, right_mask])
        blended_right = (right_feed.astype(np.float32) * right_mask_3ch).astype(np.uint8)

        # Left-align for the Right Projector
        target_w, target_h = self.projector_width, self.projector_height
        h, w = blended_right.shape[:2]
        canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
        new_w = int(w * (target_h / h))
        resized = cv2.resize(blended_right, (new_w, target_h))

        if new_w <= target_w:
            canvas[:, :new_w] = resized
        else:
            canvas = cv2.resize(blended_right, (target_w, target_h))
        return canvas

    def right(self):
        self.show(config.RIGHT_WINDOW_NAME, self.blend_right(self.load_image()))


if __name__ == "__main__":
    # Usage: python main.py left   or   python main.py right
    side = sys.argv[1].lower() if len(sys.argv) > 1 else ""
    blender = ImageBlender()
    if side == "left":
        blender.left()
    elif side == "right":
        blender.right()
    else:
        print("Usage: python main.py [left|right]")
        sys.exit(1)
