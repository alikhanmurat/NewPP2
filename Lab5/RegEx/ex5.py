import re
txt = str(input())
x = re.search("ab$", txt)

if x:
    print ("Yes")
else:
    print ("No")
