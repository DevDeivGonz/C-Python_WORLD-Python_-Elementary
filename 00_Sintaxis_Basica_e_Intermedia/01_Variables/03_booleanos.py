"""
BOOLEANOS 

Los booleanos en Python son valores que pueden ser True o False. Estos valores pueden ser el resultado de evaluaciones 
de expresiones utilizando operadores de comparación y lógicos. A continuación, explicaré en detalle y con ejemplos cómo funcionan 
estos operadores y cómo se utilizan en estructuras de control como bucles while.

"""



import random

# Generar un número entero aleatorio entre 1 y 10 (incluidos ambos extremos)
numero_aleatorio = random.randint(1, 10) # random.randint se usa para poner numeros aleatorios
print(f"El número aleatorio generado es: {numero_aleatorio}")

# Generar un número entero aleatorio entre 50 y 100
numero_aleatorio_2 = random.randint(50, 100)
print(f"Otro número aleatorio generado es: {numero_aleatorio_2}")

###################################################################

import os  # Importa el módulo os
import random

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpiar_pantalla()

# Genera un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
adivinado_correctamente = False

print("¡Bienvenido al juego de adivinanza!")
print("Tengo un número secreto entre 1 y 100.")
print("Intenta adivinarlo o escribe 'salir' para terminar el juego.")

while not adivinado_correctamente:
    # Solicita al usuario que ingrese un número
    entrada_usuario = input("Ingresa tu adivinanza: ")

    # Verifica si el usuario quiere salir
    if entrada_usuario.lower() == 'salir':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
    
    # Intenta convertir la entrada a un número entero
    try:
        adivinanza = int(entrada_usuario)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    
    # Verifica la adivinanza del usuario
    if adivinanza < numero_secreto:
        print("El número secreto es mayor que tu adivinanza.")
    elif adivinanza > numero_secreto:
        print("El número secreto es menor que tu adivinanza.")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto que era {numero_secreto}.")
        adivinado_correctamente = True

    # Mensaje para intentar de nuevo si no ha adivinado correctamente
    if not adivinado_correctamente:
        print("Inténtalo de nuevo.")

input("Presiona ENTER para salir...")

##############################################################################################################33

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
input("  INSERTE ENTER PARA CONTINUA  ")

limpiar_pantalla()
