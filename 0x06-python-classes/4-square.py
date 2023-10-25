#!/usr/bin/python3
""" This is based on the the Square"""


class Square:
    """This class class is used to initialize the variable"""
    def __init__(self, size=0):
        """Constructor.
        Args:
            size(int): this is an int
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """function size.
        Args:
            size(int): This is the length of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ This function calculate the area and return it"""
        return (self.__size * self.__size)
