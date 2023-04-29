import re
txt = str(input())
x = re.search("ab{2}|b{3}", txt)

if x:
    print ("Yes")
else:
    print ("No")
