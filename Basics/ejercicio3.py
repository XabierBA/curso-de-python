"""#ENUNCIADO
#Dadas las siguientes coordenadas que representan puntos, 
# calcula el módulo del vector que forman (longitud del segmento)."""


point_1 = (0, 1)
point_2 = (1, 1)

mod = (((point_2[0] - point_1[0])**2 + (point_2[1]-point_1[1])**2)**0.5)

print(f"Modulo {mod}")