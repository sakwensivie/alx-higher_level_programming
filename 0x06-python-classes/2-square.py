#!/usr/bin/python3
class Square:
    '''
        Class that defines a square
    '''
    def __init__(self, size=0)
        '''
            Initializes the class with certain paramemters
            
            Args:
                size (int): size of the square
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._size = size
