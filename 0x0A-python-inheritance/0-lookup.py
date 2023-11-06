def lookup(obj):
    """ this function return the list of the available attribute
        and methods of the object.
        args:
             obj: the value beign passed on
    """
    the_attribute_en_methods = dir(obj)
    return the_attribute_en_methods
