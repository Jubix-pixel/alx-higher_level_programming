#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for x in range(len(matrix)):
        new_matrix = matrix.append(x ** 2)
    return(new_matrix)
