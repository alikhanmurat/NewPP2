def filter_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if (x % i) == 0:
                return False
        else:
            return True

x = int(input())
thislist = []
for i in range(x):
    y = int(input())
    thislist.append(y)
    
prime_numbers = list(filter(lambda x: filter_prime(x), thislist))

print(prime_numbers)
