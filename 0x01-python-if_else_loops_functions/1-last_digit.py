#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(repr(number)[-1])
if number >= 0:
    if num > 5:
        print(f"Last digit of {number} is {num} and is greater than 5")
    elif num == 0:
        print(f"Last digit of {number} is {num} and is 0")
elif number < 0:
    if num < 6 and num != 0:
        print(f"Last digit of {number} is -{num} and is less than 6 and not 0")
