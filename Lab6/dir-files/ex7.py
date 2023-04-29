f1 = open("textex5.txt", "r")
f2 = open("textex7.txt", "w")

for i in f1:
    f2.write(i)
    f2.flush()
    
f1.close()
f2.close()
