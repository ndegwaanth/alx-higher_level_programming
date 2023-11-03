#!/usr/bin/python3
"""this is the implementation of the addition"""

def add_integer(a, b=98):
    """this funtion  implement the addition of 2 integers.
       args:
            a(int): the integer beign passed on.
            b(int): the second integer beign passed on.
       raises:
              TypeError: a must be an integer
              TypeError: b must be an interger
    """
    if ((not isinstance(a, int) and not isinstance(b, float))):
        raise TypeError("a must be an integer")
    if ((not isintance(b, float)) and (not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return (a + b)
