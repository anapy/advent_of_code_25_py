inputFile = open('input.txt')
inputFile = inputFile.readlines()

def generateResult(itemOne, itemTwo, operator):
    if operator == '*':
        return int(itemOne) * int(itemTwo)
    elif operator == '+':
        return int(itemOne) + int(itemTwo)
    return 0

resultList = list()
for i, line in enumerate(reversed(inputFile)):
    line = line.strip()
    items = line.split(' ')
    pointer = 0
    for item in (items):
        #if line is 0(in reverse) the operators, save it
        if i == 0:
            if item == '+' or item == '*':
                resultList.append([item, '0'])
        #if line is the first line with numbers, save them for later
        elif i == 1 and len(resultList) > 0:
            if item.isdigit():
                resultList[pointer][1] = item
                pointer += 1
        #if line is from 2nd to last one, save the new result from add or multiply last result to the new number
        elif i > 1 and len(resultList) > 0:
            if item.isdigit():
                resultList[pointer][1] = generateResult(item, resultList[pointer][1], resultList[pointer][0])
                pointer += 1
print(sum(result[1] for result in resultList))


