# ENUNCIADO
# Crea una función validar_edad a la cuál se le pase como argumento la edad y 
# en caso de que sea menor de 0 lance una excepción con el mensaje "La edad no puede ser negativa". 
# Posteriormente llama a la función con un valor negativo y captura la excepción.

def validar_edad(edad):
    if(edad < 0):
        raise ValueError("La edad no puede ser negativa")


try:
    validar_edad(-2)
except ValueError as error:
    print(f"Error {error}")
