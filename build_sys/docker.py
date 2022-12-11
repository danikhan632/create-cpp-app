import json
import platform
from time import sleep
# os.system()
import os
import sys


def update_docker_files(old_name,data):
    cmk=None
    with open('./build_sys/docker_files/Dockerfile.build','r',encoding='utf-8') as file:
        cmk = file.readlines()
    for i in range(0, len(cmk)):
        if old_name in cmk[i]:
            cmk[i]= cmk[i].replace(old_name, data["proj_name"])

    with open('./build_sys/docker_files/Dockerfile.build', 'w', encoding='utf-8') as file:
        file.writelines(cmk)

def docker_build(data):
    os.system("chmod -R 777 ./bin"+data["proj_name"])
    os.system("docker build ./build_sys/docker_files/Dockerfile.build -t myubunt")
    os.system("docker cp myubunt:/bin/"+data["proj_name"]+" ./bin/")

