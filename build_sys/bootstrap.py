import json
import platform
from time import sleep
# os.system()
import os
import sys
from .change_name import change_proj_name
from distutils.spawn import find_executable


def isInstalled(pkg):
    
    return find_executable(pkg) is not None

def is_cpx_boot():
    res= os.popen("cat ~/.cpx.json").read()
    if "true" in res:
        return True
    return False

def bootstrap(data):
    if os.name != "posix":
        print("Only mac and linux are supported, please use WSL")
        return
    cont= not is_cpx_boot()
    vscode=""
    print(cont)
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
    


    if is_cpx_boot()==False: 
        os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        os.system("brew install conan")
        os.system("brew install cmake")
        os.system("brew install clang")
        data["brewed"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
        data["piped"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)


        if "Darwin" in platform.system():
            os.system("xcode-select --install")
            data["os"]="mac"
            data["gcced"]=True
            json.dump(data, open(".config/data.json", "w"), indent = 4)

        elif "Linux" in platform.system() or "linux" in platform.system():
            if isInstalled("apt"):
                data["os"]="deb"
                os.system("sudo apt install -y build-essential")
                
            elif isInstalled("pacman"):
                data["os"]="arch"
                os.system("sudo pacman -Sy base-devel")
            data["gcced"]=True
            json.dump(data, open(".config/data.json", "w"), indent = 4)

    
    change_proj_name(data)
    data["bootstraped"]=True
    json.dump(data, open(".config/data.json", "w"), indent = 4)
    os.system("curl https://hackgtstoragebucket.s3.amazonaws.com/cpx.json > ~/.cpx.json")
    os.system("python3 scripts.py dev")
    # sleep(1)
    # if isInstalled("code"):
    #     os.system("code .")

