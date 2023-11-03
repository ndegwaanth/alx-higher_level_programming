#!/usr/bin/python3

"""text_indentation indent text with ne line """


def text_indentation(text):
    """ text indentation
        args:
            text(str)
    """

    if (isinstance(text, str) is False):
        raise TypeError("text must be string")
    for i in text:
        if (i == '.'):
            print('\n')
        if (i == '?'):
            print('\n')
        if (i == ':'):
            print('\n')
        print(i, end='')
