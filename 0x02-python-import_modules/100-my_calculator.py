#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    c_op = sys.argv[2]
    if c_op != "+" and c_op != "-" and c_op != "*" and c_op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if c_op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if c_op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if c_op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if c_op == "/":
        print("{} / {} = {}.".format(a, b, div(a, b)))
