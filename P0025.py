x1 = 1
x2 = 1
n = 2
temp = 0

while len(str(x2)) < 1000:
    temp, x1, n = x1 + x2, x2, n + 1
    x2 = temp
print(n)
print(x2)