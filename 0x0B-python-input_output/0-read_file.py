#!/usr/bin/python3
"""Defines a function that reads a file and prints."""


def read_file(filename=""):
   """Prints UTF8 text content to stdout."""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end='')
