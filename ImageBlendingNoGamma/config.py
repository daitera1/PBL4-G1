import os

# --- CONFIGURATION ---
PROJECTOR_WIDTH = 1920
PROJECTOR_HEIGHT = 1080
TARGET_OVERLAP_WIDTH = 1280  # Updated to 1280px overlap

# Resolved relative to this folder so the scripts work from any working directory
IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_picture.jpg")

LEFT_WINDOW_NAME = "Left Projector"
RIGHT_WINDOW_NAME = "Right Projector"
