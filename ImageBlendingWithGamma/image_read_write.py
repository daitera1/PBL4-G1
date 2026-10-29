import os
import sys

import cv2


class ImageReadWrite:
    """Reads an image from disk and stores it.

    Depends on ConfigReader for the image filename.

    Attributes (from UML):
        img_filename (String) – path to the image file
        image        (Mat)    – the loaded image matrix
    """

    def __init__(self, config_reader):
        # --- UML private attributes ---
        self.img_filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            config_reader.getImageName(),
        )  # String
        self.image = None  # Mat

        # Load image on construction
        self.image = cv2.imread(self.img_filename)
        if self.image is None:
            print(f"Error: Could not load image '{self.img_filename}'!")
            sys.exit(1)

    # --- UML public methods ---

    def getImage(self):
        """Returns the loaded image matrix (Mat)."""
        return self.image
