inputFile = open('input.txt')

diagram = list()
for line in inputFile:
    line = list(line.rstrip())
    diagram.append(line)

accessible = 0
accessibleStart = -1
while accessibleStart < accessible:
    accessibleStart = accessible
    for x in range(len(diagram)):
        for y in range(len(diagram[x])):

            if diagram[x][y] != '@':
                continue

            neighbours = 0

            #iterate the neighbours positions
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):

                    #skip the current cell
                    if dx == 0 and dy == 0:
                        continue

                    #calculate the neighbours positions
                    nx = x + dx
                    ny = y + dy

                    #verify limits: check if line exit, colum exit and that there's a roll on the cell
                    if (
                        0 <= nx < len(diagram)
                        and 0 <= ny < len(diagram[0])
                        and diagram[nx][ny] == '@'
                    ):
                        neighbours += 1

            if neighbours < 4:
                accessible += 1
                diagram[x][y] = 'x'

print(accessible)