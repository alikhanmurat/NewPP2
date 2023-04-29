mylist =[]
x = int(input())

for i in range(x):
    y = input()
    if y.isdigit():
        mylist.append(int(y))
    elif y == "False":
        mylist.append(False)
    else:
        mylist.append(y)

mytuple = tuple(mylist)

print(all(mytuple))
