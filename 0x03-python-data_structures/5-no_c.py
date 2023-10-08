#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = []
    for x in my_string:
        if x != 'c' and x != 'C':
            filtered_chars.append(x)

    result = "".join(filtered_chars)
    return result
