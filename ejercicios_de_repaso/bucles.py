'''  
El bucle for es una expresión para el control del flujo usada en programación 
donde puedes definir el número de iteraciones en una parte del código.


for <iterador /contador> in <objeto_iterable>
para <el iterador>
'''

#ciclo for

#palabra="instituto" #podemos recorrer un string
#cantidad_de_letras=0
#for letra in palabra:
    #print(letra)
    #cantidad_de_letras+=1
#print(cantidad_de_letras)



mi_lista=[] # mi lista esta vacia
#for valor in range(1,10):
    #mi_lista.append(valor)


#mi_set=set()

#for numero in range (5,10):
 #   mi_set.add(numero)
    
#print(mi_set)

mi_diccionario={}
for elemento in range(1,5):
    mi_diccionario[str (elemento)]=elemento
print(mi_diccionario)

#Ejercicios de Control de Flujo y Bucles en Python
#Ejercicio 1: Contar Letras en una Palabra
''' 
palabra = input("Ingresa una palabra: ")  # Pedimos que ingrese una palabra
# Contamos cuántas letras tiene la palabra
total_letras = len(palabra)  
# Mostramos el resultado
print(f"La palabra '{palabra}' tiene {total_letras} letras.")  
'''

#Problemas:
#Solicitar al usuario una palabra y contar cuántas letras tiene.
#Ejercicio 2: Contar Vocales en una Cuerda

frase = input("Ingresa una frase: ")  # Solicitamos una frase
# Definimos las vocales
vocales = "aeiouAEIOU"  
# Contamos cuántas hay
total_vocales = sum(1 for letra in frase if letra in vocales)  
print(f"La frase tiene {total_vocales} vocales.")



#Problemas:
#Pedir una frase al usuario y contar cuántas vocales (a, e, i, o, u) tiene.
#Ejercicio 3: Buscar una Palabra en una Lista

lista_palabras = ["python", "java", "c++", "javascript", "ruby"]  # Lista predefinida
palabra_usuario = input("Ingresa una palabra para buscar: ")  # Pedimos una palabra
if palabra_usuario in lista_palabras:
    print(f"La palabra '{palabra_usuario}' está en la lista.")
else:
    print(f"La palabra '{palabra_usuario}' no está en la lista.")



#Problemas:
#Crea una lista de palabras predefinidas y pide al usuario una palabra. Indicar si está en la lista o no.
#Ejercicio 4: Contar Números Pares en una Lista


numeros = [int(input(f"Ingresa el número {i+1}: ")) for i in range(5)]  # Pedimos 5 números
pares = [num for num in numeros if num % 2 == 0]  # Filtramos los pares
print(f"Hay {len(pares)} números pares: {pares}")






#Problemas:
#Solicitar 5 números al usuario, almacenarlos en una lista y contar cuántos son pares.
#Ejercicio 5: Filtrar Palabras Cortas y Largas

#Problemas:
#Pedir al usuario 5 palabras y separar las que tienen más de 5 letras y las que tienen menos o igual.
#Ejercicio 6: Clasificar Números en Positivos y Negativos

#Problemas:
#Pedir 6 números al usuario y separarlos en positivos y negativos.
#Ejercicio 7: Contar Ocurrencias en una Lista

#Problemas:
#Pedir al usuario 7 números y contar cuántas veces aparece cada uno.
#Ejercicio 8: Diccionario de Notas y Promedio

#Problemas:
#Pedir 3 nombres de estudiantes y sus notas, guardarlas en un diccionario y calcular el promedio.
#Ejercicio 9: Encontrar la Palabra Más Larga

#Problemas:
#Pedir al usuario una lista de 4 palabras y encontrar la más larga.
#Ejercicio 10: Clasificación de Edades

#Problemas:
#Solicitar 5 edades y clasificarlas en menores de edad (0-17), adultos (18-64) y adultos mayores (65+)

