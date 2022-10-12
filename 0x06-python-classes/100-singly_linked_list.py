#!/usr/bin/python3
'''A module that defines two implementations of singly linked lists:
    1. Node
    2. SinglyLinkedList
'''


class Node:
    '''A class that defines a node for a singly linked list
    '''
    def __init__(self, data, next_node=None):
        '''Initializes the class

            args:
                data (int): the data to be inserted
                next_node (Node): pointer to the next node in the list

            Returns: None
        '''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''Returns the data property of the calss Node
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''Setter for setting the data attribute of the class
        '''
        if not isinstance(vaue, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        '''Returns the next_node of the Node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Setter for setting the data attributte of the calss

            args:
                value (Node): Node to be set
        '''
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    '''A class that defines a singly linked list
    '''
    def __init__(self):
        '''Initailizes the instance attributes
        '''
        self.__head = None

    def __str__(self):
        '''Prints all the elements of the singly linked list
        '''
        rtn = ''
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def sorted_insert(self, value):
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
