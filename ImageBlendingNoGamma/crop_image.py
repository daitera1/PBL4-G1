class CropImage:
    """Crops a full image into left and right halves with an overlap region.

    Depends on ConfigReader for the overlap width.

    Attributes (from UML):
        img_left  (Mat) – the left cropped portion of the image
        img_right (Mat) – the right cropped portion of the image
    """

    def __init__(self, config_reader, image):
        # --- UML private attributes ---
        self.img_left = None   # Mat
        self.img_right = None  # Mat

        # Dependencies from ConfigReader
        self._image = image
        self._overlap_width = config_reader.p_overlap

    # --- UML public methods ---

    def crop(self):
        """Splits the image into overlapping left and right halves (void).

        After calling this method, ``img_left`` and ``img_right`` are populated.
        """
        img_height, img_width = self._image.shape[:2]
        half_width = img_width // 2

        overlap_end = half_width + (self._overlap_width // 2)
        overlap_start = half_width - (self._overlap_width // 2)

        self.img_left = self._image[:, :overlap_end].copy()
        self.img_right = self._image[:, overlap_start:].copy()
