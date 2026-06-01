'''First idea: 
1. Create a list of list where every line is an array in the first list([@@@..@@],[..@@...]...])
2. Iterate the list and save in a second list of lists the results: add 1 each time an @ is on the adyacent position
3. Count the total number results lower than 4
'''

#1. Read the input to create the array
inputFile = open('input.txt')

diagram = list()
for line in inputFile:
    line = list(line.rstrip())
    diagram.append(line)

#print(diagram[0])

def getItemValue (item):
    if item == '.':
        return 0
    elif item == '@':
        return 1
    else:
        return 0

results = []
#Iterate the list to create the results

for x in range(len(diagram)):
    dictLine = dict()
    dictLinefut = dict()
    for y in range(len(diagram[x])):
        valueItem = getItemValue(diagram[x][y])
        if valueItem == 0:
            continue
        #añadir a los adyacentes
        #same line

        if valueItem == 1:
            dictLine[y - 1] = dictLine.get(y - 1, 0) + valueItem
            dictLine[y + 1] = dictLine.get(y + 1, 0) + valueItem
        if x > 0:
            results[x-1][y - 1] = dictLine.get(y + 1, 0) + valueItem
            results[x-1][y] = dictLine.get(y, 0) + valueItem
            results[x-1][y + 1] = dictLine.get(y + 1, 0) + valueItem
        if x < len(diagram) - 1:
            dictLinefut[y - 1] = dictLinefut.get(y - 1, 0) + valueItem
            dictLinefut[y] = dictLinefut.get(y, 0) + valueItem
            dictLinefut[y + 1] = dictLinefut.get(y + 1, 0) + valueItem
    results.append(dict(sorted(dictLine.items())))
    results.append(dict(sorted(dictLinefut.items())))

