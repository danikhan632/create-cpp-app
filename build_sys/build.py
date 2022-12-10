import json
import platform
from time import sleep
# os.system()
import os
import sys
from rename import update_execute



def get_src(data):
    exc =" "
    for path, currentDirectory, files in os.walk("./src"):
        for file in files:
            exc+=os.path.join(path, file)+ " "
    return exc

def update_execute(data):
    cmk=None
    with open('CMakeLists.txt','r',encoding='utf-8') as file:
        cmk = file.readlines()
    for i in range(0, len(cmk)):
        if "add_executable" in cmk[i]:
            cmk[i]= "add_executable(" + data["proj_name"] + get_src(data) +")\n"
    with open('CMakeLists.txt', 'w', encoding='utf-8') as file:
        file.writelines(cmk)



def build(data, release=False):
    update_execute(data)
    cmk_string="cmake -DCMAKE_BUILD_TYPE=\"Debug\" cmake ."
    if len(sys.argv) == 3 or release:
        if sys.argv[2] == "release" or release:
            cmk_string= "cmake -DCMAKE_BUILD_TYPE=\"Release\" cmake ."
        
        
    os.system("conan install . --install-folder lib --output-folder ./lib/packages")
    os.system(cmk_string)
    os.system("make")
