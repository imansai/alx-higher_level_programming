#!/usr/bin/python3
def read_file(filename=""):
    """
    Read the contents of the given text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf8') as file:
        content = file.read()
        print(content, end='')
