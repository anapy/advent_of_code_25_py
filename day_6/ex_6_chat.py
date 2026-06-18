from pathlib import Path
from math import prod

input_path = Path(__file__).parent / "test.txt"

with open(input_path, encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]

# Todas las filas con el mismo ancho
width = max(len(line) for line in lines)
lines = [line.ljust(width) for line in lines]

# Transponer
transposed = []

for col in range(width):
    transposed.append(
        "".join(line[col] for line in lines)
    )
total = 0
current_numbers = []
current_operator = None

# Recorremos de derecha a izquierda
for row in reversed(transposed):

    stripped = row.strip()

    # fila vacía => fin de bloque
    if not stripped:
        if current_operator is not None:
            if current_operator == "+":
                total += sum(current_numbers)
            else:
                total += prod(current_numbers)

        current_numbers = []
        current_operator = None
        continue

    last_char = stripped[-1]

    if last_char in "+*":
        current_operator = last_char
        stripped = stripped[:-1].strip()

    if stripped:
        current_numbers.append(int(stripped))

# último bloque
if current_operator is not None:
    if current_operator == "+":
        total += sum(current_numbers)
    else:
        total += prod(current_numbers)

print(total)