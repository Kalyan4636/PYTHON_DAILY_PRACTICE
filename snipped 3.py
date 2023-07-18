class Shape:
 def __init__(self, color):
 self.color = color
 def get_color(self):
 return self.color
class Circle(Shape):
 def __init__(self, color, radius):
 super().__init__(color)
 self.radius = radius
 def get_area(self):
 return 3.14 * self.radius**2
circle = Circle("Red", 5)
result = circle.get_color()
print(result)
