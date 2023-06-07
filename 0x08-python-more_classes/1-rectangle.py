#!/usr/bin/python3
"""A class that defines a rectangle that has 2 private attributes"""


class Rectangle:
    """intialise the class with class"""

    def __init__(self, width=0, height=0):
        
        self.width = width
        self.height = height


    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter

    def width(self, value):
        """sets the width attribute into a public variable"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
