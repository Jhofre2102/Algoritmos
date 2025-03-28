'''
Problema: Escribe un programa que verifique si una palabra ingresada por el usuario está 
en la siguiente frase:
"Python es un lenguaje de programación poderoso".
'''
# Frase dada
frase="Python es un lenguaje de programación poderoso"

# Solicitar palabra al usuario
palabra=input("Ingrese una palabra para buscar en la frase: ")

# Verificar si la palabra está en la frase (sin diferenciar mayúsculas y minúsculas)
if palabra.lower() in frase.lower():
    print("La palabra está en la frase.")
else:
    print("La palabra NO está en la frase.")
