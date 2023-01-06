#!/usr/bin/python3

""" Program that prints the number of and the list of its arguments"""
if __name__ == "__main__":
    # Importing argv
    from sys import argv

    length = len(argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {}".format(i + 1, argv[i + 1]))
