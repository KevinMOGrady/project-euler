def is_prime(Number):
    if Number <= 1:
        return False
    elif Number <= 3:
        return True
    elif Number % 2 == 0 or Number % 3 == 0:
        return False
    for i in range(5, int(Number**0.5) + 1, 6):
        if Number % i == 0 or Number % (i+2) == 0:
            return False
    return True

MaxPrimes = 0
for a in range(-999, 1000):
    n = 0
    while is_prime(n**2 + a*n + 2):
        n += 1
    if n > MaxPrimes:
        MaxPrimes, MaxProduct = n, a * 2
for a in range(-999, 1000):
    for b in range(3, 998, 2):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > MaxPrimes:
            MaxPrimes, MaxProduct = n, a * b
print(MaxProduct)