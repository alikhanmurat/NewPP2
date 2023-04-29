import re

def space(txt):
    
    x = re.findall('[A-Z][a-z]*', txt)
    newtxt = ' '.join(x)
    return newtxt

txt = input()
print(space(txt))
