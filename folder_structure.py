import os
import sys
import argparse
from pathlib import Path
import pyperclip

def parse_ignore_list(ignore_file):
    with open(ignore_file, "r") as f:
        ignore_list = [line.strip() for line in f.readlines()]
    return ignore_list

def get_formatted_structure(path, ignore_list, level=0):
    structure = ""
    for item in sorted(os.listdir(path)):
        ignore = False
        for pattern in ignore_list:
            if pattern in item:
                ignore = True
                break
        if ignore:
            continue

        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            structure += "  " * level + f"{item}/\n"
            structure += get_formatted_structure(item_path, ignore_list, level + 1)
        else:
            structure += "  " * level + f"{item}\n"
    return structure

def main():
    parser = argparse.ArgumentParser(description="Generate a folder structure and copy it to the clipboard.")
    parser.add_argument("-d", "--directory", help="Path to the directory.", default=".")
    parser.add_argument("-i", "--ignore", help="Path to the file containing a list of files/directories to ignore.", default=None)

    args = parser.parse_args()

    if args.ignore:
        ignore_list = parse_ignore_list(args.ignore)
    else:
        ignore_list = []

    directory = os.path.abspath(args.directory)
    folder_structure = get_formatted_structure(directory, ignore_list)
    pyperclip.copy(folder_structure)
    print("Folder structure copied to clipboard.")
    
if __name__ == "__main__":
    main()
