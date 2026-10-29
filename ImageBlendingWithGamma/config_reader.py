import os
import sys


class ConfigReader:
    """Reads and provides configuration parameters for image blending.

    Attributes (from UML):
        p_width    (int)   – projector / projection width in pixels
        p_height   (int)   – projector / projection height in pixels
        p_distance (float) – physical distance between projectors
        p_overlap  (int)   – target overlap width in pixels
        p_length   (float) – projection throw length
        gamma      (float) – gamma compensation value
    """

    def __init__(self, image_name="test_picture.jpg", side="left",
                 p_width=1920, p_height=1080, p_distance=0.0,
                 p_overlap=1280, p_length=0.0, gamma=1.5):
        # --- UML private attributes ---
        self.p_width = p_width          # int
        self.p_height = p_height        # int
        self.p_distance = p_distance    # float
        self.p_overlap = p_overlap      # int
        self.p_length = p_length        # float
        self.gamma = gamma              # float

        # Internal state used by getter methods
        self._image_name = image_name
        self._side = side

    # --- UML public methods ---

    def getProjectedImageWidth(self):
        """Returns the projected image width (int)."""
        return self.p_width

    def getDistanceBetweenProjector(self):
        """Prints the distance between projectors (void)."""
        print(f"Distance between projectors: {self.p_distance}")

    def getImageWidth(self):
        """Returns the configured image width (int)."""
        return self.p_width

    def getImageHeight(self):
        """Returns the configured image height (int)."""
        return self.p_height

    def getImageName(self):
        """Returns the image filename (String)."""
        return self._image_name

    def getSide(self):
        """Returns the blending side – 'left' or 'right' (String)."""
        return self._side

    def getGamma(self):
        """Returns the gamma compensation value (float)."""
        return self.gamma

    def getProjectionLength(self):
        """Returns the projection throw length (float)."""
        return self.p_length

    def getProjectionWidth(self):
        """Returns the projection width in pixels (int)."""
        return self.p_width

    def getProjectionHeight(self):
        """Returns the projection height in pixels (int)."""
        return self.p_height
