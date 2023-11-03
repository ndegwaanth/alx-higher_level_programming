#!/usr/bin/python3

""" display passed naame"""


def say_my_name(first_name, last_name=""):
    """say_my_name
        args:
            first_name(str)
            las_name(str)
    """

    if (isinstance(first_name, str) is False):
        raise TypeError("first_name must be a string")
    if (isinstance(last_name, str) is False):
        raise TypeError("las_name must be a string")
    if (len(last_name) == 0):
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
