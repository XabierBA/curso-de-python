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
    @w.setter
    def x(self, x:float) -> None:
          self.__x = x

    @property
    def y(self) -> float:
          return self.__y 
    @w.setter
    def y(self, y:float) -> None:
          self.__y = y

    @property
    def z(self) -> float:
        return self.__z
    @z.setter
    def z(self, z:float) -> None:
          self.__z = z

    def conversion(self):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (self.w * self.x + self.y * self.z)
        t1 = +1.0 - 2.0 * (self.x * self.x + self.y * self.y)
        roll = mh.atan2(t0, t1)
     
        t2 = +2.0 * (self.w * self.y - self.z * self.x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch = mh.asin(t2)
     
        t3 = +2.0 * (self.w * self.z + self.x * self.y)
        t4 = +1.0 - 2.0 * (self.y * self.y + self.z * self.z)
        yaw = mh.atan2(t3, t4)
     
        return roll, pitch, yaw # in radians

quat = Quaternions(1,2,3,4)

print(f"Euler angle: {quat.conversion()[1]}\n")
print(f" Value0: {quat.conversion()[0]}\n",
      f"Value1: {quat.conversion()[1]}\n",
      f"Value2: {quat.conversion()[2]}\n")
