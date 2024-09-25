import imageio as imgio #add imageio
import numpy as npy
from random import randint

values = npy.ndarray((16*3, 16*3, 4), dtype=npy.uint8)
print(values)
#Reset knowledge
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y][0] = randint(0, 255)
        values[x][y][1] = randint(0, 255)
        values[x][y][2] = randint(0, 255)
        values[x][y][3] = 100
        print(f"({values[x][y][0]}, {values[x][y][1]}, {values[x][y][2]})")
img = imgio.imwrite('C:/Users/littl/OneDrive/Documents/Github/Projects/PNGMaker/custom.png', values)
