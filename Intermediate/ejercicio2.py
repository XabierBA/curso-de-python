"""ENUNCIADO
# Crea una clase llamada Calculadora que reciba dos números enteros como parámetros en su constructor. 
# Esta clase debe tener los siguientes métodos:
    # Suma
    # Resta
    # Multiplicación
    # División
    # Comparación

# Recuerda manejar las excepciones."""

class Calculadora:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    # GETTER Y SETTER DE N1
    @property
    def n1(self):
        return self.__n1
    @n1.setter
    def n1(self, v):
        self.__n1 = v

    #GETTER Y SETTER DE N2
    @property
    def n2(self):
        return self.__n2
    @n2.setter
    def n2(self, v):
        self.__n2 = v

    #METODO SUMA
    def __add__(self,otro):
        res = (self.n1 + otro.n1, self.n2 + otro.n2)
        return res
    
    #METODO RESTA
    def __sub__(self,otro):
        res = (self.n1 - otro.n1, self.n2 - otro.n2)
        return res
    
    #METODO MULTIPLICACIÓN
    def __mul__(self,otro):
        res = (self.n1 * otro.n1, self.n2 * otro.n2)
        return res
    
    #METODO DIVISIÓN
    def __truediv__(self,otro):
        if(otro.n1==0 or otro.n2==0):
            raise ValueError("El divisor no puede ser 0")
        res = (self.n1 / otro.n1, self.n2 / otro.n2)
        return res
    

    

cal1 = Calculadora(4,5)
cal2 = Calculadora(5,4)

print(f"Suma -> {cal1 + cal2}")
print(f"Resta -> {cal1 - cal2}")
print(f"Multiplicación -> {cal1 * cal2}")
print(f"División -> {cal1 / cal2}")

