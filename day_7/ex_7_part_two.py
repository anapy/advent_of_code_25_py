from collections import defaultdict
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r", encoding="utf-8") as f:
    inputFile = f.readlines()

beamPosition = {}

for i, line in enumerate(inputFile):
    row = line.rstrip("\n")

    if i == 0:
        x = row.index("S")
        beamPosition[x] = 1
        continue

    newPositions = defaultdict(int)

    for position, count in beamPosition.items():

        if row[position] == "^":
            newPositions[position - 1] += count
            newPositions[position + 1] += count
        else:
            newPositions[position] += count

    beamPosition = newPositions

print(sum(beamPosition.values()))