inputFile = open('input.txt')

diagram = list()
for line in inputFile:
    line = list(line.rstrip())
    diagram.append(line)

accessible = 0
for x in range(len(diagram)):
    for y in range(len(diagram[x])):

        if diagram[x][y] != '@':
            continue

        neighbours = 0

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):

                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < len(diagram)
                    and 0 <= ny < len(diagram[0])
                    and diagram[nx][ny] == '@'
                ):
                    neighbours += 1

        if neighbours < 4:
            accessible += 1

print(accessible)