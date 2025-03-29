'''Problema: Solicitar al usuario dos conjuntos de números y luego mostrar:

    La unión de ambos conjuntos.

    La intersección de ambos conjuntos'''
    
    # Solicitar dos conjuntos de números al usuario
conjunto1 = set(map(int, input("Ingrese los números del primer conjunto separados por espacios: ").split()))
conjunto2 = set(map(int, input("Ingrese los números del segundo conjunto separados por espacios: ").split()))

# Calcular la unión e intersección
union = conjunto1 | conjunto2  # También se puede usar conjunto1.union(conjunto2)
interseccion = conjunto1 & conjunto2  # También se puede usar conjunto1.intersection(conjunto2)

# Mostrar los resultados
print("\nUnión de ambos conjuntos:", union)
print("Intersección de ambos conjuntos:", interseccion)
