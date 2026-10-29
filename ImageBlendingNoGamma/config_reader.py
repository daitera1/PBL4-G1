import json
import os
import sys


class ConfigReader:
    """Reads configuration parameters from a JSON file and provides
    getter methods for the rest of the pipeline.

    The JSON file (``config.json``) is the single flexible source for
    all tuneable settings.  The Python code stays hardcoded — only the
    JSON values change between runs.

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
        self.p_width = int(data.get("p_width", 1920))
        self.p_height = int(data.get("p_height", 1080))
        self.p_distance = float(data.get("p_distance", 0.0))
        self.p_overlap = int(data.get("p_overlap", 1280))
        self.p_length = float(data.get("p_length", 0.0))
        self.gamma = float(data.get("gamma", 1.0))

        # Additional settings from JSON
        self._image_name = str(data.get("image_name", "test_picture.jpg"))
        # Command-line side override takes priority over JSON value
        self._side = side_override if side_override else str(data.get("side", "left"))

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
        """Returns the gamma value (float). 1.0 = linear (no compensation)."""
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
