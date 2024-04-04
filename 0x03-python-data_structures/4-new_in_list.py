#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    _copy = my_list.copy()
    _ln = len(my_list) - 1

    if idx < 0 or idx > _ln:
        return my_list.copy()
    else:
        _copy[idx] = element
        return _copy
