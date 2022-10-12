#!/usr/bin/python3
'''A module that defines a square class
'''


class Square:
    '''A class that defines a square
    '''
    def __init__(self, size):
        ''' Initialize some instance attributes related to the square
            Args:
                param1 (int): size of the square
        '''
        self.__size = int(size)
