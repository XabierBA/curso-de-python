"""ENUNCIADO:
Crea tres variables (nómbralas de una forma correcta) que contengan los siguientes datos:
   -Una tupla con un rango de números
   -Una lista con todos los datos básicos.
   -Un set con los booleanos True, True, False.
   -Un diccionario con 3 pares clave-valor cuyos valores sean tres tipos de datos avanzados diferentes.
Imprime por pantalla los datos y razona el resultado."""

ej_tupla = (range(1, 50))

ej_lista = [10,"Hola mundo",False,3.14,(4, 5)]

ej_set={"True", "True", "False"}

ej_diccionario = {"Tupla1": (range(1, 2)),
                  "Lista1": [1,2,3,4],
                  "Set1":{"True", "False"}
                  }


print(f"Tupla: {ej_tupla}\n" , 
      f"Lista: {ej_lista}\n",
      f"Set: {ej_set}\n",
      f"Diccionario: {ej_diccionario}\n")