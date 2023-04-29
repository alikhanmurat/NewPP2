string = str(input())
cntup = 0
cntlow = 0

for i in string:
    if i.isupper():
        cntup += 1
    elif i.islower():
        cntlow += 1

print ("Capital letters:", cntup)
print ("Lower letters:", cntlow)
