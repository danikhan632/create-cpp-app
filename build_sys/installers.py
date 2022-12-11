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

    man = listPackageManagers()
    if len(man) ==0 or "darwin" not in platform.system().lower():
        install_pkg_mgr()
    else:
        selectPackageManager(man)



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
    if isInstalled("rpm"):
        count+=1
        managers.append("rpm")
    return managers

def selectPackageManager(managers):
    if "darwin" in platform.system().lower():
        print("mac detected")
        os.system("xcode-select --install")    
        if not isInstalled("brew"):
            print("No Package Manager installed, installing brew now")
            os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        brewInstall()
        return

    ok = False
    for i in range(0, len(managers)):
        print(str(i)+" "+ managers[i])
    slect = int(str(input("select package manager to use: ")))
    while not ok:
        if slect >= 0 and slect <= len(managers)-1:
            ok=True
        else:
            print("please make a valid choice: ")
            int(input("select package manager to use: "))

    if managers[slect] == "brew":
        brewInstall()
    elif managers[slect] == "pip":
        pipInstall()
    elif managers[slect] == "apt":
        aptInstall()
    elif managers[slect] == "dnf":
        dnfInstall()
    else:
        print("no package manager detected")
    
def brewInstall():
    os.system("brew install conan")
    os.system("brew install cmake")
    os.system("brew install clang")
    if isInstalled("apt"):
         os.system("sudo apt-get install -y build-essential")
    elif isInstalled("dnf"):
        os.system("sudo dnf install make automake gcc gcc-c++ kernel-devel")

def pipInstall():
    os.system("sudo pip install conan")
    os.system("sudo pip install cmake")
    os.system("sudo pip install clang")
    if isInstalled("apt"):
        os.system("sudo apt-get install -y build-essential")
    elif isInstalled("dnf"):
        os.system("sudo dnf install make automake gcc gcc-c++ kernel-devel")

def aptInstall():
    os.system("sudo apt-get install -y build-essential")
    os.system("sudo apt-get install -y conan")
    os.system("sudo apt-get install -y cmake")
    os.system("sudo apt-get install -y clang")
def dnfInstall():
    os.system("sudo dnf install cmake")
    os.system("sudo dnf install conan")
    os.system("sudo dnf install make automake gcc gcc-c++ kernel-devel")



def install_code_addons(data):
    cont= True
    vscode=""
    if cont:
        vscode=str(input("install vscode packages? y or n:  "))
    

    while cont:
            if vscode == "y":
                os.system("code --install-extension ms-vscode.cpptools-extension-pack")
                os.system("code --install-extension twxs.cmake")
                os.system("code --install-extension FireBlackHat.conan-tools")
                os.system("code --install-extension disroop.conan")
                os.system("code --install-extension DamianKoper.gdb-debug")
                os.system("code --install-extension matepek.vscode-catch2-test-adapter")
                os.system("code --install-extension ms-vscode.cmake-tools")
                os.system("code --install-extension ms-vscode.makefile-tools")
                os.system("code --install-extension hbenl.vscode-test-explorer")
                cont=False
                data["bootstraped"]=True
                json.dump(data, open(".config/data.json", "w"), indent = 4)
            elif vscode == "n":
                cont=False
            else:
                print("please make a valid choice")
                vscode=str(input("install vscode packages? y or n:  "))
def openCode():
    vscode=str(input("open vs_code? y or n:  "))
    if vscode.lower() == "y":
        if isInstalled("code"):
            sleep(1)
            os.system("code .")
        else:
            os.system("pwd")
            print("vscode installation not found")
            print("https://code.visualstudio.com/download")
    else:
        os.system("pwd")
        print("\n\n\n")
        print("type \"cpx\" to terminal to see all options such as \"cpx dev\" to build and run\n")
        print("Happy Hacking!!!")




def install_pkg_mgr():
    print("No Package Manager installed, installing manager now")
    managers= ["brew","pip"]

    ok = False
    for i in range(0, len(managers)):
        print(str(i)+" "+ managers[i])
    slect = int(str(input("select package manager to install: ")))
    while not ok:
        if slect >= 0 and slect <= len(managers)-1:
            ok=True
        else:
            print("please make a valid choice: ")
            int(input("select package manager to install: "))

    if managers[slect] == "brew":
        os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        brewInstall()
    elif managers[slect] == "pip":
        os.system("wget https://bootstrap.pypa.io/get-pip.py")
        os.system("python3 ./get-pip.py")
        pipInstall()