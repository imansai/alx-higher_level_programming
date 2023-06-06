#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)

if int(num_str) == 0:
    print("Last digit of " + str(number) + " is " + num_str[-1] + " and is 0")

elif int(num_str) > 5:
    print("Last digit of " + str(number) + " is " + num_str[-1] + " and is greater than 5")

elif int(num_str) < 6 and int(num_str) != 0:
    print("Last digit of " + str(number) + " is " + num_str[-1] + " and is 0"))
