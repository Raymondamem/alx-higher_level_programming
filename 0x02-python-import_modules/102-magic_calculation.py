#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        _c = add(a, b)
        for i in range(4, 6):
            _c = add(_c, i)
        return (_c)
    else:
        return(sub(a, b))
