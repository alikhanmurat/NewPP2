def down (x):
    while x >= 0:
        yield x
        x -= 1

x = int(input())

for z in down (x):
    print(z)
