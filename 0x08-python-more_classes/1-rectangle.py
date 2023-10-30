#!/usr/bin/python3
""" involves Rectangle implementation"""


class Rectangle:
    """this is the class that is used to enclose the code files"""
    def __init__(self, width=0, height=0):
        """ this is a constructor
            args:
                width (int): this is the width of the rectangle
                height (int): this is the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ this method return the private width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ this method is use to set the width to specific value.
            args:
                value (int): this the value beign set to widt.
        """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ this code is used to used to return height"""
        return self.__width

    @height.setter
    def height(self, value):
        """ this method is usd to set the value of the height to a value
            args:
                value (int): this is the value beign set to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
