import os

path = str(input())

if not os.path.exists(path):
    print ("Path doesn't exit")
    quit()

os.remove(path)
