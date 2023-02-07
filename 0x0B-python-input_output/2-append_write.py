#!/usr/bin/python3
"""Appending to a file"""


def append_write(filename="", text=""):
    """Appends a string to the end of the file

    Args:
        filename(str): The name of the file
        text(str): The text to be appended
    Returns:
        The number of characters added
    """

    with open(filename, "a", encoded="utf-8") as f:
        return f.write(text)
