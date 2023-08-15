#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _row in matrix:
        for i in range(len(_row)):
            print("{:d}".format(_row[i]), end="")
            if i != len(_row) - 1:
                print(" ", end="")
        print()
