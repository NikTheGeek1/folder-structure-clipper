# Folder Structure to Clipboard Tool

This Python script allows you to generate a formatted folder structure of a given directory, taking into account a list of files and directories to ignore (similar to .gitignore). The resulting folder structure will be copied to your clipboard, ready for pasting into any text editor or document.

## Dependencies

This script requires the `pyperclip` package to interact with the clipboard. You can install it using:


## Usage

To use the script, run it in the terminal with the following flags:

- `-d`, `--directory`: (Optional) Path to the directory you want to generate the folder structure for. Defaults to the current directory.
- `-i`, `--ignore`: (Optional) Path to the file containing a list of files/directories to ignore. Defaults to no ignore file.

Example:

python folder_structure.py -d ./example -i ./ignorefile.txt


This will generate a formatted folder structure for the specified directory and copy it to your clipboard.

## Ignore File Format

The ignore file should contain one file or directory pattern per line. The script will ignore any files or directories that contain a pattern specified in the ignore file. For example:

.git
pycache
*.pyc


This ignore file will cause the script to ignore any `.git` directories, `__pycache__` directories, and any files ending with `.pyc`.