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
    if len(man) ==0:
        install_pkg_mgr()
    else:
        selectPackageManager(man,data)



def system_config(data):
    build_info = "\n\n\nThe following info has been detected:\r\nOperating System: "+platform.system()+"\r\nbrew installled: "+str(isInstalled("brew"))+"\r\npip3 installed: "+str(isInstalled("pip3"))+"\r\nArchitecture: "+platform.architecture()[0] +"\r\nMachine: " + platform.machine()+ "\r\nNode: " + platform.node()+"\r\n apt: "+str(isInstalled("apt") and "darwin" not in platform.system().lower()) +"\r\n rpm: "+str(isInstalled("rpm")) +"\r\n yum: "+str(isInstalled("yum")) +"\r\n pacman: "+str(isInstalled("pacman")) +"\r\n docker: "+str(isInstalled("docker"))
    return build_info



def listPackageManagers():
    managers=[]
    count=0
    if isInstalled("brew"):
        count+=1
        managers.append("brew")
    if isInstalled("pip3"):
        count+=1
        managers.append("pip3")
    if isInstalled("apt"):
        count+=1
        managers.append("apt")
    if isInstalled("dnf"):
        count+=1
        managers.append("dnf")
    if isInstalled("pacman"):
        count+=1
        managers.append("pacman")
    return managers

def selectPackageManager(managers,data):
    
    ok = False
    print("The following packages will be installed and scanned:\r\nconan: "+str(isInstalled("conan")) + "\r\ncmake: "+str(isInstalled("cmake")) +"\r\ngcc: "+str(isInstalled("gcc"))+"\n\n")
    for i in range(0, len(managers)):
        print(str(i)+": "+ managers[i])
    slect = int(str(input("select package manager to use\nEnter 6 to install skip native installation and use Docker Mode\nEnter 7 to install pip3\nEnter 8 to install brew\nEnter 9 to skip package installation: ")))
    while not ok:
        if (slect >= 0 and slect <= len(managers)-1) or slect==9 or slect==8 or slect==7 or slect ==6:
            ok=True
        else:
            print("please make a valid choice: ")
            slect = int(str(input("select package manager to use or enter 9 to skip package installation: ")))
    if slect==9:
        return
    elif slect==8:
        os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        brewInstall()
    elif slect==7:
        os.system("wget https://bootstrap.pypa.io/get-pip.py")
        os.system("python3 ./get-pip.py")
        pipInstall()
    elif slect==6:
        data["useDocker"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
        dockerMode()
    elif managers[slect] == "brew":
        brewInstall()
    elif managers[slect] == "pip3":
        pipInstall()
    elif managers[slect] == "apt":
        aptInstall()
    elif managers[slect] == "dnf":
        dnfInstall()
    elif managers[slect] == "pacman":
        pacmanInstall()
    else:
        print("no package manager detected")
    
def brewInstall():
    os.system("brew install conan")
    os.system("brew install cmake")
    os.system("brew install clang")
    os.system("brew install neofetch")
    if isInstalled("apt"):
         os.system("sudo apt-get install -y build-essential")
    elif isInstalled("dnf"):
        os.system("sudo dnf install make automake gcc gcc-c++ kernel-devel")
    elif isInstalled("pacman"):
        os.system("sudo pacman -S base-devel")
    elif "darwin" in platform.system().lower():
        print("Apple Macintosh")
        os.system("xcode-select --install")


def pipInstall():
    os.system("sudo pip3 install conan")
    os.system("sudo pip3 install cmake")
    os.system("sudo pip3 install clang")
    if isInstalled("apt"):
        os.system("sudo apt-get install -y build-essential")
        os.system("sudo apt-get install neofetch")
    elif isInstalled("dnf"):
        os.system("sudo dnf install make automake gcc gcc-c++ kernel-devel")
        os.system("sudo dnf install neofetch")
    elif isInstalled("pacman"):
        os.system("sudo pacman -S base-devel")
        os.system("sudo pacman -S neofetch")

    elif "darwin" in platform.system().lower():
        print("Apple Macintosh")
        os.system("xcode-select --install")

def aptInstall():
    os.system("sudo apt-get install -y build-essential")
    os.system("sudo apt-get install -y conan")
    os.system("sudo apt-get install -y cmake")
def dnfInstall():
    os.system("sudo dnf install cmake")
    os.system("sudo dnf install conan")
    os.system("sudo dnf install make automake gcc gcc-c++ kernel-devel")
def pacmanInstall():
    os.system("sudo pacman -Syu")
    os.system("sudo pacman -S base-devel")
    os.system("sudo pacman -Syu cmake")
    os.system("sudo pacman -Syu conan")
    if isInstalled("brew"):
        os.system("brew install conan")
    elif isInstalled("pip3"):
        os.system("sudo pip3 install conan")
    else:
        os.system("wget https://bootstrap.pypa.io/get-pip.py")
        os.system("sudo python3 ./get-pip.py")

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
    managers= ["brew","pip3"]

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
    elif managers[slect] == "pip3":
        os.system("wget https://bootstrap.pypa.io/get-pip.py")
        os.system("sudo python3 ./get-pip.py")
        pipInstall()

def dockerMode():
    if "darwin" in platform.system().lower():
        if not isInstalled("docker"):
            if not isInstalled("brew"):
                os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            os.system("brew install --cask docker")
    elif not isInstalled("docker"):
        os.system("sudo true")
        os.system("wget -qO- https://get.docker.com/ | sh")