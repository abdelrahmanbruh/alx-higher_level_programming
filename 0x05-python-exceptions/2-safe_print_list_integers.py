#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """safely print list of the integers

    Args:
        my_list (list): my_list to print the elements
        x (int): the number of elements
    Returns:
        no of elements
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
