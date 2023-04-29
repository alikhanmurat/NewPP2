import math

class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y2

    def show(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

p1.show()

print(p1.dist(p2)) 
