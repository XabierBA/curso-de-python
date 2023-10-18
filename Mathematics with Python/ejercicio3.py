"""
#ENUNCIADO
Por defecto los enteros en Python son de 32 bits.Crea un array de dos dimensiones con 5 columnas
y 3 filas de enteros de 16 bits.
"""

import numpy as np

array16 = np.array([[1, 4, 7, 10, 13],
                    [2, 5, 8, 11, 14],
                    [3, 6, 9, 12, 15]], dtype=np.int16)

print(array16)

print(f"Tipo de dato de Array16 : {array16.dtype}")
