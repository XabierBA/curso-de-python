"""
#ENUNCIADO
Crea 3 arrays de numpy a partir de las siguientes listas y comprueba su tipo de dato:
    # list1 = [1, 2, 3, 4, 5]
    # list2 = [1, 2, 3, 4, 5.0]
    # list3 = [1, 2, 3, 4, 'a']
"""

import numpy as np

list1 = np.array([1, 2, 3, 4, 5])
print(f"Tipo de dato lista 1 : {list1.dtype}\n")

list2 = np.array([1, 2, 3, 4, 5.0])
print(f"Tipo de dato lista 2 : {list2.dtype}\n")

list3 = np.array([1, 2, 3, 4, 'a'])
print(f"Tipo de dato lista 3 : {list3.dtype}")
