#!/usr/bin/python3


def raise_exception_msg(message=""):
    """Raise a NameError exception with a specified message.

    Args:
        message (str): The message to include in the exception (default: "").

    Raises:
        NameError: Always raises a NameError exception with the specified message.
    """
    raise NameError(message)
