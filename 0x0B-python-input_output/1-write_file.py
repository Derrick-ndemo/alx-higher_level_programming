#!/usr/bin/python3
"""Defines a write func"""


def write_file(filename="", text=""):
    """Write a string to utf-8 text file

    Args:
        filename(str): The name of the file to write
        text(str): The text to be written to the file
    Returns:
        the numbers of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
