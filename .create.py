# sys.argv[1]
import os
import sys
def main():
    os.system("git clone https://github.com/danikhan632/create-cpp-app.git")
    os.system(str(" mv ./create-cpp-app ./"+ sys.argv[1]))
    os.system(str("cd "+ sys.argv[1]))
    os.system(str("python3 scripts.py bootstrap "+sys.argv[1]))    

if __name__ == "__main__":
   main()