import cv2
import numpy as np


class MaskCreator:
    """Creates a linear gradient mask for edge blending (no gamma compensation).

    Attributes (from UML):
        gamma     (float) – gamma exponent (1.0 = linear, no compensation)
        overlapPx (int)   – width of the overlap region in pixels
    """

    def __init__(self, gamma, overlapPx):
        # --- UML private attributes ---
        self.gamma = gamma          # float  (1.0 for linear)
        self.overlapPx = overlapPx  # int

    # --- UML public methods ---

    def createMask(self, side, height, width):
        """Creates a 3-channel linear gradient mask for the given side (Mat).

        With gamma = 1.0 the formulas simplify to:
        - Left:  alpha = 1 - x
        - Right: alpha = x

        Parameters
        ----------
        side   : str   – ``'left'`` or ``'right'``
        height : int   – mask height (pixels)
        width  : int   – mask width  (pixels)

        Returns
        -------
        numpy.ndarray – 3-channel (BGR) float32 mask with values in [0, 1].
        """
        mask = np.ones((height, width), dtype=np.float32)

        for i in range(self.overlapPx):
            x = i / self.overlapPx  # normalised position 0 -> 1

            if side == "left":
                # Linear fade-out: alpha = 1 - x
                alpha = 1.0 - x
                col_idx = width - self.overlapPx + i
                if 0 <= col_idx < width:
                    mask[:, col_idx] = alpha
            else:  # right
                # Linear fade-in: alpha = x
                alpha = x
                if i < width:
                    mask[:, i] = alpha

        # Expand to 3 channels so it can be multiplied with a BGR image
        return cv2.merge([mask, mask, mask])
