"""

" FOR " es una estructura de control en muchos lenguajes de programación que se utiliza para iterar sobre una secuencia de elementos, 
como una lista, tupla, diccionario o rango. Básicamente, permite ejecutar un bloque de código una vez para cada elemento en la secuencia.
   
ITERAR ES REPETOR DEFINIDAMENTE

quiere decir que mientras que hile se usa de manera idefinida, for se usa de manera ya definida.
"""


import os
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
    
    
print("Iterar sobre los elementos de una lista: ")
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

numeros = [1,2,3,4,5,6,7,12,34,56,78,12,34,545,]
bananos = ["VERDES", "ROJOS", "AMARILLOS", "NEGROS"]

for numeros in numeros: 
    print(numeros)
for bananos in bananos:
    print(bananos)

