'''
Ejercicio 1: Operadores Aritméticos

Problema: Escribe un programa que solicite al usuario dos números y 
realice las operaciones de suma, resta, multiplicación, división y módulo.

'''
# Solicitar dos números al usuario
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))

# Operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"
modulo = num1 % num2 if num2 != 0 else "No se puede calcular el módulo con cero"

# Mostrar resultados
print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Módulo: {modulo}")

