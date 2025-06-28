import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['door-closed.png', 'door-open.png']

images = []

target_size = (200, 200)
for filename in filenames:
    img = Image.open(filename).convert("RGB").resize(target_size)
    images.append(np.array(img))

iio.imwrite('door.gif', images, duration = 400, loop = 0)