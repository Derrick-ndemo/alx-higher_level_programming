#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
    except (ValueError, TypeError):
        return False
    else:
        return True
