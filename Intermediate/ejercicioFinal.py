"""ENUNCIADO

Con tus nuevos conocimietos utiliza todos los elementos que creas necesarios para mejorar 
la clase Quaternions del ejercicio final del módulo anterior del curso.

Obligatoriamente debes usar al menos un método especial (sin incluir el constructor) 
y anotaciones de tipo.
      
Por último debes llamar a esta clase en un módulo distinto."""

import math as mh

class Quaternions:

    def __init__(self, w: float, x: float, y: float, z: float):
        # Normalize the quaternion
        norm = mh.sqrt(w**2 + x**2 + y**2 + z**2)
        if norm == 0:
            raise ValueError("Quaternion norm is zero")
        self.__w = w / norm
        self.__x = x / norm
        self.__y = y / norm
        self.__z = z / norm

    # GETTERS AND SETTERS
    @property
    def w(self) -> float:
        return self.__w

    @w.setter
    def w(self, w: float) -> None:
        self.__w = w

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float) -> None:
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float) -> None:
        self.__y = y

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, z: float) -> None:
        self.__z = z

    def pitch(self) -> float:
        # Calculate pitch (x-axis rotation)
        sinP = 2 * (self.w * self.y - self.x * self.z)
        return mh.asin(sinP)
    def yaw(self) -> float:
        # Calculate yaw (z-axis rotation)
        sinY = 2.0 * (self.w * self.z + self.x * self.y)
        cosY = 1.0 - (2.0 * (self.z * self.z + self.y * self.z))
        return mh.atan2(sinY, cosY)

    def roll(self) -> float:
        # Calculate roll (y-axis rotation)
        sinR = 2.0 * (self.w * self.x + self.y * self.z)
        cosR = 1.0 - (2.0 * (self.x * self.x + self.y * self.y))
        return mh.atan2(sinR, cosR)

    def __str__(self) -> str:
        return f"Quaternion(w={self.w}, x={self.x}, y={self.y}, z={self.z})"

quat = Quaternions(1, 2, 3, 4)

print("EULER ANGLES IN RADIANS:")
print(f"{quat}\n")
print(f"Value0(Roll): {quat.roll()}\n",
      f"Value1(Pitch): {quat.pitch()}\n",
      f"Value2(Yaw): {quat.yaw()}\n")