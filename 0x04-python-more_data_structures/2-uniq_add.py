#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    uniq_list = set(my_list)
    for i in uniq_list:
        num += i
    return (num)
