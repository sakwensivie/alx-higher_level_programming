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

        if (not isinstance(position, tuple)):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (not isinstance(position[0], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (not isinstance(position[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (len(position) != 2):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif ((position[0] < 0) or (position[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __le__(self, other):
        return self.__size <= other.__size

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
