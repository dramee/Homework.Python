import numpy as np
from random import randint
from collections import namedtuple
from time import time


DIM = 50

field = [[randint(0, 1) for i in range(DIM)] for j in range(DIM)]
np_field = np.array(field)


def find_neighbourhood(x, y):
    check_x = list(range(-1, 2))
    check_y = list(range(-1, 2))
    if y == 0:
        check_y.pop(0)
    elif y == DIM - 1:
        check_y.pop(-1)
    if x == 0:
        check_x.pop(0)
    elif x == DIM - 1:
        check_x.pop(-1)
    neighborhood = namedtuple("neighborhood", ["check_x", "check_y"])
    neighborhood.check_x = check_x
    neighborhood.check_y = check_y
    return neighborhood


def alive_or_dead(field, x, y):
    neighbourhood = find_neighbourhood(x, y)
    alive_counter = 0
    main_cell = None
    for i in neighbourhood.check_x:
        for j in neighbourhood.check_y:
            if i == 0 and j == 0:
                main_cell = field[y][x]
            else:
                if field[y + j][x + i]:
                    alive_counter += 1
    if main_cell and (alive_counter < 2 or alive_counter > 3):
        field[y][x] = 0
    elif not main_cell and alive_counter == 3:
        field[y][x] = 1
    pass


def life_game(field):
    start = time()
    for itr in range(128):
        for y in range(DIM):
            for x in range(DIM):
                alive_or_dead(field, x, y)
    end = time()
    return end - start


# for ln in field:
#     print(ln)

# print()

python_time = life_game(field)

# for ln in field:
#     print(ln)

# print(np_field)
# print()

numpy_time = life_game(np_field)

# print(np_field)

print(f"python time: {python_time}", f"numpy_time: {numpy_time}", sep="\n")