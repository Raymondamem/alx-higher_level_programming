#!/usr/bin/python3
def magic_calculation(a, b):
    rlt = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            rlt += a ** b / x
        except Exception:
            rlt = b + a
            break
    return rlt
