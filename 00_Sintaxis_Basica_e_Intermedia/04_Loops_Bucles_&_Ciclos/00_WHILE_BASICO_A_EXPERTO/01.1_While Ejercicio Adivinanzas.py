import random
import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def juego_de_las_adivinanzas():
    numero_random = random.randint(1, 20)
    intentos = 0
    
    while True:
        try:
            intento = int(input("Adivina el numero: "))
            intentos += 1  # Incrementa el número de intentos

            if intento == numero_random:
                print(f"FELICIDADES, ADIVINASTE EL NUMERO EN {intentos} INTENTOS")
                break
            elif intento > numero_random:
                print("EL NUMERO ES MENOR ")
            else:
                print("EL NUMERO ES MAYOR ")
        except ValueError:
            print("ERROR. DEBE INGRESAR UN VALOR NUMÉRICO VÁLIDO ")

def main(): # Define una función llamada main(). Esta función puede contener el código principal de tu programa.
    print("JUEGO DE LAS ADIVINANZAS USANDO WHILE FALSE")
    print("""BIENVENIDO, DIGINTE EL NUMERO QUE CREA QUE ES,
          RECUERDE QUE ES DEL 1 AL 20.
          !!! BUENA SUERTE !!!
          """)
    input("ENTER PARA CONTINUAR")
    limpiar_pantalla()
     
    while True:
        juego_de_las_adivinanzas()
        respuesta = input("""\n
                        DESEA CONTINUAR?
                        PULSE ENTER PARA CONTINUAR
                        INSERTE 'salir' PARA FINALIZAR EL JUEGO
                        """).strip().lower() # .strip(): Elimina los espacios en blanco al principio y al final de una cadena. Por ejemplo, si el usuario escribe " hola ", 
                                             #.strip() eliminará los espacios en blanco y dejará "hola".
                                             #.lower(): Convierte toda la cadena en minúsculas. Por ejemplo, si el usuario escribe "Hola", .lower() lo convertirá en "hola". 
                                             # Esto es útil para hacer que la entrada del usuario sea insensible a mayúsculas y minúsculas, lo que significa que "SALIR", 
                                             # "salir" y "Salir" se considerarán equivalentes.

        if respuesta == 'salir':
            limpiar_pantalla()
            print("QUE TENGA UN EXCELENTE DIA")
            break  # Salir del bucle principal

if __name__ == "__main__":
    main()
# Esta línea verifica si el script se está ejecutando directamente o si se está importando como un módulo en otro script. Si se está ejecutando directamente (es decir,
# no se está importando), se ejecutará el código que está indentado debajo de esta línea. Esto es útil cuando quieres que ciertas partes del código se ejecuten --->
# ---> solo cuando ejecutas el script directamente, y no cuando lo importas como un módulo en otro script.

