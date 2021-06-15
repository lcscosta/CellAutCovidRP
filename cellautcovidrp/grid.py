'''
=========================================
    Cellular Automata Grid
=========================================
'''

import numpy as np
import matplotlib.pyplot as plt

def grid_creation(Area, Popratio=1, Arearatio = 100):
    ''' A function for creation of a grid'''
    
    # Area ratio
    # 1 km^2 -> 100 (100m^2)

    # number of grid divisions
    gridcounts = Area * 100

    # grid side 
    gridside = int(np.sqrt(gridcounts))

    # create Matrix
    grid = np.zeros((gridside,gridside))

    return grid

def pop_random(Grid, Population, Popratio=1):
    ''' A function for creation of a grid'''

    # Pop = Population*Popratio

    Population = Population*Popratio
    
    for i in range(Population):
        x = np.random.randint(len(Grid[0]))
        y = np.random.randint(len(Grid[0]))
        
        Grid[x][y] += 1

    return Grid

def grid_visualization(Grid):
    plt.matshow(Grid)
    plt.show()
