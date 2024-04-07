#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_new_list = []
    my_sum = 0
    for my_num in my_list:
        if my_num not in my_new_list:
            my_sum += my_num
            my_new_list.append(my_num)
    return my_sum
