
import json
import platform
from time import sleep
# os.system()
import os
import sys

from build_sys.data_str import usage_text
from build_sys.tools import test, sanitize, debug, benchmark, run, clean
from build_sys.build import build
from build_sys.change_name import change_proj_name
from build_sys.bootstrap import bootstrap
from build_sys.prod import prod
from build_sys.docker import docker_build
name=""
def main():

    usage = usage_text()
    cof = open('.config/data.json')
    data = json.loads(cof.read())
    if len(sys.argv) == 1:
        print(usage)
    else:
        if str(sys.argv[1]) == "build":
           build(data)
        elif str(sys.argv[1]) == "run":
            run(data)
        elif str(sys.argv[1]) == "bootstrap":
            bootstrap(data)
        elif str(sys.argv[1]) == "dev":
            build(data)
            run(data)
        elif str(sys.argv[1]) == "clean":
            clean(data)
        elif str(sys.argv[1]) == "rename" and len(sys.argv) == 3:
            change_proj_name(data)

        elif str(sys.argv[1]) == "debug":
            debug(data)
        elif str(sys.argv[1]) == "test":
            test(data)
        elif str(sys.argv[1]) == "sanitize":
            sanitize(data)
        elif str(sys.argv[1]) == "benchmark":
            benchmark(data)
        elif str(sys.argv[1]) == "prod":
            prod(data)
        elif str(sys.argv[1]) == "docker":
            if len(sys.argv) == 2:
                print("docker")
            elif len(sys.argv) == 3 and sys.argv[2] =="build":
                docker_build(data)
            
        else:
            print("invalid arguments")



if __name__ == "__main__":
   main()