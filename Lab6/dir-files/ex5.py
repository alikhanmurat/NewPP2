mylist = ['1', '2', '3', '4', '5']

f = open("textex5.txt", "w")

for i in mylist:
    f.write(str(i))
    f.write("\n")

f.close()
