'''
Problema: Crear un diccionario con las calificaciones de 3 estudiantes 
y permitir que el usuario consulte la calificación de uno de ellos.
'''

# Diccionario con calificaciones de 3 estudiantes
calificaciones = {
    "Ana": 4.5,
    "Carlos": 3.8,
    "Elena": 4.9
}

# Solicitar el nombre del estudiante al usuario
estudiante = input("Ingrese el nombre del estudiante para consultar su calificación: ")

# Consultar la calificación con get() y manejar el caso si no existe
calificacion = calificaciones.get(estudiante, "El estudiante no está en el registro.")

# Mostrar el resultado
print(f"La calificación de {estudiante} es: {calificacion}" if estudiante in calificaciones else calificacion)
