#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        j = 0
        for arg in sys.argv:
            if j != 0:
                print('{}: {}'.format(j, arg))
            j += 1
