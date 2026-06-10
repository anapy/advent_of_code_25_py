inputFile = open('input.txt')

#read the file and create two groups: ranges of correct ids and productIds
idsRanges = list()
productIds = list()
for line in inputFile:
    line = line.strip()

    if not line:
        continue

    if '-' in line:
        numbers = line.split('-')
        idsRanges.append((int(numbers[0]), int(numbers[1])))
        idsRanges.sort()

    else:
        productIds.append(int(line))
        productIds.sort()
    

fresh = 0
for number in productIds:
    for id in idsRanges:
        if number < id[0]:
            break
        elif number >= id[0] and number <= id[1]:
            print(number, id )
            fresh += 1
            break

print(fresh)