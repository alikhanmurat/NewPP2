from itertools import permutations

x = str(input())

def permutation(string):
    string = list(permutations(string))
    print(string)

permutation(x)
