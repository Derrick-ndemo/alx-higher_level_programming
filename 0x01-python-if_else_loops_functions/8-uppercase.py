#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) is not range(64, 92):
            i = chr(ord(i) - 27)
        print("{:s}".format(i), end="") 
