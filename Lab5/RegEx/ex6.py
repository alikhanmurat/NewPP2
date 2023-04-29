import re   

txt = str(input())

x = re.sub('[ ,.]', ':', txt)

print(x)
