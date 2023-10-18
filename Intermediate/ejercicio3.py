"""ENUNCIADO
Tienes una lista de estudiantes y sus calificaciones correspondientes. 
Tu tarea es imprimir el nombre de cada estudiante junto con su posición
en la lista y su calificación usando la funcion enumerate()."""

students = ["Pedro", "María", "Juan", "Ana"]
grades = [3, 10, 8, 5]

for i, students in enumerate(students):
        print(f"Estudiante {i}: {students}",f"|| Nota -> {grades[i]}\n")