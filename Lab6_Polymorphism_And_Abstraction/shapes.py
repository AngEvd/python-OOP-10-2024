from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> None:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> None:
        pass


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.__radius = radius

    def calculate_area(self) -> float:
        return pi * pow(self.__radius, 2)

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height: int, width: int) -> None:
        self.__height = height
        self.__width = width

    def calculate_area(self) -> int:
        return self.__width * self.__height

    def calculate_perimeter(self) -> int:
        return 2 * (self.__width + self.__height)
