import imageio as imgio #add imageio
import numpy as npy
from random import randint

values = npy.ndarray((16*3, 16*3, 3), dtype=npy.uint8)
print(values)
#Reset knowledge
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y][0] = randint(0, 255)
        values[x][y][1] = randint(0, 255)
        values[x][y][2] = randint(0, 255)

print(values)
img = imgio.imwrite('map.png', values)
