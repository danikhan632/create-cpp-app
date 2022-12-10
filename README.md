cmake -S . ./output/
make


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

edit conanfile.txt to add packages



````

echo "\nfunction create-cpp-app(){\r\n    git clone https://github.com/danikhan632/create-cpp-app.git\r\n    mv ./create-cpp-app ./\$1 \r\n    cd \$1\r\n    python3 scripts.py bootstrap \$1\r\n}\r\nalias cpx=\"python3 scripts.py\"" >> ~/.zshrc && sed -i -e "s/\r//g" ~/.zshrc && source ~/.zshrc 

````