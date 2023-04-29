class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

x = int(input())
y = int(input())
rec_area = Rectangle(x, y)
print(rec_area.area())
