inputFile = open('input.txt')
voltageSum = 0
for line in inputFile:
    numbers = list()
    line = list(line.rstrip())

    #split the batteries bank
    batteries = line

    firstNumber = max(batteries[:len(batteries) - 12])
    firstIndex = batteries.index(firstNumber)
    batteries = batteries[firstIndex:]
    i = 0
    while len(batteries) >= 12:
        try:
            #case following number is bigger than current one -> delete current
            if batteries[i] < batteries[i + 1]:
                batteries.pop(i)
            else:
                #Check first is the current number is higher than the possible max number within the pending ones
                possibleMax = max(batteries[i:len(batteries) - 11 + i]) if len(batteries) > i else batteries[i]

                #If same as the possible max keep the number and increase the index
                if batteries[i] == possibleMax:
                    i += 1

                #If smaller than the possible max delete it
                else:
                    batteries.pop(i)
    
            #print('fin', batteries, len(batteries), i, batteries[i], 'pos ', possibleMax, len(batteries) - 12 + i)
            if(i == len(batteries) - 1): batteries = batteries[:12]
            if(len(batteries) == 12):
                delimiter = ''
                voltageSum +=(int(delimiter.join(batteries)))
                break
        except ValueError:
            #print(batteries, i, numbers)
            print(ValueError)
            break

print('Final joltage is ', voltageSum)
