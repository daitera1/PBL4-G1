## \page class_overview Class Overview
#
# This page gives an overview of all classes in the Alpha Blender system
# and explains how they work together. Click a class name to open its
# detailed reference page.
#
# \section class_list_sec Class List
#
# | Class | File | Responsibility |
# |-------|------|----------------|
# | \ref main_alpha_blender.MainAlphaBlender "MainAlphaBlender" | main_alpha_blender.py | Entry point. Controls the whole pipeline and displays the final image. |
# | \ref config_reader.ConfigReader "ConfigReader" | config_reader.py | Reads projector and image settings (width, distance, overlap, gamma, side). |
# | \ref image_read_write.ImageReadWrite "ImageReadWrite" | image_read_write.py | Loads the source image from disk as an OpenCV Mat. |
# | \ref crop_image.CropImage "CropImage" | crop_image.py | Splits the source image into left and right parts for each projector. |
# | \ref calculate_overlap.CalculateOverlap "CalculateOverlap" | calculate_overlap.py | Calculates the overlap width and the gamma-corrected alpha values. |
# | \ref mask_creator.MaskCreator "MaskCreator" | mask_creator.py | Creates the gradient mask applied to the overlap region. |
#
# \section class_flow_sec Processing Flow
#
# 1. \b MainAlphaBlender starts the program and creates a \b ConfigReader.
# 2. \b ConfigReader loads all projector and image parameters.
# 3. \b ImageReadWrite reads the source image.
# 4. \b CropImage cuts the image into the left and right parts.
# 5. \b CalculateOverlap determines the overlap region for this projector side.
# 6. \b MaskCreator builds the gamma-based blending mask.
# 7. \b MainAlphaBlender applies the mask and displays the result in full screen.
#
# \section class_detail_sec Class Details
#
# \subsection cd_main MainAlphaBlender
# The controller of the system. It owns the ConfigReader instance and
# calls the other classes in order.
# - Method: \ref main_alpha_blender.MainAlphaBlender.display "display()"
#
# \subsection cd_config ConfigReader
# A helper class that stores every configuration value and provides
# getter methods for them.
# - Main methods: getProjectedImageWidth(), getDistanceBetweenProjector(),
#   getImageWidth(), getImageHeight(), getImageName(), getSide(), getGamma()
#
# \subsection cd_image ImageReadWrite
# Reads the image file given by \c img_filename and keeps it in memory.
# - Method: \ref image_read_write.ImageReadWrite.getImage "getImage()"
#
# \subsection cd_crop CropImage
# Produces \c img_left and \c img_right, the two images sent to the projectors.
# - Method: \ref crop_image.CropImage.crop "crop()"
#
# \subsection cd_overlap CalculateOverlap
# Uses the projector side and overlap width to compute the alpha ramp:
# \f[ I'(x) = (1 - x)^{\gamma} \f]
# - Method: \ref calculate_overlap.CalculateOverlap.alphaGamma "alphaGamma()"
#
# \subsection cd_mask MaskCreator
# Generates the gradient mask from the gamma value and the overlap width
# in pixels.
# - Method: \ref mask_creator.MaskCreator.createMask "createMask()"
