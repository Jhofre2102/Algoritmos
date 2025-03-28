'''
Problema: Escribe un programa que determine si un número ingresado por el 
usuario es par o impar utilizando el operador módulo %.
'''
# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Verificar si es par o impar usando el operador módulo
if numero % 2 == 0:
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")
