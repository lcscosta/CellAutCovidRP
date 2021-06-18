
import grid as g
import cells as c 

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
