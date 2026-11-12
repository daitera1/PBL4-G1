## \mainpage Alpha Blending Multi-Projector Documentation
#
# \section intro_sec 1. Introduction
#
# This is the User Manual for the Multi-Projector Alpha Blending application.
# The program displays one image across two adjacent projectors and applies a
# gamma-corrected alpha mask to the overlapping region, so that the final
# projected image looks like one large, seamless picture.
# The application reads its settings (image path, projector distance, gamma, etc.)
# from a configuration file and uses OpenCV and NumPy for image processing.
#
# This User Manual is divided into the following sections:
# - \ref req_sec
# - \ref setup_sec
# - \ref arch_sec
# - \ref math_sec
# - \ref vis_sec
# - \ref usage_sec
#
# \note Beginners may skip the "Mathematical Foundation" section and start with
# "System Requirements" and "Setup".
#
# \section req_sec 2. System Requirements
#
# - <b>Operating System</b>: Windows 10 / 11 (tested)
# - <b>Python</b>: 3.9 or later
# - <b>Required Python Libraries</b>:
#   1. numpy
#   2. opencv-python
# - <b>Hardware</b>: two projectors placed side by side with an overlapping area
#
# \section setup_sec 3. Setup
#
# <b>Step 1: Install required packages</b>
#
# Run the following command:
# \code{.sh}
# pip install -r requirements.txt
# \endcode
#
# <b>Step 2: Configure the settings</b>
#
# Open \c config.json and adjust the values if needed:
# - <b>image_name</b>: path to the image you want to project
# - <b>side</b>: \c left or \c right, the position of this projector
# - <b>distance_between_projectors</b>: distance between the two projectors (cm)
# - <b>projected_image_width</b>: width of one projector's image (cm)
# - <b>gamma</b>: gamma value used when creating the mask
#
# <b>Step 3: Run the program</b>
# \code{.sh}
# python main_alpha_blender.py
# \endcode
#
# \section arch_sec 4. System Architecture
#
# The application consists of two main components:
#
# 1. <b>MainAlphaBlender</b>: the main controller class. It loads the image,
#    calculates the overlap region and applies the alpha mask.
# 2. <b>ConfigReader</b>: a helper class that reads \c config.json and provides
#    getter methods for the projector parameters.
#
# \section math_sec 5. Mathematical Foundation
#
# Projectors do not have a linear luminance response, so simple linear blending
# produces bright or dark bands in the overlap region. Gamma correction is used
# to compensate for this:
#
# \f[
#   M(x) = B(x)^{1/\gamma}
# \f]
#
# where:
# - \f$M(x)\f$ is the calculated mask value,
# - \f$B(x)\f$ is the linear ramp value (0 to 1),
# - \f$\gamma\f$ is the gamma value (typically 2.2 to 2.4).
#
# \section vis_sec 6. Visualization of the Blending Process
#
# \subsection before_sec Before Mask Application
#
# The raw left and right projector inputs. Without the mask, the overlap region
# appears brighter than the rest of the image.
#
# \image html Left.jpg "Left projector input" width=45%
# \image html Right.jpg "Right projector input" width=45%
#
# \subsection after_sec After Mask Application
#
# After applying the gamma-corrected alpha mask, the brightness in the overlap
# region matches the rest of the image.
#
# \image html final.png "Blended result" width=90%
#
# \section usage_sec 7. Usage Notes
#
# - Make sure both projectors use the same resolution (e.g. 1920x1080).
# - If a visible seam remains, adjust the \c gamma value in \c config.json.
# - Press any key or close the window to exit the program.
