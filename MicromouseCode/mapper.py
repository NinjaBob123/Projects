import imageio as imgio #add imageio
import numpy as npy
values = npy.ndarray((32, 32, 3))
img = imgio.imwrite('map.png', values)
