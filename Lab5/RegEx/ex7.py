import re   

def snake_to_camel(str1):
    str1 = list(str1.split('_'))
    str2 = str(str1[0])
    for i in range(1, len(str1)):
        str2 += (str1[i][0]).upper()
        str2 += str1[i][1:]
    return str2 

str1 = str(input())
x = snake_to_camel(str1)
print(x)
