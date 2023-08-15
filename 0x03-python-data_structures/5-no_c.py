#!/usr/bin/python3

def no_c(my_string):
    _new_string = my_string.translate({ord(i): None for i in 'cC'})

    return _new_string
