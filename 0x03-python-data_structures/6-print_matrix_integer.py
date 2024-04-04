#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nrow in matrix:
        for i in range(len(nrow)):
            print("{:d}".format(nrow[i]), end="")
            if i != len(nrow) - 1:
                print(" ", end="")
        print()
