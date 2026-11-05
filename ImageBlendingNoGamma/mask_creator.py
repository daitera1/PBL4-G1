import cv2
import numpy as np


class MaskCreator:
    """Creates a linear gradient mask for edge blending (no gamma compensation).

    Uses the global configuration variable by default for gamma (1.0) and overlap values.

    Attributes (from UML):
        gamma     (float) – gamma exponent (1.0 = linear, no compensation)
        overlapPx (int)   – width of the overlap region in pixels
    """

    def __init__(self, config_reader=None, gamma=None, overlapPx=None):
        if config_reader is None and gamma is None and overlapPx is None:
            from config import config as global_config
            config_reader = global_config

        # --- UML private attributes ---
        if config_reader is not None and hasattr(config_reader, "getGamma"):
            self._gamma = config_reader.getGamma()
            self._overlapPx = config_reader.getOverlap()
        else:
            self._gamma = float(config_reader if config_reader is not None else (gamma if gamma is not None else 1.0))
            self._overlapPx = int(overlapPx if overlapPx is not None else (gamma if gamma is not None else 1280))

        self._mask = None

    # --- Property accessors (for backward compatibility) ---

    @property
    def gamma(self):
        return self.getGamma()

    @gamma.setter
    def gamma(self, val):
        self.setGamma(val)

    @property
    def overlapPx(self):
        return self.getOverlapPx()

    @overlapPx.setter
    def overlapPx(self, val):
        self.setOverlapPx(val)

    @property
    def mask(self):
        return self.getMask()

    @mask.setter
    def mask(self, val):
        self.setMask(val)

    # --- Getter methods ---

    def getGamma(self):
        """Returns the gamma value (float)."""
        return self._gamma

    def getOverlapPx(self):
        """Returns the overlap width in pixels (int)."""
        return self._overlapPx

    def getMask(self):
        """Returns the most recently created mask (Mat or None)."""
        return self._mask

    # --- Setter methods ---

    def setGamma(self, gamma):
        """Sets the gamma exponent (void)."""
        self._gamma = float(gamma)

    def setOverlapPx(self, overlapPx):
        """Sets the overlap width in pixels (void)."""
        self._overlapPx = int(overlapPx)

    def setMask(self, mask):
        """Sets the stored gradient mask (void)."""
        self._mask = mask

    # --- UML public methods ---

    def createMask(self, side, height, width):
        """Creates a 3-channel linear gradient mask for the given side (Mat).

        With gamma = 1.0 the formulas simplify to:
        - Left:  alpha = 1 - x
        - Right: alpha = x

        Parameters
        ----------
        side   : str – ``'left'`` or ``'right'``
        height : int – mask height (pixels)
        width  : int – mask width  (pixels)

        Returns
        -------
        numpy.ndarray – 3-channel (BGR) float32 mask with values in [0, 1].
        """
        mask = np.ones((height, width), dtype=np.float32)

        for i in range(self._overlapPx):
            x = i / self._overlapPx  # normalised position 0 -> 1

            if side == "left":
                # Linear fade-out: alpha = 1 - x
                alpha = 1.0 - x
                col_idx = width - self._overlapPx + i
                if 0 <= col_idx < width:
                    mask[:, col_idx] = alpha
            else:  # right
                # Linear fade-in: alpha = x
                alpha = x
                if i < width:
                    mask[:, i] = alpha

        # Expand to 3 channels so it can be multiplied with a BGR image
        self._mask = cv2.merge([mask, mask, mask])
        return self._mask
