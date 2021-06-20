'''
=========================================
    Cellular Automata Spreading Covid
=========================================
'''
import cities as ct
import cells as c
import grid as g
import iteration as it


# Teste Def 

area = 1
pop = 100

# Create Grid
grid = g.create_grid(area)
print(grid)

# Create cell list
cell = c.create_cellsmatrix(pop)

# Cell initial position
cell = c.cells_initialstatus(cell, pop)

# Cell random pos
cell = c.cells_randompos(cell, grid)

# read the position of cells e update cells matrix
grid_popdensity = g.positionupdate(cell, grid)

# grid_visualizer
g.grid_visualization(grid_popdensity)

i = 0
while i < 101:
    cell = c.cells_positeration(cell, grid)
    print(i)
    i = i+1

grid_popdensity = g.positionupdate(cell, grid)

g.grid_visualization(grid_popdensity)

ct.save_city('Batatais', grid_popdensity, cell )

cellsread = ct.read_city('Batatais', pop)

print(cellsread)

