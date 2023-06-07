#!/usr/bin/python3
for number in range(100):
    print(format(number, '02d'), end="")
    if number < 99:
        print(", ", end="")
    else:
        print()
