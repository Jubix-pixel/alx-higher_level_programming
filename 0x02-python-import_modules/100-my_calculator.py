#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if n[1] != "+" and n[1] != "-" and n[1] != "*" and n[1] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    n[0] = int(a)
    n[2] = int(b)
    from calculator_1.py import add, sub, mul, div
    if n == 3:
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
