import sys

import cv2


class ImageReadWrite:
    """Reads an image from disk and stores it.

    Attributes (from UML):
        img_filename (String) – path to the image file
        image        (Mat)    – the loaded image matrix
    """

    def __init__(self, img_filename):
        # --- UML private attributes ---
        self.img_filename = img_filename  # String
        self.image = None                 # Mat

        # Load image on construction
        self.image = cv2.imread(self.img_filename)
        if self.image is None:
            print(f"Error: Could not load image '{self.img_filename}'!")
            sys.exit(1)

    # --- UML public methods ---

    def getImage(self):
        """Returns the loaded image matrix (Mat)."""
        return self.image
