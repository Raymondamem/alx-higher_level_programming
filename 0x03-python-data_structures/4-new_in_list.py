#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _copy = my_list.copy()
    _len = len(my_list) - 1

    if idx < 0 or idx > _len:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
