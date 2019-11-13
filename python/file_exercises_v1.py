# Reference: https://www.w3resource.com/python-exercises/file/

# Write a menu driven program to do following tasks:
# 1. read first n lines of a file
# 2. read even lines and write into another file
# 3. find and display the longest word
# 4. read random line from a file and calculate its length
# 5. display the no of lines, no of empty lines,
#    and no of characters in the file

# given file assets/source.txt

import random
import os

MENUS = {
    "1": "Read first n lines",
    "2": "Read even lines and write into another file",
    "3": "Find the longest word",
    "4": "Read random line from a file and calculate its length",
    "5": "No of lines, empty lines and total characters"
}


def display_menu():
    print("******** MENU ********")
    for menu_index in range(len(MENUS)):
        print("{}. {}".format(menu_index+1, MENUS[str(menu_index+1)]))


def display_lines(path):
    n = int(input("Enter value of 'n': "))
    file = open(path, "r")
    while n != 0:
        print(file.readline().rstrip("\n"))
        n -= 1

    file.close()


def read_even_lines_and_write(path):
    dest_path = "assets/dest.txt"
    with open(dest_path, "w") as f:
        file = open(path, "r")
        for i, line in enumerate(file):
            if (i+1) % 2 == 0:
                print(line.rstrip(), file=f)

    print("\n\nContent copied in new file:")
    f = open(dest_path, "r")
    for line in f:
        print(line.rstrip())


def longest_word(path):
    longest_word = ""
    f = open(path, "r")
    for line in f:
        max_word = max(line.split(' '))
        if len(max_word) > len(longest_word):
            longest_word = max_word

    print("Longest word is: " + longest_word)


def random_line_and_length(path):
    f = open(path, "r")
    lines = [line for line in f.read().splitlines() if line != '']
    random_line = random.choice(lines)
    print("Random line is {}.\nLength is {}.".format(
        random_line, len(random_line)))


def display_stats(path):
    statinfo = os.stat(path)
    f = open(path, "r")
    lines = f.read().splitlines()
    empty_lines = lines.count('')
    print("No of characters: {}\nNo of lines: {}\nNo of empty lines: {}".format(
        statinfo.st_size, len(lines), empty_lines))
    print("")


def main():
    # need to give absolute path if file source directory is at different path
    filepath = "assets/source.txt"
    display_menu()
    print()
    selected_choice = input("Select your choice (1/2/3/4/5): ")
    if selected_choice == "1":
        display_lines(filepath)
    elif selected_choice == "2":
        read_even_lines_and_write(filepath)
    elif selected_choice == "3":
        longest_word(filepath)
    elif selected_choice == "4":
        random_line_and_length(filepath)
    elif selected_choice == "5":
        display_stats(filepath)
    else:
        print("Invalid choice. Select from 1, 2, 3, 4 or 5.")


if __name__ == '__main__':
    main()
