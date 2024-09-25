import imageio as imgio #add imageio
import numpy as npy
from random import randint

width = input("How wide do you want the image to be in pixels?: ")
height = input("How tall do you want the image to be in pixels?: ")
values = npy.ndarray((int(width), int(height), 4), dtype=npy.uint8)
print(values)
#Reset knowledge
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y][0] = randint(0, 255)
        values[x][y][1] = randint(0, 255)
        values[x][y][2] = randint(0, 255)
        values[x][y][3] = 100
        print(f"({values[x][y][0]}, {values[x][y][1]}, {values[x][y][2]})")
img = imgio.imwrite('./custom.png', values)
