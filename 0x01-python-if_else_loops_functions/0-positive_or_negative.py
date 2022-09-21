#!/usr/bin/python3
import random as rand
x = rand.randint(-10, 10)
if x > 0:
    print('{:d} is positive'.format(x))
elif x == 0:
    print('{:d} is zero'.format(x))
else:
    print('{:d} is negetive'.format(x))
