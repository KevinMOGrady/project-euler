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

Limit = 2000000
Result = 0
for i in range(2, Limit):
    if is_prime(i): Result += i
print(Result)