# geometry_toolkit.py
import math

class ShapeCalculator:
    def area(self, x=None, y=None):
        if x is not None and y is None:
            return math.pi * x * x
        elif x is not None and y is not None:
            return x * y
        else:
            return 0

# Demo
calc = ShapeCalculator()
print("Area of Circle (radius=5):", calc.area(5))
print("Area of Rectangle (4x6):", calc.area(4, 6))
