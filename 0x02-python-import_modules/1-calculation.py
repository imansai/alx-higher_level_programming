#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = int(a / b)

    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_sub))
    print("{} * {} = {}".format(a, b, result_mul))
    print("{} / {} = {}".format(a, b, result_div))
