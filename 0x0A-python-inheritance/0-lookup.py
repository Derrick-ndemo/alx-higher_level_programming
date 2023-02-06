#!/usr/bin/python3
"""Defines an object attributes lookup functions."""


def lookup(obj):
    """Return a list of an object's availlable attributes."""
    return (dir(obj))
