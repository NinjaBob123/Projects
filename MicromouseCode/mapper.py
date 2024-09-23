import imageio as imgio #add imageio # type: ignore
import numpy as npy
values = npy.ndarray('32x32x3')
img = imgio.imwrite('map.png', values)
