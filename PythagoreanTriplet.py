a = 1
b = 2
c = 997

a = 332
b = 333
c = 335

# print((1000 - 335) / 2)
# print(((1000 - 335) / 2) % 1)

def solution():
    for c in range(335, 998):
        HalfRemainder = (1000 - c)/2
        if HalfRemainder % 1 == 0:
            a, b = int(HalfRemainder - 1), int(HalfRemainder + 1)
        else:
            a, b = int(HalfRemainder - 0.5), int(HalfRemainder + 0.5)
        while a > 0 and b < c:
            if a**2 + b**2 == c**2:
                print(a, b, c)
                return a*b*c
            a -= 1
            b += 1
    return 0

print(solution())