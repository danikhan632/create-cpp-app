#!/bin/bash

#add this to .zshrc
function create-cpp-app(){
    git clone https://github.com/danikhan632/create-cpp-app.git
    mv ./create-cpp-app ./$1 
    cd $1
    python3 scripts.py bootstrap $1
}
alias cpx="python3 scripts.py"
CPX_BOOT="yes"

echo "function create-cpp-app(){\r\n    git clone https://github.com/danikhan632/create-cpp-app.git\r\n    mv ./create-cpp-app ./\$1 \r\n    cd \$1\r\n    echo python3 scripts.py bootstrap \$1\r\n}" >> ~/.zshrc
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/danikhan632/create-cpp-app/main/install.sh)"