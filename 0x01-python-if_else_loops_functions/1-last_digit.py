#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
last_num = num_str[-1]
il_num = int(last_num)

if number >= 0:
    if il_num == 0:
        print(f"Last digit of {number} is {il_num} and is 0")
    elif il_num < 6 and il_num != 0:
        print(f"Last digit of {number} is {il_num} and is less than 6 and not 0")
    elif il_num > 5:
        print(f"Last digit of {number} is {il_num} and is greater than 5")
else:
    il_num *= -1
    if il_num == 0:
        print(f"Last digit of {number} is {il_num} and is 0")
    elif il_num < 6 and il_num != 0:
        print(f"Last digit of {number} is {il_num} and is less than 6 and not 0")
    elif il_num > 5:
        print(f"Last digit of {number} is {il_num} and is greater than 5")
