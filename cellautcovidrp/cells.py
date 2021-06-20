'''
===============================
    Cell Functions
===============================
'''

import numpy as np
import random

def cells_initialstatus(cells, Population, Pop_ratio=1):
    Population = Population*Pop_ratio
    for i in range(Population):
        cells[i][2] = 1
    return cells

def cells_randompos(cells, grid):
    ''' A function for creation of a grid'''

    for i in range(cells.shape[0]):
        x = np.random.randint(len(grid[0]))
        y = np.random.randint(len(grid[0]))

        cells[i][0], cells[i][1] = x, y

    return cells

def cells_positeration(cells, grid):
    xlim = grid.shape[0]-1
    ylim = grid.shape[1]-1

    for i in range(cells.shape[0]):
        x, y = cells[i][0], cells[i][1]

        if x != 0 and y != 0 and x != xlim and y != ylim:
            xinc, yinc = random.randint(-1,1), random.randint(-1,1)
        else:
            if x == 0 and y == 0:
                xinc, yinc = random.randint(0,1), random.randint(0,1)
            if x == 0 and y == ylim:
                xinc, yinc = random.randint(0,1), random.randint(-1,0)
            if x == 0 and y != 0 and y != ylim:
                xinc, yinc =  random.randint(0,1), random.randint(-1,1)
            if x == xlim and y == 0:
                xinc, yinc = random.randint(-1,0), random.randint(0,2)
            if x == xlim and y == ylim:
                xinc, yinc = random.randint(-1,0), random.randint(-1,0)
            if x == xlim and y != 0 and y != ylim:
                xinc, yinc =  random.randint(-1,0), random.randint(-1,1)
            if y == 0 and x != 0 and x != ylim:
                xinc, yinc = random.randint(-1,1), random.randint(0,1)
            if y == ylim and x != 0 and x != ylim:
                xinc, yinc = random.randint(-1,1), random.randint(-1,0)

        cells[i][0], cells[i][1] = x + xinc, y + yinc

    return cells

def create_cellsmatrix(Population, Pop_ratio=1):
    #   Create a Matrix
    #   pos x, pos y, condition

    Population = Population*Pop_ratio

    cells = np.zeros((Population, 3))

    cells = cells_initialstatus(cells, Population, Pop_ratio)

    return cells

