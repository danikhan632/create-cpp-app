
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


    cof = open('.config/data.json')
    data = json.loads(cof.read())
    name=data["proj_name"]
    first=data["bootstraped"]
    print(data["bootstraped"])
    if first == "false" or first == "False" or first == False :
        print("must bootstrap")
        bootstrap(data)
    #print(name)

    if len(sys.argv) == 1:
        print("Usage:\r\npython3 scripts.py ARG\r\n\r\ndev\t\t to build and run project\r\nbuild\t\t to build project\r\nrun\t\t to run project\r\nrename ARG2\t to rename project, ARG2 is new name no spaces\r\nclean\t\t to clean cmake & conan backups, moved to .config/cold_store")
    else:
        if str(sys.argv[1]) == "build":
           build(data)
        elif str(sys.argv[1]) == "run":
            run(data)
        elif str(sys.argv[1]) == "bootstrap":
            bootstrap(data, sys.argv[2])
        elif str(sys.argv[1]) == "dev":
            build(data)
            run(data)
        elif str(sys.argv[1]) == "clean":
            clean(data)
        elif str(sys.argv[1]) == "rename":
            change_proj_name(data,sys.argv[2])
        else:
            print("invalid arguments")





def run(data):
    os.system("./output/"+data["proj_name"])


def build(data):
    clean(data)
    # os.system("mv .config/cold_store/CMakeCache.txt ./CMakeCache.txt")
    # os.system("mv .config/cold_store/cmake_install.cmake ./cmake_install.cmake ")
    update_execute(data)
    os.system("conan install . --install-folder lib --output-folder ./lib/packages")
    os.system("cmake .")
    os.system("make")
    # os.system("mv ./CMakeCache.txt .config/cold_store/CMakeCache.txt")
    # os.system("mv ./cmake_install.cmake .config/cold_store/cmake_install.cmake")

def clean(data):
    # os.system("mv ./CMakeCache.txt .config/cold_store/CMakeCache.txt")
    # os.system("mv ./cmake_install.cmake .config/cold_store/cmake_install.cmake")
    os.system("mv ./lib/conaninfo.txt .config/cold_store/conaninfo.txt")
    os.system("mv ./lib/conanbuildinfo.txt .config/cold_store/conanbuildinfo.txt")
    os.system("mv ./lib/conanbuildinfo.cmake .config/cold_store/conanbuildinfo.cmake")
    os.system("mv ./lib/conan.lock .config/cold_store/conan.lock")
    


    # os.system("mv ./ .config/cold_store/")
    



def change_proj_name(data, new_name):
    if new_name == "" or " " in new_name:
        return
    old_name=""
    old_name=data["proj_name"]
    print("dec ",old_name, new_name)
    data["proj_name"] = new_name

    repl =(open('CMakeLists.txt').read())
    print(repl)
    repl=repl.replace(old_name, new_name)
    print(repl)
    file = open('CMakeLists.txt', 'w', encoding='utf-8')
    file.write(repl)
    json.dump(data, open(".config/data.json", "w"), indent = 4)

def update_execute(data):
    cmk=None
    with open('CMakeLists.txt','r',encoding='utf-8') as file:
        cmk = file.readlines()
    for i in range(0, len(cmk)):
        if "add_executable" in cmk[i]:
            cmk[i]= "add_executable(" + data["proj_name"] + get_src(data) +")\n"
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



def bootstrap(data, new_name):
    if os.name != "posix":
        print("Only mac and linux are supported, please use WSL")
        return
    vscode=str(input("install vscode packages? y or n:  "))
    cont=False
    while not cont:
        match vscode:
            case "y":
                os.system("code --install-extension ms-vscode.cpptools-extension-pack")
                os.system("code --install-extension twxs.cmake")
                os.system("code --install-extension FireBlackHat.conan-tools")
                os.system("code --install-extension disroop.conan")
                os.system("code --install-extension DamianKoper.gdb-debug")
                os.system("code --install-extension matepek.vscode-catch2-test-adapter")
                os.system("code --install-extension ms-vscode.cmake-tools")
                os.system("code --install-extension ms-vscode.makefile-tools")
                os.system("code --install-extension hbenl.vscode-test-explorer")
                cont=True
                data["bootstraped"]=True
                json.dump(data, open(".config/data.json", "w"), indent = 4)
            case "n":
                cont=True
            case default:
                print("please make a valid choice")
                vscode=str(input("install vscode packages? y or n:  "))
    

    if not isInstalled("brew --version"):
        install_brew=input("install brew? y or n:  ")
        cont=False
        while not cont:
            match install_brew:
                case "y":
                    os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
                    if not isInstalled("gcc"):
                        os.system("brew install gcc")
                    data["brewed"]=True
                    json.dump(data, open(".config/data.json", "w"), indent = 4)
                    cont=True
                case "n":
                    cont=True
                case default:
                    print("please make a valid choice")
                    install_brew=str(input("install brew? y or n"))
    else:
        data["brewed"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)

    if not isInstalled("pip --version"):
        os.system("wget https://bootstrap.pypa.io/get-pip.py")
        os.system("python3 ./get-pip.py")
        os.system("./get-pip.py")
        data["piped"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
    else:
        data["piped"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)


    if "Darwin" in platform.system():
        if not isInstalled("gcc --version"):
            os.system("xcode-select --install")
        data["os"]="mac"
        data["gcced"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)

    elif "Linux" in platform.system() or "linux" in platform.system():
        if isInstalled("apt"):
            data["os"]="deb"
            if not isInstalled("gcc --version"):
                os.system("sudo apt install -y build-essential")
            
        elif isInstalled("pacman"):
            data["os"]="arch"
            if not isInstalled("gcc --version"):
                os.system("sudo pacman -Sy base-devel")
        data["gcced"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)

    if not isInstalled("conan --version"):
        os.system("pip install conan")
        data["conaned"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
    else:
        data["conaned"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)

    if not isInstalled("cmake --version"):
        os.system("pip install cmake")
        data["cmaked"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
    else:
        data["cmaked"]=True
        json.dump(data, open(".config/data.json", "w"), indent = 4)
    
    change_proj_name(data, new_name)
    data["bootstraped"]=True
    json.dump(data, open(".config/data.json", "w"), indent = 4)
    
    

    


def isInstalled(pkg):
    res= os.popen(pkg).read()
    if "command not found" in res:
        return False
    return True








if __name__ == "__main__":
   main()