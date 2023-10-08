#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements; use 0 for missing values
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Sum the first elements of each tuple and the second elements
    result = (a[0] + b[0], a[1] + b[1])
    return result
