#!/usr/bin/python3
"""Defines a write func"""


def write_file(filename="", text=""):
    """Returns the numbers of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
        
