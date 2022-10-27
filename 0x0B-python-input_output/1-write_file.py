#!/usr/bin/python3
'''This module contains a function that writes text to a file
'''


def write_file(filename='', text=''):
    '''Writes a text to a file

    Args:
        filename (str): name of the file to be writtern on

        twxt (str): text to be written
    '''

    with open(filename, 'w', encoding='utf-8') as read_file:
        return read_file.write(text)
