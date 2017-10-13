n1 = 1
n2 = 2
n3 = 3
x = 2
range = 4000000
while n3 <= range:
    if n3 % 2 == 0:
        x += n3
    n1 = n2
    n2 = n3
    n3 = n1 + n2
print(x)