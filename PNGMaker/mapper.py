import imageio as imgio #add imageio
import numpy as npy
values = npy.ndarray((16*3, 16*3, 3), dtype=npy.uint8)
print(values)
#Reset knowledge
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y][0] = 0
        values[x][y][1] = 0
        values[x][y][2] = 0
#if left sensor shows < 5cm distance, then color left pixel red
height = 0
width = 0
leftSensor = 5
if leftSensor <= 5:
    values[height][width][0] = 255
    values[height][width][1] = 0
    values[height][width][2] = 0
print(values)
img = imgio.imwrite('map.png', values)
