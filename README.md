#Create-cpp-app and cpx
install with the following for Mac/Linux, python3 must be installed
check which shell you have by running the command:

[![Watch the video](https://hackgtstoragebucket.s3.amazonaws.com/thumbnail.png)](https://youtu.be/sW8PO2zghhE)



````
which $SHELL
sudo apt-get install python3-distutils


````
For ZSH
````
echo "\nfunction create-cpp-app(){\r\n    git clone https://github.com/danikhan632/create-cpp-app.git\r\n    mv ./create-cpp-app ./\$1 \r\n    cd \$1\r\n    python3 scripts.py bootstrap \$1\r\n}\r\nalias cpx=\"python3 scripts.py\"" >> ~/.zshrc && sed -i -e "s/\r//g" ~/.zshrc && source ~/.zshrc 
````
For Bash
````
echo "\nfunction create-cpp-app(){\r\n    git clone https://github.com/danikhan632/create-cpp-app.git\r\n    mv ./create-cpp-app ./\$1 \r\n    cd \$1\r\n    python3 scripts.py bootstrap \$1\r\n}\r\nalias cpx=\"python3 scripts.py\"" >> ~/.bashrc && sed -i -e "s/\r//g" ~/.bashrc && source ~/.bashrc 
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
docker          use docker

edit conanfile.txt to add packages


to build the default app, run
````
cpx build
````



