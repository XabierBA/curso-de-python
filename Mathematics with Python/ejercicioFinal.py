"""
#ENUNCIADO
En este ejercicio se llevará a cabo la representación en dos dimensiones del circuito de Nürburgring. 
La imagen en 2D adjunta en este enlace debería parecerse bastante a la producida en el programa. 
En dicha representación deberán diseñarse dos líneas, una que represente la parte derecha de la pista 
y otra que represente la parte izquierda.

Se va a suponer que por dicho circuito tiene que competir un coche autónomo, por ejemplo, el UM24. 
Para que esto sea posible, es necesario que la línea de la derecha se represente por medio de conos 
(o símbolos que se le parezcan) de color amarillo. La parte izquierda debe ser igual, pero con conos azules.

Dichos conos serán representados por coordenadas bidimensionales, que deberán ser localizadas en dos 
arrays independientes para poder ser diferenciadas. Asimismo, deberán ser nombradas como Límite derecho y 
Límite izquierdo.

Posteriormente se deberán calcular las posiciones intermedias entre los conos, tomar una muestra de 
puntos de las mismas y proceder al cálculo de una ruta que recorra el circuito sin salirse de los límites 
del mismo (de la forma que se quiera, más o menos optimizada).

La línea trazada deberá ser verde y continua (sin representación de puntos intermedios). 
Deberá ser nombrada como Trazada intermedia.

El resultado final del ejercicio debe ser la representación en 2 dimensiones de las tres líneas, 
con sus respectivos nombres mostrados en pantalla y un título que describa adecuado el proceso realizado.
"""