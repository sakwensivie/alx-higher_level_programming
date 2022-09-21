#!/usr/bin/python3
def fizzbuzz():
    print(1, end='')
    for i in range(2, 101):
        if i % 5 == 0 and i % 3 == 0:
            print(' FizzBuzz', end='')
        elif i % 5 == 0:
            print(' Buzz', end='')
        elif i % 3 == 0:
            print(' Fizz', end='')
        else:
            print(' {:d}'.format(i), end='')
    print(' ')
