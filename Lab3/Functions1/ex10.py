def my_function(x):
  return list(dict.fromkeys(x))

y = int(input())
thislist = []
for i in range(y):
  z = str(input())
  thislist.append(z)
  
mylist = my_function(thislist)
print(mylist)
