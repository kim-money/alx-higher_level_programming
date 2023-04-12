#!/usr/bin/python3
"""defining a square subclass of the rectangle class.import rectangle and initialise to define square. then initialise a new square"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
      


    def __init__(self, size):

           self.integer_validator("size", size)
             super().__init__(size, size)
              self.__size = size
