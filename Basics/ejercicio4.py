"""ENUNCIADO
Usando un bucle for imprime los números del 0 al 100 en saltos de 3 en 3."""

#Metodo malo
veces = 100
for i in range(veces):
    while i%3 == 0:
        print(f"Número {i}")
        break

#Metodo facil
for i in range(0,veces,3):
    print(f"Número: {i}")
    