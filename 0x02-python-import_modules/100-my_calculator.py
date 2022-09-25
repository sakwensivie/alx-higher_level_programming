#!/usr/bin/python3
if __name__ == '__main__':
    from sys import exit, argv
    from calculator_1 import add, sub, mul, div

    op_dict = {'+': add, '-': sub, '*': mul, '/': div}

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if argv[2] not in op_dict.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    answer = op_dict[argv[2]](int(argv[1]), int(argv[3]))

    print(answer)
