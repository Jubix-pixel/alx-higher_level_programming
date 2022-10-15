#!/usr/bin/python3
# 2-square.py
""" Define a Square of a Size Attribute."""

class Square:
    """Represent a Square of size attribute."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
