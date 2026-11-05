import sys

import cv2

from config import config
from image_read_write import ImageReadWrite
from crop_image import CropImage
from mask_creator import MaskCreator
from calculate_overlap import CalculateOverlap


class MainAlphaBlender:
    """Orchestrates the full image-blending pipeline (no gamma compensation).

    All tuneable parameters live in ``config.json`` and are accessible via the
    global ``config`` variable across classes.

    Attributes (from UML):
        __configReader (ConfigReader) – configuration provider
    """

    def __init__(self):
        # Read the side from the command-line argument (overrides JSON default)
        side = sys.argv[1].lower() if len(sys.argv) > 1 else None
        if side is not None and side not in ("left", "right"):
            print("Usage: python main.py [left|right]")
            sys.exit(1)

        # --- UML private attribute (uses global ConfigReader instance) ---
        self.__configReader = config
        if side is not None:
            self.__configReader.setSide(side)

    # --- Getter & Setter methods ---

    def getConfigReader(self):
        """Returns the configuration reader instance (ConfigReader)."""
        return self.__configReader

    def setConfigReader(self, config_reader):
        """Sets the configuration reader instance (void)."""
        self.__configReader = config_reader

    # --- UML public methods ---

    def display(self):
        """Runs the full blending pipeline and displays the result (void)."""
        cfg = self.getConfigReader()
        side = cfg.getSide()

        # 1. Read the image (uses global config variable)
        reader = ImageReadWrite()
        image = reader.getImage()
        img_height, img_width = image.shape[:2]

        # 2. Safety-check overlap and update via getter and setter
        if img_width <= cfg.getOverlap():
            original = cfg.getOverlap()
            cfg.setOverlap(img_width // 3)
            print(
                f"Note: Image width ({img_width}px) is smaller than "
                f"{original}px. Adjusting overlap to {cfg.getOverlap()}px."
            )

        # 3. Crop the image (uses global config variable & getter methods)
        cropper = CropImage(image)
        cropper.crop()
        cropped = cropper.getImgLeft() if side == "left" else cropper.getImgRight()

        # 4. Create the linear gradient mask (uses global config variable)
        mask_creator = MaskCreator()
        mask = mask_creator.createMask(side, img_height, cropped.shape[1])

        # 5. Apply alpha blending (uses global config variable)
        calc = CalculateOverlap(cropped, mask)
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
