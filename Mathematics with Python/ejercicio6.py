"""
#ENUNCIADO
Sabiendo que la imagen del ejemplo anterior tiene 3 canales de color, mostrar tres descomposiciones 
de la misma en pantalla. En cada una de ellas deben verse solo los canales rojo, verde y azul, 
respectivamente.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

img = misc.face() # Imagen para pruebas que ofrece SciPy

red_channel = img.copy()
red_channel[:,:,1]=0
red_channel[:,:,2]=0
plt.title("Canal Rojo")
plt.imshow(red_channel)
plt.figure()


green_channel = img.copy()
green_channel[:,:,0]=0
green_channel[:,:,2]=0
plt.title("Canal Rojo")
plt.imshow(green_channel)
plt.figure()


blue_channel = img.copy()
blue_channel[:,:,0]=0
blue_channel[:,:,1]=0
plt.title("Canal Rojo")
plt.imshow(blue_channel)
plt.show()
