import json
import platform
from time import sleep
# os.system()
import os
import sys

def change_proj_name(data):
    if sys.argv[2] == "" or " " in sys.argv[2]:
        return
    old_name=""
    old_name=data["proj_name"]
    # print("dec ",old_name, sys.argv[2])
    data["proj_name"] = sys.argv[2]

    repl =(open('CMakeLists.txt').read())
    # print(repl)
    repl=repl.replace(old_name, sys.argv[2])
    # print(repl)
    file = open('CMakeLists.txt', 'w', encoding='utf-8')
    file.write(repl)
    json.dump(data, open(".config/data.json", "w"), indent = 4)