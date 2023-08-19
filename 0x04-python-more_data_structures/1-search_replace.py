#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_new_list = []
    for el in my_list:
        if el == search:
            my_new_list.append(replace)
        else:
            my_new_list.append(el)
    return my_new_list
