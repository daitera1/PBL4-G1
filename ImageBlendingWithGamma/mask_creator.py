import cv2
import numpy as np


class MaskCreator:
    """Creates a gamma-compensated gradient mask for edge blending.

    Depends on ConfigReader for gamma and overlap values.

    Attributes (from UML):
        gamma     (float) – gamma compensation exponent
        overlapPx (int)   – width of the overlap region in pixels
    """

    def __init__(self, config_reader):
        # --- UML private attributes (sourced from ConfigReader) ---
        self.gamma = config_reader.getGamma()        # float
        self.overlapPx = config_reader.p_overlap      # int

    # --- UML public methods ---

    def createMask(self, side, height, width):
        """Creates a 3-channel gradient mask for the given side (Mat).

        For the **left** side the alpha fades out across the overlap:
            alpha(x) = (1 - x) ^ gamma

        For the **right** side the alpha fades in across the overlap:
            alpha(x) = x ^ gamma

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
                # Left: full brightness at start of overlap, fading out
                alpha = (1.0 - x) ** self.gamma
                col_idx = width - self.overlapPx + i
                if 0 <= col_idx < width:
                    mask[:, col_idx] = alpha
            else:  # right
                # Right: fading in from dark to full brightness
                alpha = x ** self.gamma
                if i < width:
                    mask[:, i] = alpha

        # Expand to 3 channels so it can be multiplied with a BGR image
        return cv2.merge([mask, mask, mask])
