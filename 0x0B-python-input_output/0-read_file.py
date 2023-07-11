#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Write the given text to a file with the specified filename.

    Args:
        filename (str): The name of the file to write to.
        text (str): The content to write to the file.

    Raises:
        IOError: If there is an error while writing to the file.
    """
	with open(filename, 'w', encoding='utf8') as file:
	file.write(text)
