#!/usr/bin/python3
def read_file(filename=""):
    """Defines a function that reads a file and prints."""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end='')
