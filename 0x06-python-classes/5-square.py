#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ rep... of a square class"""

    def __init__(self, size=0):
        """ instantation with size for our object 
        initialization
        """
        self.__size = size

        """ Getter for the private attr size"""
    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ method that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ print rep of square with a char... """
        for item in range(self.__size):
            [print("#", end="") for j in range(self.__size)]