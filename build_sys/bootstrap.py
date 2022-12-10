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
from .installers import system_config,installing_deps,install_code_addons


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
    installing_deps(data)
    install_code_addons(data)
    change_proj_name(data)
    update_docker_files("myproj",data)

    os.system("curl https://hackgtstoragebucket.s3.amazonaws.com/cpx.json > ~/.cpx.json")
    os.system("python3 scripts.py dev")






