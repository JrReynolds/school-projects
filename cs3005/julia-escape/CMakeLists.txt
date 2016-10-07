cmake_minimum_required(VERSION 3.6)
project(julia_final)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    JEscape.cpp
    JEscape.h
    main.cpp)

add_executable(julia_final ${SOURCE_FILES})
