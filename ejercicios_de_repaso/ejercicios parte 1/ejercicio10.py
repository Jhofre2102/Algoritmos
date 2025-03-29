'''
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
'''

productos = {"Manzana": 1.5, "Banano": 0.8, "Leche": 2.3}

producto = input("Ingrese el nombre del nuevo producto: ")
precio = float(input("Ingrese el precio: "))

productos[producto] = precio

print(productos)

