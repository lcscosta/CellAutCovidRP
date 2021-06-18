'''
===============================
    Cell Functions
===============================
'''

import numpy as np

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

def create_cellsmatrix(Population, Pop_ratio=1):
    #   Create a Matrix
    #   pos x, pos y, condition

    Population = Population*Pop_ratio
 
    cells = np.zeros((Population, 3))

    cells = cells_initialstatus(cells, Population, Pop_ratio)

    return cells

