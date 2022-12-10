import json
import platform
from time import sleep
# os.system()
import os
import sys
import rename 
from build import update_execute



def run(data):
    os.system("./bin/"+data["proj_name"])



def test(data):
    print()

def sanitize(data):
    update_execute(data)
    os.system("conan install . --install-folder lib --output-folder ./lib/packages")
    os.system("cmake -DCMAKE_EXE_LINKER_FLAGS=\"-fno-omit-frame-pointer -fsanitize=address\" -DCMAKE_BUILD_TYPE=\"Debug\" cmake . && make")
    run(data)
    os.system("cmake -DCMAKE_EXE_LINKER_FLAGS=\"\" cmake . && make")

def debug(data):
    os.system("gdb ./bin/"+data["proj_name"] +" run")   

def clean(data):
    # os.system("mv ./CMakeCache.txt .config/cold_store/CMakeCache.txt")
    # os.system("mv ./cmake_install.cmake .config/cold_store/cmake_install.cmake")
    os.system("mv ./lib/conaninfo.txt .config/cold_store/conaninfo.txt")
    os.system("mv ./lib/conanbuildinfo.txt .config/cold_store/conanbuildinfo.txt")
    os.system("mv ./lib/conanbuildinfo.cmake .config/cold_store/conanbuildinfo.cmake")
    os.system("mv ./lib/conan.lock .config/cold_store/conan.lock")
def benchmark(data):
    print()
