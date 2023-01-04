#!/usr/bin/python3
def fizzbuzz():
    for var in range(1, 101):
        if var % 3 == 0 and var % 5 == 0:
            print("FizzBuzz", end=' ')
        elif var % 3 == 0:
            print("Fizz", end=' ')
        elif var % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(f"{var:d}", end=' ')
