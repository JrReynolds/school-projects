cmake_minimum_required(VERSION 3.6)
project(julia_colors)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    main.cpp JColors.cpp JColors.h RGB.cpp RGB.h)

add_executable(julia_colors ${SOURCE_FILES})