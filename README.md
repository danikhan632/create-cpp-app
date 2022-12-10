cmake -S . ./output/
make


Usage:
python3 scripts.py ARG

dev             to build and run project
build           to build: python3 scripts.py build debug or python3 scripts.py build release
run             to run project
debug             to debug project
rename ARG2     to rename project, ARG2 is new name no spaces

edit conanfile.txt to add packages



````

echo "\nfunction create-cpp-app(){\r\n    git clone https://github.com/danikhan632/create-cpp-app.git\r\n    mv ./create-cpp-app ./\$1 \r\n    cd \$1\r\n    python3 scripts.py bootstrap \$1\r\n}\r\nalias cpx=\"python3 scripts.py\"" >> ~/.zshrc && sed -i -e "s/\r//g" ~/.zshrc && source ~/.zshrc 

````