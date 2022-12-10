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
    ok = False
    slec = str(input("\r\nis this correct? (y or n): "))
    while not ok:
        if "y" in slec.lower():
            ok=True
        elif "n" in slec.lower():
            print("aborting")
            exit()
        else:
            print("please make a valid choice: ")
            slec = str(input("\r\nis this correct? (y or n): "))

    if "darwin" in platform.system().lower():
        print("mac detected")
        os.system("xcode-select --install")
        data["os"]="mac"
        data["gcced"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)


    print(listPackageManagers())

    if not isInstalled("brew"): 
        os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        os.system("brew install conan")
        os.system("brew install cmake")
        os.system("brew install clang")
        data["brewed"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
        data["piped"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)





def system_config(data):
    build_info = "\n\n\nThe following info has been detected:\r\nOperating System: "+platform.system()+"\r\nbrew installled: "+str(isInstalled("brew"))+"\r\npip installed: "+str(isInstalled("brew"))+"\r\nArchitecture: "+platform.architecture()[0] +"\r\nMachine: " + platform.machine()+ "\r\nNode: " + platform.node()+"\r\n apt: "+str(isInstalled("brew")) +"\r\n rpm: "+str(isInstalled("rpm")) +"\r\n yum: "+str(isInstalled("yum")) +"\r\n yum: "+str(isInstalled("yum"))
    return build_info



def listPackageManagers():
    managers=[]
    count=0
    if isInstalled("brew"):
        count+=1
        managers.append("brew")
    if isInstalled("pip"):
        count+=1
        managers.append("pip")
    if isInstalled("apt"):
        count+=1
        managers.append("apt")
    if isInstalled("dnf"):
        count+=1
        managers.append("dnf")
    if isInstalled("yum"):
        count+=1
        managers.append("yum")
    if isInstalled("rpm"):
        count+=1
        managers.append("rpm")
    return managers