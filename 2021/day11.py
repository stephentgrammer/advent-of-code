input = """8548335644
6576521782
1223677762
1284713113
6125654778
6435726842
5664175556
1445736556
2248473568
6451473526"""

test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

import numpy as np
matrix = np.matrix(" ".join([c for c in input]).replace(" \n ", ";"))
rows, cols = matrix.shape
ones = np.full((rows, cols), 1)

total = 0

def flash(i, j):
    matrix[i, j] = 0
    num = 1
    ii = range(i,i+2) if i == 0 else range(i-1,i+1) if i == rows-1 else range(i-1,i+2)
    jj = range(j,j+2) if j == 0 else range(j-1,j+1) if j == rows-1 else range(j-1,j+2)

    for x in ii:
        for y in jj:
            z = matrix[x, y]
            if z != 0:
                matrix[x, y] += 1
            if z >= 9:
                num += flash(x, y)

    return num


steps = 0
while True:
    matrix += ones
    if np.array_equal(matrix, ones):
        print(steps)
        break
    steps += 1
    for idx, value in np.ndenumerate(matrix):
        if value == 10:
            total += flash(*idx)
    if steps == 100:
        print(total)
        # break

