
import grid as g
import cells as c
import numpy as np

def create_malha():
    return


def create_city(cityname, Population, Area, Pop_ratio=1, Area_ratio=100):
    # first create city_grid and city_cellsmatrix
    grid = g.create_grid(Area, Area_ratio)
    cellsmatrix = c.create_cellsmatrix(Population)

    # random position of cells
    cellsmatrix = c.cells_randompos(cellsmatrix, grid)

    # read the position of cells e update cells matrix
    grid_popdensity = g.positionupdate(cellsmatrix, grid)

    # grid_visualizer
    g.grid_visualization(grid_popdensity)

    return grid, cellsmatrix


def save_city(cityname, grid, cellsmatrix):

    with open(cityname + '.txt', 'w') as f:
        for i in range(cellsmatrix.shape[0]):
            f.write('{} {} {} \n'.format(cellsmatrix[i][0],cellsmatrix[i][1],cellsmatrix[i][2]))

    return print( cityname + ' saved data')

def read_city(cityname, Population, Pop_ratio=1):

    cells = np.zeros((Population,3))
    i =0
    with open(cityname + '.txt', 'r') as f:
        for line in f:
            parts = line.split(' ')
            cells[i][0] = int(float(parts[0]))
            cells[i][1] = int(float(parts[1]))
            cells[i][2] = int(float(parts[2]))

            i = i + 1

    return cells
