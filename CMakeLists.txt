cmake_minimum_required(VERSION 3.0.0)
project(myproj VERSION 0.1.0)
set(CMAKE_CXX_STANDARD 14)


INCLUDE_DIRECTORIES(./include)
include(./lib/conanbuildinfo.cmake)  # Includes the contents of the conanbuildinfo.cmake file.
conan_basic_setup()  # Prepares the CMakeList.txt for Conan.
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ./output) 

set(CMAKE_BUILD_TYPE ${CMAKE_BUILD_TYPE})


add_executable(myproj ./src/helper.cpp ./src/adv.cpp ./src/main.cpp )
TARGET_LINK_LIBRARIES(myproj ${CONAN_LIBS})
