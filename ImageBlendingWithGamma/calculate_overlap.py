import cv2
import numpy as np


class CalculateOverlap:
    """Applies the alpha-gamma mask to a cropped image and positions it on
    a projector-sized canvas.

    Depends on ConfigReader for side, overlap, and projector dimensions.

    Attributes (from UML):
        side         (String) – ``'left'`` or ``'right'``
        overlapWidth (int)    – effective overlap width in pixels
    """

    def __init__(self, config_reader, cropped_image, mask):
        # --- UML private attributes (sourced from ConfigReader) ---
        self.side = config_reader.getSide()                    # String
        self.overlapWidth = config_reader.p_overlap            # int

        # Internal state needed by alphaGamma()
        self._cropped_image = cropped_image
        self._mask = mask
        self._projector_width = config_reader.getProjectionWidth()
        self._projector_height = config_reader.getProjectionHeight()

    # --- UML public methods ---

    def alphaGamma(self):
        """Applies the gradient mask and returns the canvas-placed result (Mat).

        The blended image is positioned on a black canvas sized to the
        projector resolution:
        - **left** side  → right-aligned on the canvas
        - **right** side → left-aligned on the canvas

        Returns
        -------
        numpy.ndarray – BGR uint8 image at projector resolution.
        """
        # Apply the gradient mask
        blended = (self._cropped_image.astype(np.float32) * self._mask).astype(np.uint8)

        target_w = self._projector_width
        target_h = self._projector_height
        h, w = blended.shape[:2]

        canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
        new_w = int(w * (target_h / h))
        resized = cv2.resize(blended, (new_w, target_h))

        if self.side == "left":
            # Right-align for the left projector
            if new_w <= target_w:
                canvas[:, target_w - new_w:] = resized
            else:
                canvas = cv2.resize(blended, (target_w, target_h))
        else:
            # Left-align for the right projector
            if new_w <= target_w:
                canvas[:, :new_w] = resized
            else:
                canvas = cv2.resize(blended, (target_w, target_h))

        return canvas
