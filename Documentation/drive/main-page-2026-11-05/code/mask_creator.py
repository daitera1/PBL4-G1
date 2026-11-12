#!/usr/bin/env python
# -*- coding: utf-8 -*-


## @brief Creates the blending mask applied to the overlap region.
#
#  Generates a gradient mask based on the gamma value and
#  overlap pixel width, used to smoothly blend the two
#  projected images together.
#
#  UML class diagram:
#  @image html 3.png "MaskCreator UML Class Diagram"
class MaskCreator(object):


    ## @brief Initialises MaskCreator with default None values.
    def __init__(self):

        ## @brief Gamma value controlling the blending curve shape.
        self.gamma = None

        ## @brief Width of the overlap region in pixels.
        self.overlapPx = None


    ## @brief Generates and returns the blending mask.
    #  @return Mat The blending mask as a gradient Mat object.
    def createMask(self):
        pass
