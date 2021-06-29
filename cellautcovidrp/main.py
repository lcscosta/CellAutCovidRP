'''
=========================================
    Cellular Automata Spreading Covid
=========================================
'''
import cities as ct
import cells as c
import grid as g
import iteration as it
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Teste Def

area = 651
pop = 711825

# Create Grid
grid = g.create_grid(area)

# Create cell list
cell = c.create_cellsmatrix(pop)

# Cell initial position
cell = c.cells_initialstatus(cell, pop)

# Cell random pos
cell = c.cells_randompos(cell, grid)

# read the position of cells e update cells matrix
grid_popdensity = g.suscept_positionupdate(cell, grid)

# grid_visualizer
#g.grid_visualization(grid_popdensity)

# include initial infected
cell = c.cells_initialinfected(cell, pop)

g.gvisualization(cell, grid, 200)

grid_popdensity = g.suscept_positionupdate(cell, grid)

g.grid_visualization(grid_popdensity)

ct.save_city('Batatais', grid_popdensity, cell )

cellsread = ct.read_city('Batatais', pop)


