#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        _ln = len(my_list)
        for i in range(_ln):
            print("{:d}".format(my_list[i]))
