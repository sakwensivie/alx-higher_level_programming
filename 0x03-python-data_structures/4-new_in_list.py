#!/usr/bin/python3
if __name__ == '__main__':
    def new_in_list(my_list, idx, element):
        if idx < 0:
            return (None)
        if idx > len(my_list):
            return (my_list)
        new_list = my_list[:]
        new_list[idx] = element
        return (new_list)
