import os

path = str(input())

print("Directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)

print("\nFiles:")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)

print("\nAll Directories and Files:")
for root, dirs, files in os.walk(path):
    for i in files:
        print(os.path.join(root, i))
    for i in dirs:
        print(os.path.join(root, i))
