file = open('input.txt')


#Read the file and split the numbers by commas
ranges = file.read()
rangeList = ranges.split(',')

sum = 0
#Convert the string to number ranges
for range in rangeList:
    sequence = (range.split('-'))
    initialNumber = int(sequence[0])
    endNumber = int(sequence[1])

    #Iterate ranges
    while initialNumber <= endNumber:
        #Check whether number split by half are a repeated sequence
        stringNumber = str(initialNumber)
        numberLength = len(stringNumber)
        if numberLength % 2 == 0:
            if stringNumber[:int(numberLength/2)] == stringNumber[int(numberLength/2):]:
                #Sum the number if so
                sum = sum + initialNumber

        initialNumber = initialNumber + 1

print('The sum is: ', sum)