#!/usr/bin/pyhton3
def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg("This a custom exception message")
except NameError as e:
    print("caught an exception"+ e)
