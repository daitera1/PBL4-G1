import cv2
import numpy as np


class CalculateOverlap:
    """Applies the alpha mask to a cropped image and positions it on
    a projector-sized canvas (no gamma compensation).

    Uses the global configuration variable by default for side, overlap,
    and projector dimensions.

    Attributes (from UML):
        side         (String) – ``'left'`` or ``'right'``
        overlapWidth (int)    – effective overlap width in pixels
    """

    def __init__(self, *args, **kwargs):
        cfg = None
        cropped = None
        mask = None

        if len(args) == 2:
            cropped = args[0]
            mask = args[1]
        elif len(args) >= 3:
            cfg = args[0]
            cropped = args[1]
            mask = args[2]

        cropped = kwargs.get("cropped_image", cropped)
        mask = kwargs.get("mask", mask)
        cfg = kwargs.get("config_reader", kwargs.get("config", cfg))

        if cfg is None:
            from config import config as global_config
            cfg = global_config

        # --- UML private attributes ---
        self._side = cfg.getSide() if cfg else "left"
        self._overlapWidth = cfg.getOverlap() if cfg else 1280

        # Internal state
        self._cropped_image = cropped
        self._mask = mask
        self._projector_width = cfg.getProjectionWidth() if cfg else 1920
        self._projector_height = cfg.getProjectionHeight() if cfg else 1080
        self._blended_result = None

    # --- Property accessors (for backward compatibility) ---

    @property
    def side(self):
        return self.getSide()

    @side.setter
    def side(self, val):
        self.setSide(val)

    @property
    def overlapWidth(self):
        return self.getOverlapWidth()

    @overlapWidth.setter
    def overlapWidth(self, val):
        self.setOverlapWidth(val)

    # --- Getter methods ---

    def getSide(self):
        """Returns the blending side – 'left' or 'right' (String)."""
        return self._side

    def getOverlapWidth(self):
        """Returns the overlap width in pixels (int)."""
        return self._overlapWidth

    def getProjectorWidth(self):
        """Returns the target canvas width (int)."""
        return self._projector_width

    def getProjectorHeight(self):
        """Returns the target canvas height (int)."""
        return self._projector_height

    def getCroppedImage(self):
        """Returns the cropped input image (Mat)."""
        return self._cropped_image

    def getMask(self):
        """Returns the gradient mask (Mat)."""
        return self._mask

    def getBlendedResult(self):
        """Returns the blended and canvas-positioned image (Mat or None)."""
        return self._blended_result

    # --- Setter methods ---

    def setSide(self, side):
        """Sets the blending side – 'left' or 'right' (void)."""
        self._side = str(side)

    def setOverlapWidth(self, overlap_width):
        """Sets the overlap width in pixels (void)."""
        self._overlapWidth = int(overlap_width)

    def setProjectorWidth(self, width):
        """Sets the canvas projector width in pixels (void)."""
        self._projector_width = int(width)

    def setProjectorHeight(self, height):
        """Sets the canvas projector height in pixels (void)."""
        self._projector_height = int(height)

    def setCroppedImage(self, cropped_image):
        """Sets the cropped input image (void)."""
        self._cropped_image = cropped_image

    def setMask(self, mask):
        """Sets the alpha mask (void)."""
        self._mask = mask

    def setBlendedResult(self, blended_result):
        """Sets the blended result image (void)."""
        self._blended_result = blended_result

    # --- UML public methods ---

    def alphaGamma(self):
        """Applies the linear gradient mask and returns the canvas-placed result (Mat).

        The blended image is positioned on a black canvas sized to the
        projector resolution:
        - **left** side  → right-aligned on the canvas
        - **right** side → left-aligned on the canvas

        Returns
        -------
        numpy.ndarray – BGR uint8 image at projector resolution.
        """
        if self._cropped_image is None or self._mask is None:
            raise ValueError("Cropped image and mask must be set before blending.")

        # Apply the linear gradient mask
        blended = (self._cropped_image.astype(np.float32) * self._mask).astype(np.uint8)

        target_w = self._projector_width
        target_h = self._projector_height

        # Stretch to fill the full projector canvas so both sides align
        canvas = cv2.resize(blended, (target_w, target_h))

        self._blended_result = canvas
        return self._blended_result
