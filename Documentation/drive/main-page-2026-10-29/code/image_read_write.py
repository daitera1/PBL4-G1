#!/usr/bin/env python
# -*- coding: utf-8 -*-


## @brief Handles reading and writing image files from disk.
#
#  Loads an image from a given filename and provides
#  access to the loaded image as an OpenCV Mat object.
class ImageReadWrite(object):


    ## @brief Initialises ImageReadWrite with default None values.
    def __init__(self):

        ## @brief Path and filename of the image to load.
        self.img_filename = None

        ## @brief The loaded image stored as a Mat object.
        self.image = None


    ## @brief Returns the loaded image.
    #  @return Mat The image loaded from img_filename.
    def getImage(self):
        pass
