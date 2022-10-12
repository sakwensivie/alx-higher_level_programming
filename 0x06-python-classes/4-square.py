#!/usr/bin/python3
'''A module that defines a class for square
'''


class Square:
    '''Class that defines a square
    '''
    def __init__(self, size=0):
        '''Initializes the class with certain paramemters
            Args:
                size (int): size of the square
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Returns the area of the square
        '''
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)
