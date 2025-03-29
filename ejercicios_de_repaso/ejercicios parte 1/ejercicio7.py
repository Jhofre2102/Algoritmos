'''
Problema: Almacenar los nombres de 3 ciudades en una tupla y luego mostrar:

    La primera y la última ciudad.

    La cantidad de caracteres de cada ciudad.
'''
# Almacenar los nombres de 3 ciudades en una tupla
ciudades = ("Bogotá", "Madrid", "Tokio")

# Mostrar la primera y la última ciudad
print("Primera ciudad:", ciudades[0])
print("Última ciudad:", ciudades[-1])

# Mostrar la cantidad de caracteres de cada ciudad
print("\nCantidad de caracteres por ciudad:")
for ciudad in ciudades:
    print(f"{ciudad}: {len(ciudad)} caracteres")
