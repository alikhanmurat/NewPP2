import os

path = str(input())

if os.access(path, os.F_OK):
    print("File exists")
else:
    ("File doesn't exist")

if os.access(path, os.R_OK):
    print("File readable")
else:
    ("File isn't readable")

if os.access(path, os.W_OK):
    print("File writable")
else:
    ("File isn't writable")

if os.access(path, os.X_OK):
    print("File executable")
else:
    ("File isn't executable") 
