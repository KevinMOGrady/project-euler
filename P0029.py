SolutionSet = {}
for a in range(2, 101):
    for b in range(2, 101):
        x = a**b
        SolutionSet[x] = x
print(len(SolutionSet))