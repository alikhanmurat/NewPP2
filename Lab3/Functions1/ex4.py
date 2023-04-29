import math

def filter_prime(x):
    def prime(y):
        if y < 2:
            return False
        for i in range(2, int(math.sqrt(y)) + 1):
            if y % i == 0:
                return False
        return True

    return [y for y in x if prime(y)]

z = int(input())
thislist = []
for i in range(z):
    w = int(input())
    thislist.append(w)

primes = filter_prime(thislist)
print(primes)
