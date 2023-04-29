import os
path = str(input())

if os.path.exists(path):
    print("Yes")
else:
    print("No")

if os.path.exists(path):
    print(os.path.basename(path))
else:
    print("No")

if os.path.exists(path):
    print(os.path.dirname(path))
else:
    print("No")
