"""

En Python, while y for son dos estructuras de control que se utilizan para realizar bucles, es decir, 
ejecutar repetidamente un bloque de código. Sin embargo, hay diferencias importantes entre ellos.

WHILE
La sentencia while ejecuta un bloque de código mientras una condición sea verdadera. 
La condición se evalúa antes de cada iteración del bucle y, si es True, se ejecuta el bloque de código. Si es False, el bucle se detiene.

"""


import os
print(" WHILE Y SUS USOS DESDE LO BASICO HASTA LO MAS EXPERTO")
def limpiar_pantalla():
    if os.name == "int":
        os.system("cls")
    else:
        os.system("clear")
input("DAR ENTER PARA CONTINUAR")
limpiar_pantalla()


contador = 0 # INICIA A CONTAR 
while contador < 100: # ES LA BRECHA MAXIMA HASTA DONDE DEJARA DE CONTAR 
    print(contador)
    contador += 3**2 # SE ASIGNA COMO LOS NUMEROS VAN A CONTARSE, AQUI SE CONTARAN PERO CON EL 3**2, 
                     # PERO SI SE PONE DE A 2 SE CONTARA EN PAR, Y SI SE PONE DE A 3 SOLO CONTARA LOS MULTIPLOS DE 3, Y ASI SUSESIVAMENTE 
                     
def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
input("ENTER PARA CONTINUAR")
limpiar_pantalla()

contador = 0
while contador < 100:
    print(contador)
    contador += 5**2 # se contará con los numeros de 5**2
    
def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
       os.system("clear")
input("ENTER PARA CONTINUAR")
limpiar_pantalla()



