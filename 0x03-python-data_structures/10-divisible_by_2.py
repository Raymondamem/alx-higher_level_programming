#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    _new_list = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            _new_list.append(True)
        else:
            _new_list.append(False)
    return _new_list
