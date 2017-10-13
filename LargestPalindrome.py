import math

def is_palindrome(Number):
    Digits = int(math.log(Number, 10))
    IsPalindrome = True
    # for LowDigit, HighDigit in zip(range(0, (Digits + 1) // 2), range(Digits, (Digits // 2) + 1)):
    for LowDigit in range(0, (Digits + 1) // 2):
        HighDigit = Digits - LowDigit
        # print(HighDigit)
        HighNumber = Number // (10**HighDigit) % 10
        LowNumber = Number // (10**LowDigit) % 10
        # print(HighNumber)
        # print(LowNumber)
        if HighNumber != LowNumber:
            IsPalindrome = False
            break
    return IsPalindrome

def first_palindrome(High, Low):
    Product = 0
    for Number1 in range(High, Low-1, -1):
        for Number2 in range(High, Low-1, -1):
            Product = Number1 * Number2
            if is_palindrome(Product):
                print(Product)
                print(Number1)
                print(Number2)
                return (Product, Number1, Number2)
    return (0, 0, 0)
                
def greatest_palindrome(High, Low):
    NextAnswer = first_palindrome(High, Low)
    GreatestPalindrome = NextAnswer[0]
    while NextAnswer[0] != 0 and NextAnswer[1] >= NextAnswer[2]:
        NextAnswer = first_palindrome(NextAnswer[1] - 1, NextAnswer[2] + 2)
        if NextAnswer[0] > GreatestPalindrome:
            GreatestPalindrome = NextAnswer[0]
    return GreatestPalindrome

print(greatest_palindrome(999,100))

# for Number1 in range(998, 997, -1):
    # Number2 = 1
# print(Number1)

# first_palindrome()


# print(int(math.log(10001, 10)))
# print(is_palindrome(1))
# print(is_palindrome(10))
# print(is_palindrome(11))
# print(is_palindrome(121))
# print(is_palindrome(110))
# print(is_palindrome(1991))
# print(is_palindrome(98989))
# print(is_palindrome(987789))