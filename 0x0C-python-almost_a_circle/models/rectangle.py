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

        @property
        def x(self):
            """ this is the getter for the x_func"""
            return self.__x

        @x.setter
        def x(self, value):
            """ this is the setter for the x_func
                args:
                    @value: this is the value beign set to x
            """
            self.__x = value

        @property
        def y(self):
            """this is the getter method for the y_func"""
            return self.__y

        @y.setter
        def y(self, value):
            """ this is the setter for the y_func
                args:
                    @value: this is the value to be assigned to the y
            """
            self.__y = value

        def area(self):
            """
            Return area of the rectangle
            """
            area = self.width * self.height

            return area

        def display(self):
            """
            Prints size of rectangle using #
            """
            for _ in range(self.y):
                print()

            for _ in range(self.height):
                print(" " * self.x + "#" * self.width)

        def __str__(self):
            """
            Return the print() and str() representation of the Rectangle.
            """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

        def update(self, *args, **kwargs):
            """
            Assign arguments to attributes based on their positions.
            """
            if args:
                for count, arg in enumerate(args):
                    if count == 0:
                        self.id = arg
                    elif count == 1:
                        self.width = arg
                    elif count == 2:
                        self.height = arg
                    elif count == 3:
                        self.x = arg
                    elif count == 4:
                        self.y = arg
                    else:
                        break

            elif len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

                # than 5, and one of the attributes is at the end

        def to_dictionary(self):
            """
            Represents a dictionary representation of rectangle
            """
            rec_dict = {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
            }

            return rec_dict


if __name__ == "__main__":
    pass
