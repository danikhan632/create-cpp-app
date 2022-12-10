import json
import platform
from time import sleep
# os.system()
import os
import pathlib
import sys
from .change_name import change_proj_name
from distutils.spawn import find_executable
from .docker import update_docker_files
from .installers import system_config


def isInstalled(pkg):
    return find_executable(pkg) is not None

def is_cpx_boot():
    res= os.popen("cat ~/.cpx.json").read()
    if "true" in res:
        return True
    return False

def bootstrap(data):
    if os.name != "posix":
        print("Windows detected, use in docker mode?")
        return
    print(system_config(data))
    install_code_addons(data)
    change_proj_name(data)
    update_docker_files("myproj",data)
    data["bootstraped"]=True

    json.dump(data, open(".config/data.json", "w"), indent = 4)
    os.system("curl https://hackgtstoragebucket.s3.amazonaws.com/cpx.json > ~/.cpx.json")
    os.system("python3 scripts.py dev")


def openCode():
    cont= False
    vscode=""
    print(cont)
    if cont:
        vscode=str(input("open vs_code? y or n:  "))
    while cont:
            if vscode == "y":
                sleep(1)
                os.system("code .")
            elif vscode == "n":
                cont=False
            else:
                os.sys("pwd")

def install_code_addons(data):
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



