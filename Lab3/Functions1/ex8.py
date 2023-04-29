def spy_game(x): 
    cnt = 0  
    pos = 0

    for i in range (len(x)): 
        if x[i] == 7: 
            pos = i 
    for i in range(pos): 
        if x[i] == 0: 
            cnt += 1   

    if(cnt >= 2):      
        return True 
    else: 
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
