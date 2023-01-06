#!/usr/bin/python3

if __name__ == "__main__":
    # infinite addition of numbers in the terminal

    from sys import argv

    pos = len(argv) - 1
    add = 0

    for i in range(pos):
        add = add + int(argv[i + 1])
    print("{:d}".format(add))
