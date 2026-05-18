inputFile = open('input.txt')

voltageSum = list()
for line in inputFile:
    numbers = list()
    line = list(line.rstrip())
    print(line)

    #split the batteries bank
    batteries = line

    #get one maximum digit
    firstMax = max(batteries)

    #get its index
    firstMaxIndex = batteries.index(firstMax)
    
    #edge case when the biggest number is the last one on the list
    if firstMaxIndex == len(batteries) - 1: 
        secondMax = firstMax
        firstMax = max(batteries[:firstMaxIndex])
        joltage = firstMax + secondMax
        print('caso 1: ', joltage)
    else:
        secondMax = max(batteries[firstMaxIndex + 1:])
        joltage = firstMax + secondMax
        print('caso 2: ', joltage)

    voltageSum.append(int(joltage))


print(voltageSum)
print('final joltage is ', sum(voltageSum))
