#!/usr/bin/python3
def uppercase(str):
    for str in range(ord(65), ord(91)):
        if (ord(str) >= 65 and ord(str) <= 90):
            print("{:s}".format(str))
        else:
            return(str)
