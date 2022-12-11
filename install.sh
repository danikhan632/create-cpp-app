
function create-cpp-app(){
    git clone https://github.com/danikhan632/create-cpp-app.git
    mv ./create-cpp-app ./$1
    cd $1
    python3 scripts.py bootstrap $1
}
alias cpx="python3 scripts.py"
#/bin.bash while IFS= read -r line do echo "$line" echo -e "$line
" >>~/zsh.txt done <"install.sh"
