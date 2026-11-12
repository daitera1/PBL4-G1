cmake_minimum_required(VERSION 3.10)
project(ImageBlendingApp)

set(CMAKE_CXX_STANDARD 17)

# Explicitly tell CMake where Homebrew installs packages (supports both Apple Silicon M1/M2/M3/M4 and Intel Macs)
if(EXISTS "/opt/homebrew/opt/opencv")
    list(APPEND CMAKE_PREFIX_PATH "/opt/homebrew/opt/opencv")
elseif(EXISTS "/usr/local/opt/opencv")
    list(APPEND CMAKE_PREFIX_PATH "/usr/local/opt/opencv")
endif()

# Find OpenCV package
find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(ImageBlendingApp main.cpp)

target_link_libraries(ImageBlendingApp ${OpenCV_LIBS})