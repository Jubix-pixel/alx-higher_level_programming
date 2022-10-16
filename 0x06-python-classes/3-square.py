#!/usr/bin/python3
# 3-square.py
""" Define a Class Square."""

class Square:
    """Represent a Class Square."""
    def __init__(self, size=0):
        """initialise a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.area = size * size
        return (self.area)
