#!/usr/bin/python3


def safe_print_integer(value):
    """safe print an integer

    Args:
        value (int): value to print

    Returns:
        false if failed true of succ
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
