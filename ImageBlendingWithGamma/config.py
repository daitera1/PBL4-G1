import os
from config_reader import ConfigReader

# --- GLOBAL CONFIGURATION VARIABLE ---
# Shared ConfigReader instance accessible throughout all classes and modules
config = ConfigReader()

# Backward-compatible alias
config_reader = config


def getConfig():
    """Returns the global ConfigReader instance."""
    global config
    return config


def setConfig(new_config):
    """Sets the global ConfigReader instance."""
    global config
    config = new_config


# Window names for display
LEFT_WINDOW_NAME = "Left Projector"
RIGHT_WINDOW_NAME = "Right Projector"


# Module-level attribute fallback for legacy constants (e.g. PROJECTOR_WIDTH)
def __getattr__(name):
    if name == "PROJECTOR_WIDTH":
        return config.getProjectionWidth()
    if name == "PROJECTOR_HEIGHT":
        return config.getProjectionHeight()
    if name == "TARGET_OVERLAP_WIDTH":
        return config.getOverlap()
    if name == "IMAGE_PATH":
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), config.getImageName()
        )
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
