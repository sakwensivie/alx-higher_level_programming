#!/usr/bin/python3
'''A module that defines a class for square
'''


class Square:
    '''Class that defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
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

        if not isinstance(position[0], int)  or not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif ((position[0] < 0) or (position[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        '''Returns the area of the square
        '''
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to returns the size value

            Returns: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object

            args:
                value (int): size of the square to be set

            Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    @property
    def position(self):
        '''A property method to return the position of a square class
        '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' A setter method to set the value of the position

            args:
                value (tuple): position

            returns:
                None
        '''

        if (not isinstance(value[0], int) or not isinstance(value[1])):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif ((value[0] < 0) or (value[1] < 0)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        '''A method that prints the square
        '''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
