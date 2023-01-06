#!/usr/bin/python3
import calculator_1 as calc
import sys

if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {'+': calc.add, '-': calc.sub, '/': calc.div, '*': calc.mul}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
    
    
