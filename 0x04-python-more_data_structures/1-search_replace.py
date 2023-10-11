#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = []
    for value in my_list:
        if value == search:
            my_new_list.append(replace)
        else:
            my_new_list.append(value)
    return (my_new_list)
