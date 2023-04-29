from functools import reduce

z = int(input())

mylist = []
for i in range(z):
    y = int(input())
    mylist.append(y)


result = reduce(lambda x, y: x * y, mylist)
print(result)
