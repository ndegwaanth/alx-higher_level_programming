#!/usr/bin/python3
""" this module  implement the Rectanlge inheritance"""
from models.base import*


class Rectangle(Base):
    """ this class implement the inheritance from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ this initialize the variables above"""
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ this is the width getter"""
            return self.__width

        @width.setter
        def width(self, value):
            """ this respresent the width setter
                args:
                    @value: the value to assign to the new width
            """
            self.__width = value
            return self.__width

        @property
        def height(self):
            """this is the height getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """this is the setter for the height
               args:
                   @value: the value to assign to the new height
            """
            self.__height = height
            return self.__height

        @property
        def x_func(self):
            """ this is the getter for the x_func"""
            return self.__x

        @x.setter
        def x_func(self, value):
            """ this is the setter for the x_func
                args:
                    @value: this is the value beign set to x
            """
            self.__x = value
            return self.__x

        @property
        def y_func(self):
            """this is the getter method for the y_func"""
            return selff.__y

        @y.setter
        def y_func(self, value):
            """ this is the setter for the y_func
                args:
                    @value: this is the value to be assigned to the y
            """
            self.__y = value
            return self.__y
