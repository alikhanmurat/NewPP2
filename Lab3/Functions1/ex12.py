def histogram(x):
    for i in x:
        print('*' * i)

y = int(input())
thislist = []
for i in range(y):
    z = int(input())
    thislist.append(z)
  
histogram(thislist)
