# to describe 2 objects (squares and circles)
class Shape:
    def area(self):
        pass # this is a placeholder that allow us to create empty code
                # without causing errors.

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2

import math
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth
    def area(self):
        return 0.5*self.base*self.heigth
    
   
square = Square(5)
print("Area of the square", square.area())
circle = Circle(3)
print("Area of the circle", circle.area())
triangle = Triangle(4,5)
triangle2 = Triangle(5,6)
print("the Area of the Triangle is", triangle2.area())
    
    