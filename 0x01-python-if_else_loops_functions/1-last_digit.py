#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
last_num = num_str[-1]

if number >= 0:
    int_last_num = int(last_num)
    if int_last_num == 0:
        print("Last digit of " + str(number) + " is " + str(int_last_num) + " and is 0")
    elif int_last_num < 6 and int_last_num != 0:
        print("Last digit of " + str(number) + " is " + str(int_last_num) + " and is less than 6 and not 0")
    elif int_last_num > 5:
        print("Last digit of " + str(number) + " is " + str(int_last_num) + " and is greater than 5")
else:
    int_last_num = int(last_num) * -1
    if int_last_num == 0:
        print("Last digit of " + str(number) + " is " + str(int_last_num) + " and is 0")
    elif int_last_num < 6 and int_last_num != 0:
        print("Last digit of " + str(number) + " is " + str(int_last_num) + " and is less than 6 and not 0")
    elif int_last_num > 5:
        print("Last digit of " + str(number) + " is " + str(int_last_num) + " and is greater than 5")
