"""
#ENUNCIADO
En este ejercicio se llevará a cabo la representación en dos dimensiones del circuito de Nürburgring. 
La imagen en 2D adjunta en este enlace debería parecerse bastante a la producida en el programa. 
En dicha representación deberán diseñarse dos líneas, una que represente la parte derecha de la pista 
y otra que represente la parte izquierda.

Se va a suponer que por dicho circuito tiene que competir un coche autónomo, por ejemplo, el UM24. 
Para que esto sea posible, es necesario que la línea de la derecha se represente por medio de conos 
(o símbolos que se le parezcan) de color amarillo. La parte izquierda debe ser igual, pero con conos azules.

Dichos conos serán representados por coordenadas bidimensionales, que deberán ser localizadas en dos 
arrays independientes para poder ser diferenciadas. Asimismo, deberán ser nombradas como Límite derecho y 
Límite izquierdo.

Posteriormente se deberán calcular las posiciones intermedias entre los conos, tomar una muestra de 
puntos de las mismas y proceder al cálculo de una ruta que recorra el circuito sin salirse de los límites 
del mismo (de la forma que se quiera, más o menos optimizada).

La línea trazada deberá ser verde y continua (sin representación de puntos intermedios). 
Deberá ser nombrada como Trazada intermedia.

El resultado final del ejercicio debe ser la representación en 2 dimensiones de las tres líneas, 
con sus respectivos nombres mostrados en pantalla y un título que describa adecuado el proceso realizado.
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

# Function that reads the file where the coordinates of the Nurburgring circuit are
def read_coords(nombre_archivo):
    x_values = []
    y_values = []
    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            x = float(fila['x_m'])
            y = float(fila['y_m'])
            x_values.append(x)
            y_values.append(y)
    return np.array(x_values), np.array(y_values)

# Function that calculates the left limit of the track
def left_offset(x, y, distancia):
    #Calculate displacement vectors to create parallel traces
    dx = np.gradient(x)
    dy = np.gradient(y)
    norm = np.sqrt(dx**2 + dy**2)
    dx = dx / norm
    dy = dy / norm

    # Calculate parallel coordinates
    x_left = x + distancia * dy
    y_left = y - distancia * dx

    return x_left, y_left

# Function that calculates the right limit of the track
def right_track(x, y, distancia):
    # Calculate displacement vectors to create parallel traces
    dx = np.gradient(x)
    dy = np.gradient(y)
    norm = np.sqrt(dx**2 + dy**2)
    dx = dx / norm
    dy = dy / norm

    # Calculate parallel coordinates
    x_right = x + distancia * dy
    y_right = y - distancia * dx

    return x_right, y_right

# Name of the CSV file containing the coordinates
archivo_coord = "nurburgring.csv"

# Read 'x' and 'y' coordinates from CSV file and save them to separate NumPy arrays
x_mid, y_mid = read_coords(archivo_coord)

# Distance to trace parallel lines(Variables can be changed)
offset1 = 10.0
offset2 = -10.0

# Get left limit of the track (Blue cones)
x_left, y_left = left_offset(x_mid, y_mid, offset1)


# Get right limit of the track (Yellow cones)
x_right, y_right = right_track(x_mid, y_mid, offset2)


# Representation of the track limits
plt.plot(x_right, y_right, c="yellow", linestyle=":", label="Right Limit (Yellow cones)")
plt.plot(x_left, y_left, c="blue", linestyle=":", label="Left Limit (Blue cones)")

# Representation of the path of the autonomous car
plt.plot(x_mid, y_mid, c="g", label="Path")

plt.xlabel('Coord x')
plt.ylabel('Coord y')
plt.title('Nurburgring circuit path planing')
plt.legend()
plt.grid(False)
plt.show()