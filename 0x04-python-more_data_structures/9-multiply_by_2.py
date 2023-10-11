#!/usr/bin/pyhton3
def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    my_list = list(my_dict.keys())
    for value in my_list:
        my_dict[value]*= 2
    return (my_dict)
