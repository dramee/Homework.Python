import numpy as np
from random import randint


def check_dead_or_alive(arr, x, y):
    counter = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            if arr[x + i][y + j] == 1:
                counter += 1
    if arr[x][y] == 1:
        if counter < 2 or counter > 3:
            arr[x][y] = 0
    else:
        if counter == 3:
            arr[x][y] = 1
    return field


DIM = 8

field = [[randint(0, 1) for i in range(DIM)] for j in range(DIM)]


for i in range(DIM):
    print(field[i])

print()

for j in range(DIM):
    for k in range(DIM):
        field = check_dead_or_alive(field, j, k)


for i in range(DIM):
    print(field[i])