#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("Addition:", add_result)
    print("Subtraction:", sub_result)
    print("Multiplication:", mul_result)
    print("Division:", div_result)