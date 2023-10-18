"""
#ENUNCIADO
Representa las funciones seno, coseno y tangente en una misma gráfica en un rango de valores de 0 a 10 
con la precisión que desees. Cada una de ellas deberá tener un nombre y color distintivos, 
mostrados en la leyenda. La gráfica deberá tener un título descriptivo."""




import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)

#Función seno
plt.plot(x,s,"r",label="Seno")

#Función coseno
plt.plot(x,c,"b",label="Coseno")

#Función tangente
plt.plot(x,t,"m",label="Tangente")


plt.title("Graphic functions")
plt.grid(True)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()

plt.show()
