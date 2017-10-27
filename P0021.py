def sum_divisors(Number):
    Answer = 1
    for i in range(2, Number//2+1):
        if Number % i == 0:
            Answer += i
    return Answer

DivisorSet = {}
Answer = 0
for i in range(1, 10000):
    n = sum_divisors(i)
    DivisorSet[i] = n
    if i > n:
        if DivisorSet[n] == i:
            Answer += i + n
print(Answer)