inputFile = open('input.txt')

#read the file and create two groups: ranges of correct ids and productIds
idsRanges = list()
for line in inputFile:
    line = line.strip()

    if '-' in line:
            start, end = map(int, line.split("-"))
            idsRanges.append((start, end))
idsRanges.sort()
    

'''freshIds = set()
for idRange in idsRanges:
    pointer = int(idRange[0])
    i = 0
    while pointer <= idRange[1]:
        freshIds.add(pointer)
        i += 1
        pointer += 1

print(len(freshIds))'''

# Fusionar rangos
merged = []

for start, end in idsRanges:
    #merged[-1] -> implies the last range
    #merged[-1][1] -> the end of the last range
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Contar IDs frescos
total = sum(end - start + 1 for start, end in merged)

print(total)
