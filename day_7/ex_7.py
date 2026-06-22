from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r", encoding="utf-8") as f:
    inputFile = f.readlines()

beamPosition = set()
beamSplit = 0
for i, line in enumerate(inputFile):
    listLine = list(line)
    if i == 0:
        x = listLine.index('S')
        beamPosition.add(x)
        continue
    
    newPositions = beamPosition.copy()
    for position in beamPosition:
        if listLine[position] == '^':
            newPositions.add(position - 1)
            newPositions.add(position + 1)
            newPositions.discard(position)
            beamSplit += 1
    beamPosition = newPositions
print(beamSplit)