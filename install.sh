#!/bin/bash


    echo $1
    git clone https://github.com/danikhan632/create-cpp-app.git
    mv ./create-cpp-app ./$1
    cd $1
    echo python3 scripts.py bootstrap $1

# git clone https://github.com/danikhan632/create-cpp-app.git
# VAR2="${VAR1}World"
# mv ./create-cpp-app ./name








# function create-cpp-app(){
    # echo $1
    # git clone https://github.com/danikhan632/create-cpp-app.git
    # VAR2="${VAR1}World"
    # mv ./create-cpp-app ./$1
    cd $1
    echo python3 scripts.py bootstrap $1

# git clone https://github.com/danikhan632/create-cpp-app.git
# VAR2="${VAR1}World"
# mv ./create-cpp-app ./name