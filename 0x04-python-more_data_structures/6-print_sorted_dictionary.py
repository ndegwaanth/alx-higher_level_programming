#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items = sorted(a_dictionary.keys())
    for key in items:
        print(key, ":", a_dictionary[key])
