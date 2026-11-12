#!/usr/bin/env python
# -*- coding: utf-8 -*-


## @brief Splits the source image into left and right halves.
#
#  Crops the full stitched image into two sub-images,
#  one for each projector, accounting for the overlap region.
class CropImage(object):


    ## @brief Initialises CropImage with default None values.
    def __init__(self):

        ## @brief The left half of the image sent to the left projector.
        self.img_left = None

        ## @brief The right half of the image sent to the right projector.
        self.img_right = None


    ## @brief Crops the source image into left and right sub-images.
    #  @return void
    def crop(self):
        pass
