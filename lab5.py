import math
from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def __del__(self):
        print(f"Об'єкт Point({self._x}, {self._y}) видалено")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def distance_to(self, other):
        return math.hypot(self._x - other._x, self._y - other._y)

    def show(self):
        print(self)

    def __str__(self):
        return f"({self._x}; {self._y})"


class Polynom:
    def __init__(self, points=None, colour=Colour.RED):
        self._points = list(points) if points else []
        self._colour = colour

    def __del__(self):
        print(f"Об'єкт Polynom ({len(self._points)} точок) видалено")

    @property
    def points(self):
        return self._points

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, value):
        if not isinstance(value, Colour):
            raise TypeError("colour має бути елементом enum Colour")
        self._colour = value

    def perimeter(self):
        n = len(self._points)
        if n < 2:
            return 0.0
        return sum(self._points[i].distance_to(self._points[(i + 1) % n])
                   for i in range(n))

    def diagonals(self):
        n = len(self._points)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                adjacent = (j == i + 1) or (i == 0 and j == n - 1)
                if not adjacent:
                    result.append((i, j, self._points[i].distance_to(self._points[j])))
        return result

    def longest_diagonal(self):
        diags = self.diagonals()
        if not diags:
            return None
        return max(diags, key=lambda d: d[2])

    def sort_by_x(self):
        self._points.sort(key=lambda p: (p.x, p.y))

    def sort_by_y(self):
        self._points.sort(key=lambda p: (p.y, p.x))

    def show(self):
        print(f"Многокутник, колір: {self._colour.name}, "
              f"кількість точок: {len(self._points)}")
        for i, p in enumerate(self._points):
            print(f"  Точка {i}: {p}")

    def show_perimeter(self):
        print(f"Периметр: {self.perimeter():.3f}")

    def show_diagonals(self):
        diags = self.diagonals()
        if not diags:
            print("Діагоналей немає (потрібно щонайменше 4 точки)")
            return
        print("Діагоналі:")
        for i, j, d in diags:
            print(f"  між точками {i} та {j}: {d:.3f}")
        i, j, d = self.longest_diagonal()
        print(f"Найдовша діагональ: між точками {i} та {j}, довжина {d:.3f}")


def main():
    p1 = Point(0, 0)
    p2 = Point(4, 1)
    p3 = Point(5, 5)
    p4 = Point(1, 4)

    poly = Polynom([p1, p2, p3, p4], Colour.GREEN)
    poly.show()
    print()
    poly.show_perimeter()
    poly.show_diagonals()

    poly.sort_by_x()
    print("\nСортування за x:")
    poly.show()

    poly.sort_by_y()
    print("\nСортування за y:")
    poly.show()

    p1.x = 2
    poly.colour = Colour.BLUE
    print(f"\nПісля змін: p1 = {p1}, колір {poly.colour.name}\n")

    del poly
    del p1, p2, p3, p4


if __name__ == "__main__":
    main()