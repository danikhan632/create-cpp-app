import json
import platform
from time import sleep
# os.system()
import os
import pathlib
import sys
from distutils.spawn import find_executable


def isInstalled(pkg):
    return find_executable(pkg) is not None

def installing_deps(data):
    print(system_config(data))

    if not isInstalled("brew"): 
        os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        os.system("brew install conan")
        os.system("brew install cmake")
        os.system("brew install clang")
        data["brewed"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
        data["piped"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)


        if "darwin" in platform.system().lower():
            os.system("xcode-select --install")
            data["os"]="mac"
            data["gcced"]=True
            json.dump(data, open(".config/data.json", "w"), indent = 4)

        else:

            # distribution
            dist = platform.dist()
            dist = " ".join(x for x in dist)
            print("Distribution: " + dist)
            data["os"]="arch"
            data["gcced"]=True
            json.dump(data, open(".config/data.json", "w"), indent = 4)



def system_config(data):
    build_info = "\n\n\nThe following info has been detected:\r\nOperating System: "+platform.system()+"\r\nbrew installled: "+str(isInstalled("brew"))+"\r\npip installed: "+str(isInstalled("brew"))+"\r\nArchitecture: "+platform.architecture()[0] +"\r\nMachine: " + platform.machine()+ "\r\nNode: " + platform.node()+"\r\n apt: "+str(isInstalled("brew")) +"\r\n rpm: "+str(isInstalled("rpm")) +"\r\n yum: "+str(isInstalled("yum")) +"\r\n rpm: "+str(isInstalled("yum"))+"\r\n is this correct(y or n)?: "
    return build_info