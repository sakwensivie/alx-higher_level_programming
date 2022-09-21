#!/usr/bin/python3
import random
x = random.randint(-10, 10)
if x > 0:
    print('{:d} is positive'.format(x))
elif x == 0:
    print('{:d} is zero'.format(x))
else:
    print('{:d} is negetive'.format(x))
