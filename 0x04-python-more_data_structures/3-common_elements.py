#!/usr/bin/python3
def common_elements(set_1, set_2):
    comparison = set(set_1)
    comparison_1 = set(set_2)
    intersect = comparison.intersection(comparison_1)
    return intersect
