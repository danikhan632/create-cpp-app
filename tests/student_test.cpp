#include "../vcpkg/packages/gtest_x64-linux/include/gtest/gtest.h"
#include "../include/student.h"
TEST(StudentTest, id_num) {
    Student bob = Student(4.0f, "bob", 11, 78934);
    EXPECT_EQ(78934,*(bob.get_id()) );
}