from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r", encoding="utf-8") as f:
    inputFile = f.readlines()

coordinatesList = [
    tuple(map(int, line.strip().split(",")))
    for line in inputFile
]
print(coordinatesList[:7])

def calculateArea(x1, x2, y1, y2):
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height

maxArea = 0
for i in range(len(coordinatesList)):
    for j in range(i + 1, len(coordinatesList)):
        area = calculateArea(coordinatesList[i][0], coordinatesList[j][0],coordinatesList[i][1],coordinatesList[j][1])
        maxArea = max(maxArea, area)
        print(coordinatesList[i], coordinatesList[j],area)

print(maxArea)