'''-- Day 1: Secret Entrance ---'''

#Get the file info
file = open('input.txt')

pointer = 50
times = 0
turns = 0
#Read the file line by line
for line in file:
    #delete the spaces
    line = line.rstrip()

    #Get the rotation by direction + positions
    direction = line[:1]
    positions = int(line[1:])

    #Reduce the number by the size of the circle to avoid complete turns and count them
    turns = turns + int(positions / 100)
    positions = positions % 100

    #get the new position
    if direction == 'L':
        newPosition = pointer - positions
        if newPosition < 0:
            newPosition = 100 + newPosition
            if newPosition != 0 and pointer != 0:
                turns = turns + 1

    else:
        newPosition = pointer + positions
        if newPosition > 99: 
            newPosition = newPosition - 100
            if newPosition != 0 and pointer != 0:
                turns = turns + 1

    pointer = newPosition
    
    #check whether the circle is pointing to 0
    if pointer == 0:
        times = times +1
        

print('Total of 0 pointing', times)
print('Total of 0 pointing plus turns', turns + times)
