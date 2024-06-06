import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    

""" print("Contador")


contador = 0
for i in range(5):
    contador += 1
print("El contador es:", contador)

input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

contador = 0

for i in range(100):
    contador += +2 # cuenta de 2 en 2, numeros pares
    print(contador)
    
input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

contador = -10

for i in range(100):
    contador += 5 # cuenta de 5 en 5, numeros pares
    print(contador)
    
    
input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

limite = 10
contador = 0

for i in range(1, limite + 1):
    contador += 1

print("El contador ha llegado a:", contador)
"""
###


cadena = "Hola Mundo"
contador = 0

for caracter in cadena:
    contador += 1

print("El número de caracteres en la cadena es:", contador)

input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

cadena = "Hola Mundo, este es un ejemplo"
contador_palabras = len(cadena.split())

print("El número de palabras en la cadena es:", contador_palabras)

input("ENTER PARA CONTINUAR: ")
limpiar_pantalla()

cadena = "Hola Mundo"
caracter_buscado = 'o'
contador_ocurrencias = cadena.count(caracter_buscado)

print(f"El número de ocurrencias de '{caracter_buscado}' en la cadena es:", contador_ocurrencias)

