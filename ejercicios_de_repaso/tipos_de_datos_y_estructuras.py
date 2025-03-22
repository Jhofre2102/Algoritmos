'''
<class 'int'>: identifica que la variable es un entero
<class 'float'>: identifica que la variable es un numero decimal
<class 'str'>: identifica que la variable es una cadena de texto
<class 'bool'>: identifica que la variable es un valor true o false (boolean)
'''

x=True #True y False son palabras reservadas del lenguage
print(type(x))

autor='andres'
print(type(autor))
carro="This is andres' car: "
modelo='1999'
print(carro + modelo)#el simbolo + permite concatenar textos en python


'''
Tipos de estructura de datos y 

1. Conjuntos ++
2. Tuplas ++
3. Listas +++
4. Diccionarios +++


'''

# Uso conjuntos

'''
Los sets o conjuntos son estructuras especiales que nos ayudan a almacenera un grupo
de elementos. Cuando el orden de los elementos no es relevante podemos utilizar sets
en Python.

como se define cuando veamos { ,,,,,}

<class 'set >
'''

set1={"a", "b", 'c', "d"}
print(type(set1))

set2={"e", 'f', "g"}

#metodos para el tratamiento de conjuntos
#set.union()
#union de conjunto
#print(set1.union(set2))

set3={"a", "b", "c","c","d", "d"}
#print(set3)

set4=set3.union(set1)
#print(set4)

#interseccesion de conjuntos con python

set5={ "f","w", "a", "b"}
#print(set5.intersection(set1))


set5.remove("w")
print(set5)
set4.add("a")
#print(set4)

#print(set4.issuperset(set5))
set4.issuperset(set5)

set6={"andres", 5, True}
set7={"andres", 5, True, "daniel"}
#print(set6.issuperset(set7)) #False
#print(set7.issuperset(set6)) #true

#print(set6.issubset(set7))#True
#print(set7.issubset(set6))#false


'''
Uso de tuplas 
Son estructuras de datos rigidas que no permiten muchos metodos 
se usan cuando queremos resguardar la informacion (inmutable)
como se define (, , , , , , , ,)

si permitenn valores duplicados
<class ''>


'''




tupla1=(1,1,1,1,1,2,3,4,5,)
#print(type(tupla1))
#metodos count
conteo=tupla1.count(1)
#print(conteo)


#index

indice=tupla1.index(1)
#print(indice)
'''
PTYHON ES UN LENGUAJE INDEXADO EN CERO
siempre el primer elemento en una estructura de daos tiene
el indice cer0, en otras palabras , la posicion inicail siempre es 0
indice <==>


'''

'''
Uso de listas

Las listas en python son estrcutura de datos que almacenan elementos de manera ordenada y mutable
son un tipo de dato nativo del lenguaje de programacion python


como se define: [,,,,,]
si permiten valores duplicados
pueden contener cualquier tipo de dato
numero, letras o incluso otras listas


'''

lista1=[8,9,7,5,4,10]
print(type(lista1))

lista2=["jhon", "alejandro","lewin"],["juan"]



#metodos
#count
#print(lista1.count(14))

#reverse

#print(lista1.reverse)
lista1.append("20")
print(lista1)

listab=lista1.sort()

#print(listab)
#remov
# 

lista1.remove(7)
#print(lista1)


lista2=["jhon", "alejandro","lewin"],["juan"]
print(lista2[0[1]])

