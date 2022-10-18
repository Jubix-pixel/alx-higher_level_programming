#!/usr/bin/python3
"""

This Module is compiled by a class that defines a rectangle.

"""

class Rectangle:
    """Class that Defines a Rectangle."""
    def __init__(self, width=0, height=0):
        """Method that initializes the instance


        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.


        """
        self.width = width
        self.height = height

    @property
    def self(width):
        """Method that returns the value of the width.

        Retruns: Width of the rectangle.

        """
