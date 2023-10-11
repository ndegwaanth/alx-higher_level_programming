#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    comparison = set(set_1)
    comparison_1 = set(set_2)
    intersect = comparison.union(comparison_1)
    return intersect
