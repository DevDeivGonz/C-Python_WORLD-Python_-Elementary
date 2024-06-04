import os
print("USOS DE WHILE TRUE")
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
input("INTER PARA CONTINUAR")
limpiar_pantalla()
    

while True:
    respuesta = input("Escribe 'salir' para terminar el bucle: ")
    if respuesta == 'salir':
        break

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        input("INTER PARA CONTINUAR")
limpiar_pantalla()

print("USO AVANZADO DE WHILE TRUE")
def get_positive_number():
    while True:
        try:
            number = int(input("Ingrese un número positivo: "))
            if number > 0:
                print("El numero es positivo")
                return number
            else:
                print("El número no es positivo. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

print(f"Número ingresado: {get_positive_number()}")

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        input("INTER PARA CONTINUAR")
limpiar_pantalla()


def menu():
    print("WHILE TRUE USADO PARA CREAR MENUS")
    while True:
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Salir")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            print("Ha seleccionado la Opción 1")
        elif choice == "2":
            print("Ha seleccionado la Opción 2")
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        input("INTER PARA CONTINUAR")
limpiar_pantalla()
