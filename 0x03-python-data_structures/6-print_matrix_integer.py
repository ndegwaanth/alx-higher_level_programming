#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            separator = " " if col != row[-1] else ""
            print("{}{}".format(col, separator), end="")
        print()
