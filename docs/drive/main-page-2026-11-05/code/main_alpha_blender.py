#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config_reader import ConfigReader


## @brief Entry point for the alpha blending system.
#
#  Controls the overall image stitching pipeline using
#  two projectors with gamma-based alpha blending.
#
#  UML class diagram:
#  @image html 4.png "MainAlphaBlender UML Class Diagram"
class MainAlphaBlender(object):


    ## @brief Initialises MainAlphaBlender and its ConfigReader.
    def __init__(self):
        ## @brief Config reader instance for loading projector settings.
        self.__configReader = None


    ## @brief Displays the stitched image across both projectors.
    #  @return void
    def display(self):
        pass
