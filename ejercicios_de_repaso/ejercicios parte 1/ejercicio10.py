'
Problema: Crear un diccionario con algunos productos 
y permitir que el usuario agregue un nuevo producto con su precio.
''''''
''
# Diccionario con productos y precios
productos = {
    "Manzana": 1.5,
    "Banano": 0.8,
    "Leche": 2.3
}

# Solicitar al usuario un nuevo producto y su precio
nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
precio = float(input("Ingrese el precio del producto: "))

# Agregar al diccionario
productos[nuevo_producto] = precio

# Mostrar el diccionario actualizado
print("\nLista actualizada de productos y precios:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}")
