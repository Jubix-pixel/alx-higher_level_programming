#!/usr/bin/python3
def uppercase(str):
    for str in range(65, 91):
        if (ord(str) >= "A" and ord(str) <= "Z"):
            print("{:s}".format(str))
        else:
            return(str)
