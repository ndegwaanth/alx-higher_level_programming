#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    iterator = 0
    try:
        for m in range(x):
            if (iterator >= 0):
                break
            print(my_list[m], end="")
            iterator = iterator + 1
    except IndexError:
        pass
    finally:
        print()
    return iterator
