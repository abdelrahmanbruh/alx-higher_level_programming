#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print the list but it's safe

    Args:
        my_list (list): my list to print it
        x (int): the number of elements
    Returns:
        number of elemnts printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
