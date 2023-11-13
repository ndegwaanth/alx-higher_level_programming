#!/usr/bin/python3
""" this include the python script"""


class Base:
    """ this is the first class Base"""
    __nb_object = 0

    def __init__(self, id=None):
        """ this is the initializer of the attributes.
            args:
                 @id: this the id
        """
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
