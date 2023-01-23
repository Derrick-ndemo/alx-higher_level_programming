#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
        print("Inside result: {}".format(res))
    except (ZeroDivisionError, ValueError, TypeError):
        print("Inside result: None")
        return None
