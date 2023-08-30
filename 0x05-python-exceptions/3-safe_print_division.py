#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result1 = a / b
    except ZeroDivisionError:
        result1 = None
    finally:
        print("Inside result: {}".format(result))
        return result1
