from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r", encoding="utf-8") as f:
    inputFile = f.readlines()

coordinatesList = list()
for line in inputFile:
        coordinatesList.append(tuple(map(int, line.strip().split(','))))

distList = []
for i in range(len(coordinatesList)):
    for j in range(i + 1, len(coordinatesList)):
        dx = coordinatesList[i][0] - coordinatesList[j][0]
        dy = coordinatesList[i][1] - coordinatesList[j][1]
        dz = coordinatesList[i][2] - coordinatesList[j][2]

        dist2 = dx*dx + dy*dy + dz*dz
        distList.append((dist2, i, j))

distList.sort()

print(distList[:5])

# Union-Find
n = len(coordinatesList)

parent = list(range(n))
size = [1] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

# Conectar los 1000 pares más cercanos
for _, i, j in distList[:1000]:
    union(i, j)

# Calcular tamaños finales
components = {}

for i in range(n):
    root = find(i)
    components[root] = components.get(root, 0) + 1

sizes = sorted(components.values(), reverse=True)

answer = sizes[0] * sizes[1] * sizes[2]

print(answer)