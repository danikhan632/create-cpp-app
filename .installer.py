# sys.argv[1]
import os
import sys
def main():
    file1 = open("~/.zshrc", "a")  # append mode
    file1.write("\n")
    file1.write("alias create-cpp-app=\"python3 ~/.create.py\"\n")
    file1.write("alias cpx=\"python3 scripts.py\"\n")
    file2 = open("~/.bashrc", "a")  # append mode
    file2.write("\n")
    file2.write("alias create-cpp-app=\"python3 ~/.create.py\"\n")
    file2.write("alias cpx=\"python3 scripts.py\"\n")

    file2.close()
if __name__ == "__main__":
   main()
   
   
   