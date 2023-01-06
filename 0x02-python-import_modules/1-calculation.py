#!/usr/bin/python3

# __name__ = "__main__" makes sure the code dosent run if imported as a module
if __name__ == "__main__":
    """ Simple calculator"""
    import calculator_1 as calc

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
