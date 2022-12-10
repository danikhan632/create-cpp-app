
import json
import platform
from time import sleep
# os.system()
import os
import sys

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

name=""
def main():

    usage = ("Usage:\r\n"
   "python3 scripts.py A"
   "RG\r\n\r\n"
   "dev             to b"
   "uild and run project"
   "\r\n"
   "build           to b"
   "uild: python3 script"
   "s.py build debug or "
   "python3 scripts.py b"
   "uild release\r\n"
   "run             to r"
   "un project\r\n"
   "debug           to d"
   "ebug project\r\n"
   "rename ARG2     to r"
   "ename project, ARG2 "
   "is new name no space"
   "s");

    cof = open('.config/data.json')
    data = json.loads(cof.read())
    name=data["proj_name"]
    first=data["bootstraped"]
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
        else:
            print("invalid arguments")


def debug(data):
    os.system("gdb ./bin/"+data["proj_name"])    


def run(data):
    os.system("./bin/"+data["proj_name"])


def build(data):
    
    clean(data)
    update_execute(data)
    if len(sys.argv) == 3:
        setFlag(data,sys.argv[2])
    os.system("conan install . --install-folder lib --output-folder ./lib/packages")
    os.system("cmake .")
    os.system("make")

def clean(data):
    # os.system("mv ./CMakeCache.txt .config/cold_store/CMakeCache.txt")
    # os.system("mv ./cmake_install.cmake .config/cold_store/cmake_install.cmake")
    os.system("mv ./lib/conaninfo.txt .config/cold_store/conaninfo.txt")
    os.system("mv ./lib/conanbuildinfo.txt .config/cold_store/conanbuildinfo.txt")
    os.system("mv ./lib/conanbuildinfo.cmake .config/cold_store/conanbuildinfo.cmake")
    os.system("mv ./lib/conan.lock .config/cold_store/conan.lock")
    


    # os.system("mv ./ .config/cold_store/")
    


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

def update_execute(data, sanit):
    cmk=None
    with open('CMakeLists.txt','r',encoding='utf-8') as file:
        cmk = file.readlines()
    for i in range(0, len(cmk)):
        if "add_executable" in cmk[i]:
            cmk[i]= "add_executable(" + data["proj_name"] + get_src(data) +")\n"
        elif "fsanitize=address" in cmk[i]:
            if not sanit and "#" in cmk[i]:
                cmk[i]=cmk[i].replace("#", "")
            elif sanit and "#" not in cmk[i]:
                cmk[i]="#"+cmk[i]

    # print(cmk)
    with open('CMakeLists.txt', 'w', encoding='utf-8') as file:
        file.writelines(cmk)

def get_src(data):
    exc =" "
    for path, currentDirectory, files in os.walk("./src"):
        for file in files:
            exc+=os.path.join(path, file)+ " "
    # print(exc)
    return exc



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
    os.system("cpx dev")
    os.system("cpx")
    sleep(1)
    if isInstalled("code"):
        os.system("code .")


def isInstalled(pkg):
    res= os.popen(pkg).read()
    if "command not found" in res:
        return False
    return True

def setFlag(data, flag):
    ins="Debug"
    if flag == "release":
        ins="Release"

    cmk=None
    with open('CMakeLists.txt','r',encoding='utf-8') as file:
        cmk = file.readlines()
    for i in range(0, len(cmk)):
        if "CMAKE_BUILD_TYPE" in cmk[i]:
            cmk[i]= "set(CMAKE_BUILD_TYPE "+ins+")\n"
    # print(cmk)
    with open('CMakeLists.txt', 'w', encoding='utf-8') as file:
        file.writelines(cmk)



def is_cpx_boot():
    res= os.popen("cat ~/.cpx.json").read()
    if "true" in res:
        return True
    return False

def prod(data):
    print()

def test(data):
    print()
def sanitize(data):
    print()
def benchmark(data):
    print()




if __name__ == "__main__":
   main()