'''inputFile = open('input.txt')
inputFile = inputFile.readlines()'''
from pathlib import Path
import math

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r", encoding="utf-8") as f:
    inputFile = f.readlines()


def generateResult(numberList, operator):
    if operator == '+':
        return sum(int(x) for x in numberList)
    elif operator == '*':
        return math.prod(int(x) for x in numberList)
    return 0

resultList = list()
itemByItemList = list()
for i, line in enumerate(inputFile):
    itemByItemList.append(list(line))

finalResultList = list()
for i, itemLine in enumerate(itemByItemList):
    itemPointer = 0
    groupPointer = 0
    lastItemSpace = False
    newGroup = True
    operatorPointer = 0
    for k, item in enumerate(reversed(itemLine)):
        if item.isdigit():
            if i == 0:
                if newGroup:
                    resultList.append(list())
                    newGroup = False
                resultList[groupPointer].append(item)
            else:
                if len(resultList[groupPointer]) <= itemPointer:
                    resultList[groupPointer].append(item)
                else:
                    resultList[groupPointer][itemPointer] = resultList[groupPointer][itemPointer]+ item
                newGroup = False
            itemPointer += 1
            lastItemSpace = False
        elif item == '+' or item == '*':
            finalResultList.append(generateResult(resultList[operatorPointer], item))
            lastItemSpace = False
            operatorPointer += 1
        elif item == ' ':
            if lastItemSpace:
                itemPointer += 1
            elif newGroup:
                if i == 0:
                    resultList.append(list())
                    resultList[groupPointer].append('')
                itemPointer += 1
                newGroup = False
            else:
                newGroup = True
                groupPointer += 1
                itemPointer = 0
            lastItemSpace = True

print(sum(finalResultList))