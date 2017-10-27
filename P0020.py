from math import factorial

Number = factorial(100)
Answer = 0
for x in str(Number):
    Answer += int(x)
print(Answer)