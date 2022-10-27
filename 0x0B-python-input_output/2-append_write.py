#!/usr/bin/python3
'''This module contains a function to append to a file
'''


def append_write(filename='', text=''):
    '''Appends to a file

    Args:
        filename (str): full path to the file to be edited

        text (str): text to be appended at the end of the file.

    '''

    with open(filename, 'a', enconding='utf-8') as f:
        return f.write(text)
