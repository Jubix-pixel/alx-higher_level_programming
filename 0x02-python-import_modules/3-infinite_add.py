#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    n = len(sys.argv)
    for x in range(1, n):
        add += int(sys.argv[x])
    print(add)
