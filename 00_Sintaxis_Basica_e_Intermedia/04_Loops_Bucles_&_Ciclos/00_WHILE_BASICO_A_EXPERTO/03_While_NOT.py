"""

El término "while not" se refiere a una estructura de control que utiliza la negación de una condición en un bucle while. 
Básicamente, significa "mientras no sea cierto". Se utiliza para ejecutar un bloque de código mientras la condición especificada sea falsa.

"""
import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')    
    else:
        os.system('clear')
        
def main_menu():
    print("""BIENVENIDO AL MENU PRINCIPAL 
          \nPOR FAVOR ELIGA UNA OPCION
          \n""")
    print("1. Entrada de datos validada negativamente")
    print("2. Espera hasta que se cumpla una condición inversa")
    print("3. Iteración hasta que se alcance un estado deseado")
    print("4. Procesamiento de listas o estructuras de datos")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Entrada inválida. Ingrese una opción válida.")
            continue  # Vuelve al inicio del bucle para solicitar una nueva entrada
        
        if opcion == 1:
            submenu_numeros_negativos()
        elif opcion == 2:
            submenu_espera_condicion()
        elif opcion == 3:
            submenu_interaccion_estado()
        elif opcion == 4:
            submenu_procesamiento_listas_datos()
        elif opcion == 5:
            print("¡Gracias por elegirnos, nos veremos en otra oportunidad!")
            break  # Sale del bucle while
        else:
            print("Opción no válida. Intente de nuevo.")

 
def submenu_numeros_negativos():
    numero = 0
    while True:
        limpiar_pantalla()
        print("""Entrada de datos validada negativamente.
              \nCuando deseas solicitar al usuario que ingrese datos hasta que proporcionen una entrada válida, 
              puedes usar while not para ejecutar el bloque de código mientras la entrada del usuario no sea válida.
        \nENTRADA DE DATOS VALIDADA NEGATIVAMENTE.
        \nSeleccione una opción:
        \n""")
        print("1. Ingresar un número positivo")
        print("2. Regresar al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue
        
        if opcion == 1:
            while not numero > 0:
                try:
                    numero = int(input("Ingrese un número positivo: "))
                    if numero <= 0:
                        print("El número ingresado no es válido. Intente de nuevo.")
                except ValueError:
                    print("Entrada inválida. Intente de nuevo.")

            print(f"¡Bien hecho! Has ingresado un número positivo: {numero}")
        elif opcion == 2:
            main_menu() # se pone asi para volver al menu principal
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def submenu_espera_condicion():
    # Aquí iría el código para el segundo submenú
    # Esperar hasta que el usuario no haya ingresado "salir"
    respuesta = ""
    print("""Espera hasta que se cumpla una condición inversa
          \nA veces, puede ser más natural pensar en términos de lo que no queremos que suceda en lugar de lo que queremos 
          que suceda. En esos casos, while not puede ser útil para ejecutar un bloque de código hasta que una condición 
          específica se vuelva verdadera.
          """)
    print("1. Ingresar un número positivo")
    print("2. Regresar al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
        
    if opcion == 1: 
        while not respuesta == 'salir':
            respuesta = input("Escribe 'salir' para terminar el programa: ")
            if not respuesta == 'salir':
                print("Respuesta incorrecta. Inténtelo de nuevo.")
    else:
        main_menu()
        limpiar_pantalla()


def submenu_interaccion_estado():
    print("""Espera hasta que se cumpla una condición inversa
          \nA veces, puede ser más natural pensar en términos de lo que no queremos que suceda en lugar de lo que queremos 
          que suceda. En esos casos, while not puede ser útil para ejecutar un bloque de código hasta que una condición 
          específica se vuelva verdadera.
          """)
    print("1. Ingresar: Espera hasta que se cumpla una condición inversa")
    print("2. Regresar al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
        
    contador = 0
    numero_objetivo = 10
        
    if opcion == 1: 
        while not contador == numero_objetivo:
            print(f"Contador: {contador}")
            contador += 1
    else:
        main_menu
        limpiar_pantalla()

    # Aquí iría el código para el tercer submenú
    main_menu()
def submenu_procesamiento_listas_datos():
    print("""Procesamiento de listas o estructuras de datos: 
          \nPuedes usar while not para recorrer una lista o una estructura de datos hasta que se haya procesado completamente o 
          se cumpla una condición de salida específica..
          """)
    print("1. Ingresar: Procesamiento de listas o estructuras de datos")
    print("2. Regresar al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")
        
    numeros = [1, 2, 3, 4, 5, -1, 6, 7, 8, 9, 10]
    indice = 0
    
    if opcion == 1:

        while not numeros[indice] < 0:
            print(f"Número en el índice {indice}: {numeros[indice]}")
            indice += 1

        print("Se ha encontrado un número negativo")
    else:
        main_menu()

if __name__ == "__main__":
    main_menu()
