def least_factor(Number, MaxFactor, Start=2):
    # MaxFactor = int(n**0.5)
    # if Start == 2:
        # if Number % 2 > 0:
            # Start = 3
    for i in range(Start, MaxFactor + 1):
        if Number % i == 0:
            return i
    return Number

def factors_greater_than(Number, AmountGreaterThan):
    # CurrentNumber = Number
    NextFactor = 1
    MaxFactor = int(Number**0.5)
    TotalFactors = 0
    while NextFactor <= MaxFactor:
        NextFactor = least_factor(Number, MaxFactor, NextFactor)
        if NextFactor < MaxFactor:
            TotalFactors += 2
        elif NextFactor == MaxFactor:
            TotalFactors += 1
        if TotalFactors > AmountGreaterThan:
            return True
        NextFactor += 1
    return False
    
Triangle = 0
NextGrowth = 1
AmountGreaterThan = 500
Found = False
while not Found:
    Triangle += NextGrowth
    NextGrowth += 1
    Found = factors_greater_than(Triangle, AmountGreaterThan)
print(Triangle)