file = open('input.txt')
ranges = file.read().strip()

'''return all divisors from a number except itself'''
def getDivisors(number: int):
    divisors = [1]
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

total_sum = 0

#Read the file and split the numbers by commas
rangeList = ranges.split(',')

#Convert the string to number ranges
for item_range in rangeList:

    start, end = item_range.split('-')

    initialNumber = int(start)
    endNumber = int(end)

    #Iterate ranges
    while initialNumber <= endNumber:
        #Check whether number split by half are a repeated sequence
        stringNumber = str(initialNumber)
        numberLength = len(stringNumber)

        #get lenght divisors
        divisors = getDivisors(numberLength)

        invalidID = False
        for divisor in divisors:
            patternLength = divisor

            if numberLength % patternLength != 0:
                continue
            
            #initial pattern
            pattern = stringNumber[:patternLength]

            #number of times pattern should be repeated
            repetitions = numberLength // patternLength

            #desired number when repeated
            reconstructed = pattern * repetitions
 
            if repetitions >= 2 and reconstructed == stringNumber: 
                invalidID = True
                break
        if invalidID:
            total_sum += initialNumber

        initialNumber += 1


print('The sum is: ', total_sum)