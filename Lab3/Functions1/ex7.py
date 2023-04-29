def has_33(x):
    for i in range(len(x) - 1):
        if x[i] == 3 and x[i + 1] == 3:
            return True
    return False

print (has_33([1, 3, 3])) 
print (has_33([1, 3, 1, 3])) 
print (has_33([3, 3, 1, 3])) 
