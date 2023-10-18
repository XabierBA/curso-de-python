"""Elabora un programa como se indica en los siguientes pasos:

Abre un archivo llamado output_exercise.txt en modo escritura e introduce dos líneas de texto:
    # Esta es la primera línea
    # Esto es la segunda línea

Abre el archivo en modo lectura e imprime sus contenidos en pantalla.

Abre el archivo en modo escritura sin reemplazar las líneas escritas anteriormente y 
escribe otra línea más (con lo que tú quieras poner).

Abre el archivo en modo lectura e imprime todos sus contenidos en pantalla."""

with open('archivo_prueba.txt', 'a+') as f:
    f.seek(0)
    f.write("Esto es la primera linea\n")
    f.write("Esto es la segunda linea\n")

    f.seek(0)
    print(f"Archivo mod 1 : \n{f.read()}")

    f.seek(0)
    f.write("'Con lo que tu quieras poner'")

    f.seek(0)
    print(f"Archivo mod 2 : \n{f.read()}")
