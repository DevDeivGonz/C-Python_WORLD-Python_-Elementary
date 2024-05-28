"""
WHILE 

El bucle while repite un bloque de código mientras se cumpla una condición específica.
La condición se evalúa antes de cada iteración. Si la condición es verdadera, el bloque de código se ejecuta; de lo contrario,
el bucle termina.
"""

print("USA DE WHILE BASICO")
contador = -15 # EMPIEZA A CONTAR
while contador < 45: # LLEGA HASTA EL NUMERO DE CONTAR
    print(contador)
    contador += 1 # CUENTA

import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

input("INSERTE UN CARACTER PARA CONTINUAR")

limpiar_pantalla()


# Intermedio
# El bucle while se puede usar junto con la sentencia else.
print("USA DE WHILE INTERMEDIO")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado.")
# El bloque else se ejecuta cuando la condición del while se vuelve falsa.


import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
input("INSERTE UN CARACTER PARA CONTINUAR")


# Avanzado
# Puedes usar el bucle while con declaraciones break y continue para un control más fino.
print("USA DE WHILE AVANZADO")
contador = 0
while contador < 456:
    contador += 1
    if contador == 5:
        continue  # Salta la iteración actual
    if contador == 123:
        break  # Sale del bucle
    print(contador)
    
import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
input("INSERTE UN CARACTER PARA CONTINUAR")

# OTRO EJEMPLO 

my_condition = 0 # es una especie de if pero que se repite
print("MAYOR O MENOR")
while my_condition < 0:
    print(my_condition)
    my_condition += 1
else: # else pertenece a WHILE, else nunca va solo
    print("La ejecucion es mayor o igual que") 
    
print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition > 0 :
        print("Se detoiene la ejecucion")
        break

print(my_condition)

import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
input("INSERTE UN CARACTER PARA CONTINUAR")


