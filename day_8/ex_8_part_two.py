from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

with open(input_path, "r", encoding="utf-8") as f:
    inputFile = f.readlines()

# Leer coordenadas
coordinatesList = [
    tuple(map(int, line.strip().split(",")))
    for line in inputFile
]

# Calcular todas las distancias al cuadrado
distList = []

for i in range(len(coordinatesList)):
    for j in range(i + 1, len(coordinatesList)):
        dx = coordinatesList[i][0] - coordinatesList[j][0]
        dy = coordinatesList[i][1] - coordinatesList[j][1]
        dz = coordinatesList[i][2] - coordinatesList[j][2]

        dist2 = dx * dx + dy * dy + dz * dz
        distList.append((dist2, i, j))

# Ordenar de menor a mayor distancia
distList.sort()

# -------------------------
# Union-Find
# -------------------------
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
        return False

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]
    return True


# Inicialmente hay n componentes
components = n

for _, i, j in distList:
    if union(i, j):
        components -= 1

        # Cuando todo queda conectado, esta es la última unión
        if components == 1:
            answer = coordinatesList[i][0] * coordinatesList[j][0]
            print(answer)
            break