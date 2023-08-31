#!/usr/bin/python3

"""Define of class"""
class Square:
    """Represent class"""
    def __init__(self, size=0):
        """Initialize the class
        Args:
            size (int): The size of the new square class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
