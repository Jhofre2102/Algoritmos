'''
Problema: Solicitar al usuario 5 números enteros, almacenarlos en una lista y luego mostrar:

    La lista original.

    La lista en orden inverso.

    La suma de los números.
'''

# Crear una lista vacía para almacenar los números
numeros = []

# Solicitar 5 números enteros al usuario
for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Mostrar la lista original
print("\nLista original:", numeros)

# Mostrar la lista en orden inverso
print("Lista en orden inverso:", numeros[::-1])

# Calcular y mostrar la suma de los números
print("Suma de los números:", sum(numeros))
