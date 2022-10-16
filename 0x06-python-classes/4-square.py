#!/usr/bin/python3
# 4-square.py
""" Define a Square."""

class Square:
    """Represent a Square."""
    def __init__(self, size=0):
        """initialize a new square
        Args:
            size (int): the size of a new square.
        """
        self.size = size

        @property
        def size(self):
            """Get/Set the current size of the square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Return The current Area of the square."""
            return (self.__size * self.__size)
