#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    max = my_list[0]
    for digit in range(len(my_list)):
        if my_list[digit] > max:
            max = my_list[digit]
    return (max)
