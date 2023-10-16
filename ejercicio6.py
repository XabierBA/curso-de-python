# ENUNCIADO
# Privatiza los atributos de la clase Triangle y crea mediante propiedades los métodos
# getters y setters para acceder a ellos.

class Triangle:
        def __init__(self, base, altura):
            self.__base = base
            self.__altura = altura
        
        #Setter y Getter de base
        @property
        def base(self) -> float:
             return self.__base  
        
        @base.setter
        def base(self, base:float) -> None:
             self.__base = base
  
        
        #Setter y Getter de altura
        @property
        def altura(self) -> float:
             return self.__altura 
        
        @altura.setter
        def altura(self, altura:float) -> None:
             self.__altura = altura  
             

        def area(self):
            return 0.5 * self.base * self.altura
        

triangle = Triangle(10, 5)
print(triangle.area())