#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    n = len(sys.argv) - 1
    for x in range(1, n):
        i = i + int(sys.argv[x])
    print("{}".format(i))
