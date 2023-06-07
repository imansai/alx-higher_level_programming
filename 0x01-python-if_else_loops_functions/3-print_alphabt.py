#!/usr/bin/python3

for ascii_letter in range(ord('a'), ord('z') + 1):
    if chr(ascii_letter) not in ['q', 'e']:
        print("{}".format(chr(ascii_letter)), end="")
