#  Script to generate the cell coordinates
#  for which we are going to calculate
#  the neighbor list.

# Inports:
import numpy as np

# Inputs:
size = [1,1,1]       # Number of times we are replicating the primitive cell
center = [0,0,0]     # The position (x,y,z) in space where the ceneter is
primitive_cell = [[4,0,0],[0,4,0],[0,0,4]] # The primitive cell

cell_coords = np.array(list((it.product(np.arange(size[0]),
                                        np.arange(size[1]),
                                        np.arange(size[2])))))
cell_coords_centered = cell_coords + center
cell_coords_centered = np.dot(cell_coords_centered, primitive_cell)

# return the cells coordinates generated
print(cell_coords_centered)
