class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length * self.length

x = int(input())
square_area = Square(x)
print(square_area.area())
