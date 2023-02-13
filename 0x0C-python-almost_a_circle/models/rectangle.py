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
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
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
            """Validating the method"""
            if not isinstance(value, int):
                raise TypeError('width must be an intager')
            elif value <= 0:
                raise ValueError('width must be > 0')
            self.__width = value


        @property
        def height(self):
            """Get the height of the Rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """Validating the method"""
            if not isinstance(value, int):
                raise TypeError('height must be an intager')
            elif value <= 0:
                raise ValueError('height must be > 0')

            self.__height = value

        @property
        def x(self):
            """Get the x coordinate of the Rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            """Validating the method"""
            if not isinstance(value, int):
                raise TypeError('x must be an intager')
            elif value < 0:
                raise ValueError('x must be >= 0')
            self.__x = value

        @property
        def y(self):
            """Get the y coordinate of the Rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """Validating the method"""
            if not isinstance(value, int):
                raise TypeError('y must be an intager')
            elif value < 0:
                raise ValueError('y must be >= 0')

            self.__y = value

        def area(self):
            """Public method that returns area value of rectangle instance"""
            return self.width * self.height

        def display(self):
            """Prints in stdout the rectangle instance with char #"""
            for i in range(self.width):
                for j in range(self.height):
                    print("#", end="")
                print()

        def __str__(self):
            """Updates the string method"""
            return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
