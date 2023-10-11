#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    sum = 0
    for value in my_list:
        if value not in my_set:
            sum += value
            my_set.add(value)
    return sum
