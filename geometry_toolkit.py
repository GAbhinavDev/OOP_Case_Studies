# geometry_toolkit.py

import math

class ShapeCalculator:
    def area(self, length, width=None):
        if width is None:
            # Only one argument — Circle
            result = math.pi * length * length
            print(f"Area of circle with radius {length}: {result:.2f}")
            return result
        else:
            # Two arguments — Rectangle
            result = length * width
            print(f"Area of rectangle with length {length} and width {width}: {result}")
            return result

# Test the code
if __name__ == "__main__":
    calculator = ShapeCalculator()
    calculator.area(5)          # Circle
    calculator.area(4, 6)       # Rectangle
