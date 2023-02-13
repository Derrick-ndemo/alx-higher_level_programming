#!/usr/bin/python3
"""Import the Base class from base.py"""
from models.base import Base

"""Define Rectangle class"""


class Rectangle(Base):
    """
    Inherits from methods and attributes from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
        """Initialize a new Rectangle.

        Args:
            id (int): The identity of the inherited Base.
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
            x(int): x value
            y (int): Y value
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """get the width of the Rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            """Get the height of the Rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            """Get the x coordinate of the Rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            """Get the y coordinate of the Rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
