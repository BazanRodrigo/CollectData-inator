import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

os.chdir('tmp')
dir = sorted(np.asanyarray(os.listdir()))
print(dir)

for imagenes in dir:
    print(imagenes)
    #imagenes = np.asarray(imagenes)
    print(np.asanyarray(imagenes))
    #plt.imshow(imagenes)
    #plt.show()
    img = Image.open(imagenes)
    img.show()
    print("Te sirve?")
    fs = input()

