#!/usr/bin/python3
# 2-print_alphabet.py

"""Prints the ASCII alphabet, in lowercase, not followed by a new line."""
for alphab in range(97, 123):
    print("{}".format(chr(alphab)), end="")
