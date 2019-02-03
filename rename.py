#!/usr/local/bin/python
import os
import argparse

# set up argument parser
parser = argparse.ArgumentParser(description="Rename a file by replacing specific characters, e.g. underscores with dashes")
parser.add_argument("file", help="File you want to rename")
parser.add_argument("needle", help="Character you want replaced")
parser.add_argument("replacement", help="The replacement character")
args = parser.parse_args()

# new name by simply replacing each given input
new_name = args.file.replace(args.needle, args.replacement)

# use os.rename (comes with python) to rename
os.rename(args.file, new_name)
