#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Create a new list with elements before idx
    new_list = my_list[:idx]
    
    # Extend the new list with elements after idx (skipping the idx element)
    new_list.extend(my_list[idx + 1:])
    
    return new_list
