#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} argument.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))
    if n >= 1:
        i = 0
        for i in argv:
            print("{}: {}".format(n, i))
        i = i + 1
