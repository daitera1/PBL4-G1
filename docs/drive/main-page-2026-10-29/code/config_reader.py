#!/usr/bin/env python
# -*- coding: utf-8 -*-


## @brief Reads and stores projector and image configuration values.
#
#  Provides getter methods for all parameters needed by the
#  stitching pipeline such as projector dimensions, overlap,
#  gamma value, and image metadata.
class ConfigReader(object):


    ## @brief Initialises ConfigReader with default None values.
    def __init__(self):
        ## @brief Width of the projected image in pixels.
        self.p_width = None

        ## @brief Height of the projector in physical units.
        self.p_height = None

        ## @brief Distance between the two projectors in cm.
        self.p_distance = None

        ## @brief Overlap width between the two projected images in pixels.
        self.p_overlap = None

        ## @brief Projection length (throw distance) in cm.
        self.p_length = None

        ## @brief Gamma value used for alpha blending curve.
        self.gamma = None


    ## @brief Returns the projected image width.
    #  @return int Width in pixels.
    def getProjectedImageWidth(self):
        pass


    ## @brief Returns the distance between the two projectors.
    #  @return float Distance in cm.
    def getDistanceBetweenProjector(self):
        pass


    ## @brief Returns the image width.
    #  @return int Width in pixels.
    def getImageWidth(self):
        pass


    ## @brief Returns the image height.
    #  @return int Height in pixels.
    def getImageHeight(self):
        pass


    ## @brief Returns the image filename.
    #  @return str Filename of the source image.
    def getImageName(self):
        pass


    ## @brief Returns which side this projector handles.
    #  @return str Either 'left' or 'right'.
    def getSide(self):
        pass


    ## @brief Returns the gamma value for blending.
    #  @return float Gamma value.
    def getGamma(self):
        pass


    ## @brief Returns the projection length (throw distance).
    #  @return float Length in cm.
    def getProjectionLength(self):
        pass


    ## @brief Returns the projection width.
    #  @return int Width in pixels.
    def getProjectionWidth(self):
        pass


    ## @brief Returns the projector height.
    #  @return int Height in pixels.
    def getProjectionHeight(self):
        pass
