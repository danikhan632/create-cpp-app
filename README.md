#Create-cpp-app and cpx
install with the following for Mac/Linux, python3 must be installed
check which shell you have by running the command:

[![Watch the video](https://hackgtstoragebucket.s3.amazonaws.com/thumbnail.png)](https://youtu.be/sW8PO2zghhE)



````
sudo apt-get install python3-distutils
sudo apt-get install neofetch

optional packages for a better experience



To install 
````
curl https://raw.githubusercontent.com/danikhan632/create-cpp-app/main/.installer.py > ~/.installer.py && python3 ~/.installer.py
````

create a new project: The name "my_new_proj" is whatever name you like
````
create-cpp-app my_new_proj

````
once done bootstrapping, type 
````
cpx
````
and the following should appear


Usage:
python3 scripts.py ARG

dev             build and run project
build           build: python3 scripts.py build debug or python3 scripts.py build release
run             run project
debug           run gdb on project
rename ARG2     rename project, ARG2 is new name no spaces
santize         use build using address-sanitzer
test            builds and runs GTests in tests dir
benchmark       runs benchmark on release version of project
prod            builds to release, sanitizes, tests and benchmarks
docker build    use Docker to build project

edit conanfile.txt to add packages


to build the default app, run
````
cpx build
````



