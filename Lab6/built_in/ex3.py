str1 = str(input())
str2 = reversed(str1)
str3 = ""

for x in str2:
    str3 += x

if str1 == str3:
    print ("Palinfdrome")
else:
    print ("Not a Palindrome")
