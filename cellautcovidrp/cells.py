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

def cells_initialinfected(cells, Population, Pop_ratio=1):
    Population = Population*Pop_ratio
    randomcell = np.random.randint(Population)

    cells[randomcell][2] = 2

    return cells

def cells_infectionspread(cells, grid):

    xlim = grid.shape[0]-1
    ylim = grid.shape[1]-1

    for i in range(cells.shape[0]):

        if cells[i][2] == 2:
            x, y = cells[i][0], cells[i][1]

            if x != 0 and y != 0 and x != xlim and y != ylim:
                xlist, ylist = [x-1,x,x+1],[y-1,y,y+1]
            else:
                if x == 0 and y == 0:
                    xlist, ylist = [x,x+1], [y,y+1]
                if x == 0 and y == ylim:
                    xlist, ylist = [x,x+1], [y-1,y]
                if x == 0 and y != 0 and y != ylim:
                    xlist, ylist =  [x,x+1], [y-1,y,y+1]
                if x == xlim and y == 0:
                    xlist, ylist = [x-1,x], [y,y+1]
                if x == xlim and y == ylim:
                    xlist, ylist = [x-1,x], [y-1,y]
                if x == xlim and y != 0 and y != ylim:
                    xlist, ylist =  [x-1,x], [y-1,y,y+1]
                if y == 0 and x != 0 and x != ylim:
                    xlist, ylist = [x-1,x,x+1], [y,y+1]
                if y == ylim and x != 0 and x != ylim:
                    xlist, ylist = [x-1,x,x+1], [y-1,y]

            for j in range(len(xlist)):
                for k in range(len(ylist)):
                    for ii in range(cells.shape[0]):
                        if cells[ii][0] == xlist[j] and cells[ii][1] == ylist[k] and cells[ii][2] == 1:
                            infect = np.random.randint(0,100)
                            if infect > 91:
                                cells[ii][2] = 2
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

        if cells[i][2] == 4:
            pass
        else:

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
                    xinc, yinc = random.randint(-1,0), random.randint(0,1)
                if x == xlim and y == ylim:
                    xinc, yinc = random.randint(-1,0), random.randint(-1,0)
                if x == xlim and y != 0 and y != ylim:
                    xinc, yinc =  random.randint(-1,0), random.randint(-1,1)
                if y == 0 and x != 0 and x != ylim:
                    xinc, yinc = random.randint(-1,1), random.randint(0,1)
                if y == ylim and x != 0 and x != ylim:
                    xinc, yinc = random.randint(-1,1), random.randint(-1,0)

            if cells[i][2] == 2:
                cells[i][3] += 1
                if cells[i][3] == 12:
                    cells[i][2] = cells_finalstage()

            cells[i][0], cells[i][1] = x + xinc, y + yinc

    return cells

def cells_finalstage():
    death_rate = 0.035
    death_rate = death_rate * 1000
    x = random.randint(0,1000)

    if x < death_rate:
        return 4
    else:
        return 3

def create_cellsmatrix(Population, Pop_ratio=1):
    #   Create a Matrix
    #   pos x, pos y, condition

    Population = Population*Pop_ratio

    cells = np.zeros((Population, 4))

    cells = cells_initialstatus(cells, Population, Pop_ratio)

    return cells

