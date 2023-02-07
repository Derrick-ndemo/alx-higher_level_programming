#!/usr/bin/python3


def read_file(filename=""):
    """Reading a text file"""
    with open(filename, mode='r', encode='utf-8') as f:
        print(f.read(), end='')
