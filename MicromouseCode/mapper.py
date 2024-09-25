import imageio as imgio #add imageio
import numpy as npy
values = npy.ndarray((16*3, 16*3, 3), dtype=npy.uint8)
print(values)
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y][0] = 0
        values[x][y][1] = 0
        values[x][y][2] = 0
print(values)
img = imgio.imwrite('map.png', values)
