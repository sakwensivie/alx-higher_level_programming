#!/usr/bin/python3
if __name__ == '__main__':
    import sys as s
    i = len(s.argv)
    sum = 0
    if i > 1:
        for arg in s.argv:
            if arg != s.argv[0]:
                sum += int(arg)

    print('{}'.format(sum))
