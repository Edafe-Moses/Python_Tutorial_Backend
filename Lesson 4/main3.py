import math


def perimeterOfRectangle():
    a = 12
    b = 23
    print(f"The Perimeter of Rectangle is {2 * int(a) * int(b)}")


def circumferenceOfCircle():
    r = 7
    print(f"The Circumfrence of a Circle with Radius {7} is {2 * math.pi * int(r)}")


def perimeterOfRect(x: float, y: float):
    print(f"Product of {x} and {y} is {x * y}")


perimeterOfRectangle()

circumferenceOfCircle()

perimeterOfRect(4, 3)
