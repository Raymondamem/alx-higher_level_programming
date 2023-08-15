#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _a_row in matrix:
        for _a_col in _a_row:
            print("{:d}".format(_a_col), end=" " if _a_col != _a_row[-1] else "")
        print()
