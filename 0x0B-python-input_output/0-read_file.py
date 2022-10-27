#!/usr/bin/python3
'''
This module contains a funcition that reads the contents of a file
'''


def read_file(filename=''):
    '''This function reads the contents of a file
    and prints it to stdout.

    Args:
        filename (string): the filename of the file to be read
    '''
    if type(filename) is not string:
        try:
            filename = str(filename)
        except TypeError:
            print('filename ust be an integer')
    with open(filename, 'r', encoding='utf-8') as file_lines:
        read_line = file_lines.read()
        print(read_line, end='')
