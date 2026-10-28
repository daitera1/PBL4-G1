import os

# --- CONFIGURATION ---
PROJECTOR_WIDTH = 1920
PROJECTOR_HEIGHT = 1080
TARGET_OVERLAP_WIDTH = 1280
GAMMA = 1.5  # Shared by left and right so they always match. Increase for a steeper/more concave blend curve, decrease for flatter

# Resolved relative to this folder so the scripts work from any working directory
IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_picture.jpg")

LEFT_WINDOW_NAME = "Left Projector"
RIGHT_WINDOW_NAME = "Right Projector"
