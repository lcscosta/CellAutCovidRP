'''
=========================================
    Cellular Automata Grid
=========================================
'''

import numpy as np
import matplotlib.pyplot as plt

def create_grid(Area, Area_ratio = 100):
    ''' A function for creation of a grid'''
    
    # Area ratio
    # 1 km^2 -> 100 (100m^2)

    # number of grid divisions
    gridcounts = Area * Area_ratio

    # grid side 
    gridside = int(np.sqrt(gridcounts))

    # create Matrix
    grid = np.zeros((gridside,gridside))

    return grid

def positionupdate(cells, grid):

    for i in range(cells.shape[0]):
        x, y = int(cells[i][0]), int(cells[i][1])
        grid[x][y] += 1
    
    return grid

def disease_positionupdate(cells, grid, Population):

    for i in range(len(cells[0])):
        x, y = cells[i][0], cells[i][1]
        if grid[x][y] == 0 and cells[i][2] == 1:
            grid[x][y] = 1
        elif grid[x][y] == 0 and cells[i][2] == 2:
            grid[x][y] = 2
        else:
            pass

    return grid

def grid_visualization(Grid):
    plt.matshow(Grid)
    plt.show()
