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
            [print() for y in range(self.y)]  # Handling Y coordinate
            for i in range(self.height):
                [print(" ", end="") for x in range(self.x)]
                for j in range(self.width):
                    print("#", end="")
                print()

        def update(self, *args, **kwargs):
            """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        argument = list(args)  # Unpacking the tuple
        """Getting the index and value and assigning them appropriately"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

        def to_dictionary(self):
            """Return the dictionary representation of a Rectangle."""
            return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }

        def __str__(self):
            """Return the print() and str() representation of the Rectangle."""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                           self.x, self.y,
                                                           self.width,
                                                           self.height)
