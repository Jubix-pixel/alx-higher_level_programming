#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    f_op =  sys.argv[1]
    if f_op != "+" and f_op != "-" and f_op != "*" and f_op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sys.argv[0] = int(a)
    sys.argv[2] = int(b)
    from calculator_1 import add, sub, mul, div
    if n == 3:
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} - {} = {}".format(a, b, sub(a, b)))
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print("{} / {} = {}".format(a, b, div(a, b)))
