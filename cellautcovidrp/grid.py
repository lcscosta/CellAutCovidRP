'''
=========================================
    Cellular Automata Grid
=========================================
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import cells as c
from tqdm import tqdm
from celluloid import Camera

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

def suscept_positionupdate(cells, grid):

    grid = np.zeros(grid.shape)

    for i in range(cells.shape[0]):
        if cells[i][2] == 1:
            x, y = int(cells[i][0]), int(cells[i][1])
            grid[x][y] += 1

    return grid

def infected_positionupdate(cells, grid):

    grid = np.zeros(grid.shape)

    for i in range(cells.shape[0]):
        if cells[i][2] == 2:
            x, y = cells[i][0], cells[i][1]
            grid[int(x)][int(y)] += 1

    return grid

def recupered_positionupdate(cells, grid):

    grid = np.zeros(grid.shape)

    for i in range(cells.shape[0]):
        if cells[i][2] == 3:
            x, y = cells[i][0], cells[i][1]
            grid[int(x)][int(y)] += 1

    return grid
    
def dead_positionupdate(cells, grid):

    grid = np.zeros(grid.shape)

    for i in range(cells.shape[0]):
        if cells[i][2] == 4:
            x, y = cells[i][0], cells[i][1]
            grid[int(x)][int(y)] += 1

    return grid


def count_data(cells, i):


    if i == 0 and os.path.isfile('data.txt') == True:
        os.remove('data.txt')

    w, x, y, z  = 0, 0, 0, 0
    for i in range(cells.shape[0]):
        if cells[i][2] == 1:
            w += 1
        elif cells[i][2] == 2:
            x += 1
        elif cells[i][2] == 3:
            y += 1
        elif cells[i][2] == 4:
            z += 1

    with open('data.txt', 'a') as f:
        f.write('{} {} {} {}\n'.format(w,x,y,z))

    data = np.zeros((i,4))

    j = 0
    with open('data.txt', 'r') as f:
        for line in f:
            parts = line.split(' ')
            data[j][0] = int(float(parts[0]))
            data[j][1] = int(float(parts[1]))
            data[j][2] = int(float(parts[2]))
            data[j][3] = int(float(parts[3]))

            j += 1

    return data

def grid_visualization(Grid):

    plt.matshow(Grid, cmap='Blues')
    plt.show(block=False)
    plt.pause(1)
    plt.close()

def grid_visualization_infection(cells, Grid):

    Grid_infection = infected_positionupdate(cells, Grid)
    plt.matshow(Grid_infection, cmap='Greens')
    plt.show(block=False)
    plt.pause(1)
    plt.close('all')

def gvisualization(cells, Grid, ix):

    fig, axes = plt.subplots(ncols=4, nrows=2)
    plt.ion()
    camera = Camera(fig)
    bar = tqdm(total=ix, position=0)
    for i in range(ix):

        cell = c.cells_positeration(cells, Grid)
        cell = c.cells_infectionspread(cells, Grid)

        data = count_data(cells,i)
        suscept, infect, recupered, death = data.T

        Grid = suscept_positionupdate(cells, Grid)
        Grid_infection = infected_positionupdate(cells, Grid)
        Grid_recupered = recupered_positionupdate(cells, Grid)
        Grid_death = dead_positionupdate(cells, Grid)

        axes[0][0].imshow(Grid, cmap='Blues')
        axes[0][1].imshow(Grid_infection, cmap='Reds')
        axes[0][2].imshow(Grid_recupered, cmap='Greens')
        axes[0][3].imshow(Grid_death, cmap='Greys')

        axes[1][0].plot(suscept[:i], 'o',color = 'blue' , lw = 0.8)
        axes[1][0].set_xlim([0, i])
        axes[1][1].plot(infect[:i], 'o',color = 'red' , lw = 0.8)
        axes[1][1].set_xlim([0,i])
        axes[1][2].plot(recupered[:i], 'o',color = 'green' , lw = 0.8)
        axes[1][2].set_xlim([0,i])
        axes[1][3].plot(death[:i], 'o',color = 'gray' , lw = 0.8)
        axes[1][3].set_xlim([0,i])

        bar.update()
        print(i)
        camera.snap()
    bar.close()

    animation = camera.animate()
    animation.save('test.gif', writer = 'imagemagick')

