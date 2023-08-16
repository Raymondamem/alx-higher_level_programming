#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    _len = len(sys.argv) - 1
    if _len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    _list = list(ops.keys())
    if sys.argv[2] not in _list:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    _a = int(sys.argv[1])
    _b = int(sys.argv[3])
    print("{} {} {} = {}".format(_a, sys.argv[2], _b, ops[sys.argv[2]](_a, _b)))
