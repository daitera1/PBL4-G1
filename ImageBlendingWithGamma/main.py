import sys

import cv2

from config_reader import ConfigReader
from image_read_write import ImageReadWrite
from crop_image import CropImage
from mask_creator import MaskCreator
from calculate_overlap import CalculateOverlap


class MainAlphaBlender:
    """Orchestrates the full image-blending pipeline with gamma compensation.

    All tuneable parameters live in ``config.json`` and are read by
    ConfigReader.  The code here is hardcoded logic that operates on
    those flexible values.

    Attributes (from UML):
        __configReader (ConfigReader) – configuration provider
    """

    def __init__(self):
        # Read the side from the command-line argument (overrides JSON default)
        side = sys.argv[1].lower() if len(sys.argv) > 1 else None
        if side is not None and side not in ("left", "right"):
            print("Usage: python main.py [left|right]")
            sys.exit(1)

        # --- UML private attribute ---
        # ConfigReader reads everything from config.json
        self.__configReader = ConfigReader(side_override=side)

    # --- UML public methods ---

    def display(self):
        """Runs the full blending pipeline and displays the result (void)."""
        config = self.__configReader
        side = config.getSide()

        # 1. Read the image (depends on ConfigReader)
        reader = ImageReadWrite(config)
        image = reader.getImage()
        img_height, img_width = image.shape[:2]

        # 2. Safety-check overlap and update ConfigReader
        if img_width <= config.p_overlap:
            original = config.p_overlap
            config.p_overlap = img_width // 3
            print(
                f"Note: Image width ({img_width}px) is smaller than "
                f"{original}px. Adjusting overlap to {config.p_overlap}px."
            )

        # 3. Crop the image (depends on ConfigReader)
        cropper = CropImage(config, image)
        cropper.crop()
        cropped = cropper.img_left if side == "left" else cropper.img_right

        # 4. Create the gamma-compensated gradient mask (depends on ConfigReader)
        mask_creator = MaskCreator(config)
        mask = mask_creator.createMask(side, img_height, cropped.shape[1])

        # 5. Apply alpha-gamma blending (depends on ConfigReader)
        calc = CalculateOverlap(config, cropped, mask)
        result = calc.alphaGamma()

        # 6. Display full-screen
        window_name = f"{'Left' if side == 'left' else 'Right'} Projector"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(
            window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
        )
        cv2.imshow(window_name, result)

        print(
            f"{window_name} feed running (gamma={config.getGamma()}). "
            f"Press any key to exit."
        )
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    blender = MainAlphaBlender()
    blender.display()
