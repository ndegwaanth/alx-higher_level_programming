#1/usr/bin/python3
def square_matrix_simple(matrix=[]):
    second_matrix = []
    for row_1 in matrix:
        row_1_outcome = []
        for value in row_1:
            row_1_outcome.append(value ** 2)
        second_matrix.append(row_1_outcome)
    return(second_matrix)
