def is_prime(Number):
    bool_Prime = True
    for i in range(2, int(Number**0.5) + 1):
        if Number % i == 0:
            bool_Prime = False
            break
    return bool_Prime

def least_factor(Number, Start=2):
    MaxFactor = int(Number**0.5)
    if Start == 2:
        if Number % 2 > 0:
            Start = 3
    for i in range(Start, MaxFactor + 1, 2):
        if Number % i == 0:
            return i
    return Number

def greatest_prime_factor(Number):
    CurrentNumber = Number
    NextFactor = 2
    while CurrentNumber > 1:
        NextFactor = least_factor(CurrentNumber, NextFactor)
        CurrentNumber //= NextFactor
    return NextFactor

n = 600851475143
Answer = greatest_prime_factor(n)
print(Answer)
# print(is_prime(Answer))
# print(greatest_prime_factor(2))
# print(greatest_prime_factor(3))
# print(greatest_prime_factor(4))
# print(greatest_prime_factor(10))
# print(greatest_prime_factor(42))