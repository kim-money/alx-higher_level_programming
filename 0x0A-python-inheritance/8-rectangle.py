#!/usr/bin/python3
"""Inheris from baseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
     """Represent a rectangle using BaseGeometry.Intialize a new Rectangle with height(int), and width(int)"""
    def __init__(self, width, height):

	self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

