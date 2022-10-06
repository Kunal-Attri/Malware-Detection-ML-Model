# main file for checking a file for probable Malware

import sys
from file_checker import checkFile


def main():
    if len(sys.argv) != 2:
        print("""
Invalid arguments given!
This program is to check if a given file is probable malware or not.

Usage: python3 main.py [file]
Try: python3 main.py malwares/Ransomware/Locky.exe
""")
        exit(1)
    filename = sys.argv[1]
    legitimate = checkFile(filename)
    if legitimate:
        print(f"File {sys.argv[1]} seems legitimate file!")
    else:
        print(f"File {sys.argv[1]} is probably a MALWARE!!!")


if __name__ == "__main__":
    main()
