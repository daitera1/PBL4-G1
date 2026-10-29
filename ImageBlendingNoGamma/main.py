import os
import sys

import cv2

from config_reader import ConfigReader
from image_read_write import ImageReadWrite
from crop_image import CropImage
from mask_creator import MaskCreator
from calculate_overlap import CalculateOverlap


class MainAlphaBlender:
    """Orchestrates the full image-blending pipeline (no gamma compensation).

    Attributes (from UML):
        __configReader (ConfigReader) – configuration provider
    """

    def __init__(self):
        # Read the side from the command-line argument
        side = sys.argv[1].lower() if len(sys.argv) > 1 else ""
        if side not in ("left", "right"):
            print("Usage: python main.py [left|right]")
            sys.exit(1)

        # --- UML private attribute ---
        self.__configReader = ConfigReader(
            image_name="test_picture.jpg",
            side=side,
            p_width=1920,
            p_height=1080,
            p_distance=0.0,
            p_overlap=1280,
            p_length=0.0,
            gamma=1.0,  # No gamma compensation (linear blending)
        )

    # --- UML public methods ---

    def display(self):
        """Runs the full blending pipeline and displays the result (void)."""
        config = self.__configReader
        side = config.getSide()

        # 1. Read the image
        image_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), config.getImageName()
        )
        reader = ImageReadWrite(image_path)
        image = reader.getImage()
        img_height, img_width = image.shape[:2]

        # 2. Calculate effective overlap (with safety check)
        overlap = config.p_overlap
        if img_width <= overlap:
            overlap = img_width // 3
            print(
                f"Note: Image width ({img_width}px) is smaller than "
                f"{config.p_overlap}px. Adjusting overlap to {overlap}px."
            )

        # 3. Crop the image into left / right halves
        cropper = CropImage(image, overlap)
        cropper.crop()
        cropped = cropper.img_left if side == "left" else cropper.img_right

        # 4. Create the linear gradient mask
        mask_creator = MaskCreator(config.getGamma(), overlap)
        mask = mask_creator.createMask(side, img_height, cropped.shape[1])

        # 5. Apply alpha blending and position on canvas
        calc = CalculateOverlap(
            side, overlap, cropped, mask,
            config.getProjectionWidth(), config.getProjectionHeight(),
        )
        result = calc.alphaGamma()

        # 6. Display full-screen
        window_name = f"{'Left' if side == 'left' else 'Right'} Projector"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(
            window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
        )
        cv2.imshow(window_name, result)

        print(f"{window_name} feed running. Press any key to exit.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    blender = MainAlphaBlender()
    blender.display()
