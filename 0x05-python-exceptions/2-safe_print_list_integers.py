#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    iterator = 0
    try:
        for element in range(x):
            if iterator >= x:
                break
            try:
                my_value = "{:d}".format(my_list[element])
                print(my_value, end="")
                iterator = iterator + 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    finally:
        print()
