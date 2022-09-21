#!/usr/bin/python3
def islower(c):
    """This is a function that checks for lowercase character."""
    for c in range("a", "z"):
        if c.islower() == True:
            print("{:c}.format(c) is lower")
        elif c.islower() == False:
            print("{:c}.format(c) is upper")
        else:
            print("{:d}.format(c) is upper")
