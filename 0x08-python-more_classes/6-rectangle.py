#!/usr/bin/python3
'''
This module defines a class for a rectangle
'''


class Rectangle:
    '''
    The rectangle class
    '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''
        The init method

            args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        '''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Method that calculates the Rectangle area

        Returns:
            rectangle area


        """

        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the Rectangle perimeter

        Returns:
            rectangle perimeter


        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Method that returns the Rectangle #

        Returns:
            str of the rectangle

        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def print(self):
        '''Method that prints the Rectangel #

        Returns: None
        '''
        if self.width == 0 or self.height == 0:
            print()

        for i in range(self.height):
            for j in range(self.width):
                print('#', end='')
            print()

    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted


        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
