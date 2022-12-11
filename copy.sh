#/bin.bash
while IFS= read -r line
do
echo "$line"
echo -e "$line\n" >>~/zsh.txt

done <"install.sh"