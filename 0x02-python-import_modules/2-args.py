#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))
    n = 0
    if n >= 1:
        for args in sys.argv:
            if n != 0:
                print("{}: {}".format(n, args))
            n += 1
