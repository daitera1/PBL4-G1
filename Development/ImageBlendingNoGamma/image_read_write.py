import os
import sys

import cv2


class ImageReadWrite:
    """Reads an image from disk and stores it.

    Uses the global configuration variable by default for the image filename,
    while supporting custom configuration or direct filename instantiation.

    Attributes (from UML):
        img_filename (String) – path to the image file
        image        (Mat)    – the loaded image matrix
    """

    def __init__(self, config_reader=None, img_filename=None):
        if config_reader is None and img_filename is None:
            from config import config as global_config
            config_reader = global_config

        # --- UML private attributes ---
        self._image = None          # Mat
        self._img_filename = None   # String

        if img_filename is not None:
            self._img_filename = img_filename
        elif isinstance(config_reader, str):
            self._img_filename = config_reader
        elif config_reader is not None:
            self._img_filename = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                config_reader.getImageName(),
            )

        # Load image if filename is resolved
        if self._img_filename:
            self.readImage(self._img_filename)

    # --- Property accessors (for backward compatibility) ---

    @property
    def image(self):
        return self.getImage()

    @image.setter
    def image(self, val):
        self.setImage(val)

    @property
    def img_filename(self):
        return self.getImgFilename()

    @img_filename.setter
    def img_filename(self, val):
        self.setImgFilename(val)

    # --- Getter methods ---

    def getImage(self):
        """Returns the loaded image matrix (Mat)."""
        return self._image

    def getImgFilename(self):
        """Returns the image filename / path (String)."""
        return self._img_filename

    # --- Setter methods ---

    def setImage(self, image):
        """Sets the stored image matrix (void)."""
        self._image = image

    def setImgFilename(self, img_filename):
        """Sets the image filename / path (void)."""
        self._img_filename = img_filename

    # --- I/O methods ---

    def readImage(self, img_filename=None):
        """Reads an image from disk into memory (Mat)."""
        if img_filename is not None:
            self._img_filename = img_filename
        if self._img_filename is None:
            raise ValueError("No image filename specified to read.")

        self._image = cv2.imread(self._img_filename)
        if self._image is None:
            print(f"Error: Could not load image '{self._img_filename}'!")
            sys.exit(1)
        return self._image

    def writeImage(self, filename, image=None):
        """Writes an image to disk (bool)."""
        target = image if image is not None else self._image
        if target is None:
            raise ValueError("No image available to write.")
        return cv2.imwrite(filename, target)
