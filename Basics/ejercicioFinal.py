"""ENUNCIADO

La representación de un cuaternión puede ser utilizada para describir una 
rotación en el espacio tridimensional. Es común convertir entre cuaterniones y 
ángulos de Euler (rotaciones alrededor de ejes individuales) en aplicaciones 
como la robótica y gráficos por computadora.

Esto se utiliza mucho al trabajar con orientaciones. 
Diseña una clase llamada Quaternions que facilite la transformación y manipulación de orientaciones:

MÉTODOS
    # Constructor: Debe aceptar cuatro argumentos float (en el orden w, x, y, z) que representen 
    los coeficientes del cuaternión.
    # Getters y Setters
    # Conversión de cuaternión a ángulos de Euler

CONVERSIÓN DE CUATERNIÓN A ÁGULOS DE EULER
    # El método debe devolver:

    # value0: Roll value.
    # value1: Pitch value.
    # value2: Yaw value.
"""
import math as mh

class Quaternions:

    def __init__(self, w, x, y, z):
            self.__w = w
            self.__x = x
            self.__y = y
            self.__z = z

    #GETTERS AND SETTERS
    @property
    def w(self) -> float:
          return self.__w  
    @w.setter
    def w(self, w:float) -> None:
          self.__w = w

    @property
    def x(self) -> float:
          return self.__x
    @x.setter
    def x(self, x:float) -> None:
          self.__x = x

    @property
    def y(self) -> float:
          return self.__y 
    @y.setter
    def y(self, y:float) -> None:
          self.__y = y

    @property
    def z(self) -> float:
        return self.__z
    @z.setter
    def z(self, z:float) -> None:
          self.__z = z

    
      
    def pitch(self):
        # Calculate pitch (x-axis rotation)
        sinP = 2 * (self.w * self.y - self.x * self.z)
        return mh.asin(sinP)

    def yaw(self):
        # Calculate yaw (z-axis rotation)
        sinY = 2.0 * (self.w * self.z + self.x * self.y)
        cosY = 1.0 - (2.0 * (self.z * self.z + self.y * self.z))
        return mh.atan2(sinY, cosY)

    def roll(self):
        # Calculate roll (y-axis rotation)
        sinR = 2.0 * (self.w * self.x + self.y * self.z)
        cosR = 1.0 - (2.0 * (self.x * self.x + self.y * self.y))
        return mh.atan2(sinR, cosR)




quat = Quaternions(1,2,3,4) 

print("EULER ANGELES IN RADIANS:")
print(f" Value0(Roll): {quat.roll()}\n",
      f"Value1(Pitch): {quat.pitch()}\n",
      f"Value2(Yaw): {quat.yaw()}\n")
