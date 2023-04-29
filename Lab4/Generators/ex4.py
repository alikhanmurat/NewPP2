def square (x, y):
    for i in range (x, y+1):
        yield i * i

x = int(input())
y = int(input())

for z in square (x, y):
    print(z)
