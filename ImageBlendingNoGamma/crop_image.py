class CropImage:
    """Crops a full image into left and right halves with an overlap region.

    Uses the global configuration variable by default for the overlap width,
    while supporting dependency injection for custom configurations.

    Attributes (from UML):
        img_left  (Mat) – the left cropped portion of the image
        img_right (Mat) – the right cropped portion of the image
    """

    def __init__(self, *args, **kwargs):
        # Resolve config and image flexibly
        # Supports: CropImage(image), CropImage(config_reader, image), CropImage(image, config_reader)
        cfg = None
        img = None

        if len(args) == 1:
            img = args[0]
        elif len(args) >= 2:
            if hasattr(args[0], "getOverlap") or hasattr(args[0], "p_overlap"):
                cfg = args[0]
                img = args[1]
            else:
                img = args[0]
                cfg = args[1]

        img = kwargs.get("image", img)
        cfg = kwargs.get("config_reader", kwargs.get("config", cfg))

        if cfg is None:
            from config import config as global_config
            cfg = global_config

        # --- UML private attributes ---
        self._img_left = None   # Mat
        self._img_right = None  # Mat

        # Internal state
        self._config = cfg
        self._image = img
        self._overlap_width = cfg.getOverlap() if cfg else 1280

    # --- Property accessors (for backward compatibility) ---

    @property
    def img_left(self):
        return self.getImgLeft()

    @img_left.setter
    def img_left(self, val):
        self.setImgLeft(val)

    @property
    def img_right(self):
        return self.getImgRight()

    @img_right.setter
    def img_right(self, val):
        self.setImgRight(val)

    # --- Getter methods ---

    def getImgLeft(self):
        """Returns the left cropped image (Mat)."""
        return self._img_left

    def getImgRight(self):
        """Returns the right cropped image (Mat)."""
        return self._img_right

    def getImage(self):
        """Returns the input image before cropping (Mat)."""
        return self._image

    def getOverlapWidth(self):
        """Returns the overlap width used for cropping (int)."""
        return self._overlap_width

    # --- Setter methods ---

    def setImgLeft(self, img_left):
        """Sets the left cropped image (void)."""
        self._img_left = img_left

    def setImgRight(self, img_right):
        """Sets the right cropped image (void)."""
        self._img_right = img_right

    def setImage(self, image):
        """Sets the input image to be cropped (void)."""
        self._image = image

    def setOverlapWidth(self, overlap_width):
        """Sets the overlap width used for cropping (void)."""
        self._overlap_width = int(overlap_width)

    # --- UML public methods ---

    def crop(self):
        """Splits the image into overlapping left and right halves (void).

        After calling this method, ``_img_left`` and ``_img_right`` are populated.
        """
        if self._image is None:
            raise ValueError("No image set to crop.")

        img_height, img_width = self._image.shape[:2]
        half_width = img_width // 2

        overlap_end = half_width + (self._overlap_width // 2)
        overlap_start = half_width - (self._overlap_width // 2)

        self._img_left = self._image[:, :overlap_end].copy()
        self._img_right = self._image[:, overlap_start:].copy()
