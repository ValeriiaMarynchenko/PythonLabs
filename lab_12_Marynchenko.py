import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = math.sqrt(
            (self.__vertices[1]._x - self.__vertices[0]._x) ** 2 + (self.__vertices[1]._y - self.__vertices[0]._y) ** 2)
        side2 = math.sqrt(
            (self.__vertices[2]._x - self.__vertices[1]._x) ** 2 + (self.__vertices[2]._y - self.__vertices[1]._y) ** 2)
        side3 = math.sqrt(
            (self.__vertices[0]._x - self.__vertices[2]._x) ** 2 + (self.__vertices[0]._y - self.__vertices[2]._y) ** 2)

        perimeter = side1 + side2 + side3
        return perimeter


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
