#!/usr/bin/python3
def safe_print_integer(value):
    condition = True
    try:
        print('{:d}'.format(value))
    except ValueError:
        condition = False
    
    return condition
