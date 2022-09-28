#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx_low = len(matrix)
    mtrx_col = len(matrix[0])
    for n in range(mtrx_low):
        for m in range(mtrx_col):
            new_matrix = matrix[n][m] * matrix[n][m]
    return(new_matrix)
