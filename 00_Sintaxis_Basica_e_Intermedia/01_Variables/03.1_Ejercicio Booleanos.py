"""

En este ejercicio, crearás un sencillo juego de adivinanza en el que el usuario debe adivinar un número secreto. 
El programa le dará pistas indicando si el número adivinado es mayor o menor que el número secreto. El juego continuará hasta que 
el usuario adivine el número correcto o elija salir

"""
import random
import os  # Importa el módulo os para limpiar la pantalla

num_secreto = random.randint(1, 50) # pone numeros aleatorios pero debe declararse con import random 
respuesta_correcta = False

print("""
       Bienvenido al juego de las adivinanzas. Tendrás que poner 
       el número que creas que es el correcto.
       Intenta adivinar hasta lograrlo, pero si te rindes
       escribe 'salir' para terminar el juego.
       
       ¡¡¡¡ MUCHA SUERTE SUERTEEEEEE !!!!!
       """)

while not respuesta_correcta:
    respuesta_usuario = input("Ingresa tu adivinanza: ")

    if respuesta_usuario.lower() == "salir": # lower() pone todos los caracteres en minuscula
        
        print("Gracias por jugar.")
        break

    if not respuesta_usuario:
        print("Por favor, ingresa un valor.")
        continue

    try: #  try en Python se utiliza para manejar excepciones. Dentro de un bloque try, puedes colocar código que podría generar 
         #  una excepción. 
         #  Si ocurre una excepción dentro del bloque try, Python busca un bloque except correspondiente que maneje esa excepción.
        adivinanza = int(respuesta_usuario)
    except ValueError:
        print("Por favor, ingresa un valor válido.")
        continue

    if adivinanza < num_secreto:
        print("Tu adivinanza es menor que el número correcto.")
    elif adivinanza > num_secreto:
        print("Tu adivinanza es mayor que el número correcto.")
    else:
        print(f"Felicidades, adivinaste el número correcto: {num_secreto}")
        respuesta_correcta = True

    if not respuesta_correcta:
        print("Intenta de nuevo.")

# Función para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

input("Presiona ENTER para continuar...")

limpiar_pantalla()
