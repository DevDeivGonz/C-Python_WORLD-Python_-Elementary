"""
ALGORITMO TRIANGULO
Realizar un el código de programación (con cualquier lenguaje de programación) que permita caracterizar un triangulo de acuerdo 
a sus lados y ángulos (EL USUSARIO SOLAMENTE COLOCA LOS LADOS), haciendo uso de los operadores lógicos "y" y "o" en python ( AND y OR )

1. Portada
2. Código
3. Pantallazos de su funcionamiento

Equilátero  | Si los tres lados son iguales.

Isósceles   | dos lados son iguales.

Escaleno    | Si todos los lados son diferentes.

# Clasificación del Triángulo según los Ángulos:

Rectángulo: Si cumple con el teorema de Pitágoras (a² + b² = c²).

Acutángulo: Si todos los ángulos son menores de 90 grados.

Obtusángulo: Si un ángulo es mayor de 90 grados.

Para esta clasificación, se utilizan las longitudes de los lados para calcular los ángulos internos mediante fórmulas matemáticas.
Salida de Resultados:

Mostrar al usuario el tipo de triángulo según sus lados y ángulos.
    
"""
print("|                                           |")
print("|                                           |")
print("|           BUEN DIA PARA TODOS             |")
print("|                                           |")
print("|                                           |")
print("| MI NOMBRE ES BRANDON DAVID GONZALEZ LOPEZ |")
print("|                                           |")
print("|                                           |")
print("|    PERTENECIENTE A LA FICHA 2823506-G1    |")
print("|                                           |")
print("|                                           |")
print("|   ESTA ES LA PRESENTACION DEL TALLER 5°   |")
print("|                                           |")
print("|                                           |")

import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("_____________________________________________")
input("INSERTE ENTER PARA CONTINUA  ")

limpiar_pantalla()

while True:

    print("____________________________________________________")
    lado1 = float(input("Ingrese la longitued del primer lado  "))
    print("____________________________________________________")
    lado2 = float(input("Ingrese la loguntud del segudo lado  "))
    print("____________________________________________________")
    lado3 = float(input("Ingrese la longitud del tercer lado  "))
    print("____________________________________________________")

    if (lado1 and lado2) == lado3 and (lado2 and lado3) == lado1: # Debe ser Equilátero si los tres lados son iguales.
        print("Es un triangulo Equilátero")
    elif (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1): # Debe ser Isósceles si dos lados son iguales.
        print("Es un triangulo Isósceles")
    else:
        print("El triangulo es Escaleano") # Debe ser Escaleno si todos los lados son diferentes.
    
        print("____________________________________________________")
    respuesta = input("¿Desea continuar? (SI/NO): ").upper() # Convertir la respuesta a mayúsculas

    if respuesta == "NO":
        limpiar_pantalla()
        print("____________________________________________________")
        print("Espero una nota de 100 profesora UwU, lindo día!")
        print("____________________________________________________")
        break
    
    limpiar_pantalla()


    

    
    
    
    
    