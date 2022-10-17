#!/usr/bin/python3
'''
This module contains a funciton that adds two intergers
'''

def add_integer(a, b=98):
    '''
    This function adds and returns the value of two integers

    args:
        a (int): first number to be added
        b (int): secomd number to be added

    returns: the sum of the two numbers

    raises: 
        TypeError if any of the args are not either an integer of a float
    '''

    if type(a) not in (float, int):
        raise TypeError('a must be an integer')
    if type(b) not in (float, int):
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)

    return a + b
