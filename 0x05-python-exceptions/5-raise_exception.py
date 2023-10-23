#!/usr/bin/python3
def raise_exception():
    raise TypeError("This is a type exception")

# Example usage:
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)
