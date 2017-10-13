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

def nth_prime(n):
    if n <= 1:
        return 2
    CurrentNumber = 1
    x = 1
    while x < n:
        CurrentNumber += 2
        if is_prime(CurrentNumber):
            x += 1
    return CurrentNumber

# print(nth_prime(1))
# print(nth_prime(2))
# print(nth_prime(6))
print(nth_prime(10001))
# print(is_prime(5))
# print(is_prime(1))
# print(is_prime(7))