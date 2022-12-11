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
    os.system("sudo chmod -R 777 ./bin/"+data["proj_name"])
    os.system("sudo docker container rm cpx_container")
    os.system("sudo docker build -t cpx_builder .")
    os.system("sudo docker create --name cpx_container cpx_builder ")
    os.system("sudo docker cp cpx_container:/app/output/"+data["proj_name"]+" ./output/")

# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

