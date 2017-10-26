def sum_fifth_power_digits(Number):
    Total = 0
    while Number:
        Total, Number = Total + (Number % 10) ** 5, Number // 10
    return Total

Answer = 0
# Answers under 4 digits can be eliminated because all possibilities have digits greater than allowed for 2- or 3-digits sums
# 1024 is the smallest theoretical possible answer because 4^5 = 1024 and 3^4 * 4 < 1000
# 6442 is the greatest possible 4 digit number, 6443 and greater resolves to a 5-digit sum
for x in range(1024, 6442):
    if x == sum_fifth_power_digits(x):
        print(x)
        Answer += x
# 98632 is the greatest possible 5 digit number, 98633 and greater resolves to a 6-digit sum
for x in range(10000, 98632):
    if x == sum_fifth_power_digits(x):
        print(x)
        Answer += x
# 354294 = 9^5 * 6 is the greatest possible answer, all greater numbers will be larger than the possible sum
for x in range(100000, 354294):
    if x == sum_fifth_power_digits(x):
        print(x)
        Answer += x
print(Answer)