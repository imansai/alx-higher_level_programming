#!/usr/bin/python3

"""Print all possible combinations of two digits in ascending order."""
for i in range(10):
    for j in range(10):
        if (i == 8 and j == 9):
            print(89)
            continue
        if (i < j):
            print("{}{}, ".format(i, j), end='')
