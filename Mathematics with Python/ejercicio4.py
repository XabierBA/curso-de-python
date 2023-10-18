"""
#ENUNCIADO
Grafica la función seno en el intervalo [0, 2π] con una precisión de 0.1 (saltos de 0.1 en 0.1).
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
f = np.sin(x)

plt.plot(x,f,"r")
plt.plot(x,f,":")
plt.title("Graphic sin")
plt.grid(True)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend("LP")

plt.show()
