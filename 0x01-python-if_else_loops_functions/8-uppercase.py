#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 65 and ord(str[i]) <= 90):
            print("{:s}".format(ord)(str[i]))
        else:
            return(str)
