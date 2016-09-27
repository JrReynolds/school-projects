cmake_minimum_required(VERSION 3.6)
project(julia)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp extra.cpp extra.h)
add_executable(julia ${SOURCE_FILES})