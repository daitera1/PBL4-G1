import json
import os
import sys


class ConfigReader:
    """Reads configuration parameters from a JSON file and provides
    getter and setter methods for the rest of the pipeline.

    The JSON file (``config.json``) is the single flexible source for
    all tuneable settings.

    Attributes (from UML):
        p_width    (int)   – projector / projection width in pixels
        p_height   (int)   – projector / projection height in pixels
        p_distance (float) – physical distance between projectors
        p_overlap  (int)   – target overlap width in pixels
        p_length   (float) – projection throw length
        gamma      (float) – gamma value (1.0 = linear, no compensation)
    """

    def __init__(self, config_path=None, side_override=None):
        # Resolve config.json relative to this file's directory
        if config_path is None:
            config_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "config.json"
            )

        # Read JSON file
        try:
            with open(config_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: Configuration file '{config_path}' not found!")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in '{config_path}': {e}")
            sys.exit(1)

        # --- UML private attributes (loaded from JSON) ---
        self._p_width = int(data.get("p_width", 1920))
        self._p_height = int(data.get("p_height", 1080))
        self._p_distance = float(data.get("p_distance", 0.0))
        self._p_overlap = int(data.get("p_overlap", 1280))
        self._p_length = float(data.get("p_length", 0.0))
        self._gamma = float(data.get("gamma", 1.0))

        # Additional settings from JSON
        self._image_name = str(data.get("image_name", "test_picture.jpg"))
        # Command-line side override takes priority over JSON value
        self._side = side_override if side_override else str(data.get("side", "left"))

    # --- Property accessors (for backward compatibility) ---

    @property
    def p_width(self):
        return self._p_width

    @p_width.setter
    def p_width(self, val):
        self._p_width = int(val)

    @property
    def p_height(self):
        return self._p_height

    @p_height.setter
    def p_height(self, val):
        self._p_height = int(val)

    @property
    def p_distance(self):
        return self._p_distance

    @p_distance.setter
    def p_distance(self, val):
        self._p_distance = float(val)

    @property
    def p_overlap(self):
        return self._p_overlap

    @p_overlap.setter
    def p_overlap(self, val):
        self._p_overlap = int(val)

    @property
    def p_length(self):
        return self._p_length

    @p_length.setter
    def p_length(self, val):
        self._p_length = float(val)

    @property
    def gamma(self):
        return self._gamma

    @gamma.setter
    def gamma(self, val):
        self._gamma = float(val)

    # --- Getter methods ---

    def getProjectedImageWidth(self):
        """Returns the projected image width (int)."""
        return self._p_width

    def getDistanceBetweenProjector(self):
        """Prints and returns the distance between projectors."""
        print(f"Distance between projectors: {self._p_distance}")
        return self._p_distance

    def getImageWidth(self):
        """Returns the configured image width (int)."""
        return self._p_width

    def getImageHeight(self):
        """Returns the configured image height (int)."""
        return self._p_height

    def getImageName(self):
        """Returns the image filename (String)."""
        return self._image_name

    def getSide(self):
        """Returns the blending side – 'left' or 'right' (String)."""
        return self._side

    def getGamma(self):
        """Returns the gamma value (float). 1.0 = linear (no compensation)."""
        return self._gamma

    def getProjectionLength(self):
        """Returns the projection throw length (float)."""
        return self._p_length

    def getProjectionWidth(self):
        """Returns the projection width in pixels (int)."""
        return self._p_width

    def getProjectionHeight(self):
        """Returns the projection height in pixels (int)."""
        return self._p_height

    def getOverlap(self):
        """Returns the target overlap width in pixels (int)."""
        return self._p_overlap

    def getPOverlap(self):
        """Alias for getOverlap (int)."""
        return self._p_overlap

    # --- Setter methods ---

    def setOverlap(self, overlap):
        """Sets the target overlap width in pixels (void)."""
        self._p_overlap = int(overlap)

    def setPOverlap(self, overlap):
        """Alias for setOverlap (void)."""
        self.setOverlap(overlap)

    def setSide(self, side):
        """Sets the blending side – 'left' or 'right' (void)."""
        self._side = str(side)

    def setImageName(self, image_name):
        """Sets the image filename (void)."""
        self._image_name = str(image_name)

    def setGamma(self, gamma):
        """Sets the gamma value (void)."""
        self._gamma = float(gamma)

    def setProjectorWidth(self, width):
        """Sets the projector / projection width in pixels (void)."""
        self._p_width = int(width)

    def setProjectorHeight(self, height):
        """Sets the projector / projection height in pixels (void)."""
        self._p_height = int(height)

    def setProjectionWidth(self, width):
        """Sets the projection width in pixels (void)."""
        self._p_width = int(width)

    def setProjectionHeight(self, height):
        """Sets the projection height in pixels (void)."""
        self._p_height = int(height)

    def setProjectionLength(self, length):
        """Sets the projection throw length (void)."""
        self._p_length = float(length)

    def setDistanceBetweenProjector(self, distance):
        """Sets the physical distance between projectors (void)."""
        self._p_distance = float(distance)
