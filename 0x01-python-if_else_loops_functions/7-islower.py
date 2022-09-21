#!/usr/bin/python3
def islower(c):
    """This is a function that checks for lowercase character."""
    if c.islower('a') == True:
        print("a is lower")
    if c.islower('H') == False:
        print("H is upper")
    if c.islower('A') == False:
        print("A is upper")
    if c.islower('3') == False:
        print("3 is upper")
    if c.islower('g') == True:
        print("g is upper")
