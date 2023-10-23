#!/usr/bin/python3
def safe_print_integer(value):
    try:
        my_value = "{:d}".format(value)
        print(my_value)
        print()
        return True
    except (ValueError, TypeError):
        return False
