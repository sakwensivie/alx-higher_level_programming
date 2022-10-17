#!/usr/bin/python3
'''
This module defines a class for a rectangle
'''


class Rectangle:
    '''
    The rectangle class
    '''

    def __init__(self, width = 0, height = 0):
        '''
        The init method

            args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''The width property getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Method that the sets the width of the rectangle

        args:
            value (int): the value to be set
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must >= 0')
        self.__width = value

    @property
    def height(self):
        '''Property getter to return the the height of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Property setter to set the height of the rectangle

        args:
            value (int): the value to be set as the height
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must >= 0')
        self.__height = value
