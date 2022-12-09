cmake_minimum_required(VERSION 3.16)
project(multiply_test LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

enable_testing()

add_subdirectory(src)
add_subdirectory(tests)

include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        release-1.11.0
)
FetchContent_MakeAvailable(googletest)
add_library(GTest::GTest INTERFACE IMPORTED)
target_link_libraries(GTest::GTest INTERFACE gtest_main)

add_executable(multiply_test multiply_test.cpp)

target_link_libraries(multiply_test
 PRIVATE
  GTest::GTest
  multiply)

add_test(multiply_gtests multiply_test)





# include(FetchContent)
# FetchContent_Declare(
#   googletest
#   URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
# )
# set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "./output")
# list(APPEND CMAKE_PREFIX_PATH "./vcpkg/packages/gtest_x64-linux/share/gtest/")
# find_package(GTest)
# target_link_libraries(main PRIVATE GTest::gmock GTest::gtest GTest::gmock_main GTest::gtest_main)
# enable_testing()
# add_executable(
# student_test
#   tests/student_test.cpp
# )
# target_link_libraries(
# student_test
#   GTest::gtest_main
# )

# include(GoogleTest)
# gtest_discover_tests(student_test)