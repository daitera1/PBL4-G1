#!/usr/bin/env python
# -*- coding: utf-8 -*-


## @brief Calculates the alpha blending mask for the overlap region.
#
#  Determines which side (left or right) the projector is on
#  and computes the gamma-corrected alpha values across the
#  overlap zone.
#
#  UML class diagram:
#  @image html 1.png "CalculateOverlap UML Class Diagram"
class CalculateOverlap(object):


    ## @brief Initialises CalculateOverlap with default None values.
    def __init__(self):

        ## @brief Which projector side this instance handles ('left' or 'right').
        self.side = None

        ## @brief Width of the overlap region in pixels.
        self.overlapWidth = None


    ## @brief Computes the gamma-corrected alpha blend mask.
    #
    #  Uses the formula I'(x) = (1 - x)^gamma across the overlap
    #  region to produce a smooth brightness ramp.
    #  @return Mat The computed alpha mask.
    def alphaGamma(self):
        pass
