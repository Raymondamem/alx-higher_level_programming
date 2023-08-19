#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = []
    for _col in matrix:
        _rst = list(map(lambda x: x**2, _col))
        n_matrix.append(rst)
    return n_matrix
