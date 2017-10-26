from math import log
Number = 2**1000
Digits = int(log(Number, 10)) + 1
Total = 0
print(Number)
print(Digits)
for i in range(0, Digits):
    Total += Number // 10**i % 10
print(Total)