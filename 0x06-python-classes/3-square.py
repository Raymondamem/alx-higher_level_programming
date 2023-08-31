#!/usr/bin/python3

"""Define class"""
class Square:
    """Represente class"""
    def __init__(self, size=0):
        """Initialize class
        Args:
            size (int): The size of the class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Return the current area of square class"""
        return (self.__size * self.__size)
