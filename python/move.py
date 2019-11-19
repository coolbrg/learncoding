# Write a program to perform moving the content of one file into another.
# Also, add feature of overwriting the destination file by passing arguments
# Expected Output
# $ py move.py /a/b/c/file1.txt /a/p/q/r/file1.txt --overwrite
# It should move the file present at /a/b/c/file1.txt into
#    /a/p/q/r/file1.txt and overwrite the existing file.

# Prerequisites:
# - Command line arguments
# - File operations
# - Keyword argument using '*'

import sys
import os


def move(source, destination, overwrite=False):
    print("Moving '{}' to '{}' ...".format(source, destination))

    if overwrite & os.path.isfile(destination):
        print("Deleting", destination, "...")

    if not os.path.isfile(source):
        print("Invalid source file.")
        exit()

    if not os.path.isfile(destination):
        print("Invalid destination file.")
        exit()

    with open(source, "r") as src_f:
        with open(destination, "w") as dest_f:
            for line in src_f:
                dest_f.write(line)

    print("File moved successfully!")


def main():
    if len(sys.argv) == 1:
        print("Enter the source and destination path.")
    elif len(sys.argv) == 2:
        print("Enter the destination path.")
    elif len(sys.argv) == 3:
        move(sys.argv[1], sys.argv[2])
    elif '--overwrite' in sys.argv:
        move(sys.argv[1], sys.argv[2], overwrite=True)
    else:
        print("Usage:")
        print("$ python move.py <source> <destination> [--overwrite]")


if __name__ == "__main__":
    main()
