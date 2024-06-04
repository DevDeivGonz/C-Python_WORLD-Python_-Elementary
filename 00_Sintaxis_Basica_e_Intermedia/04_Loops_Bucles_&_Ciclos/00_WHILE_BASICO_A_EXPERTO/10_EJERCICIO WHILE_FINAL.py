"""  

Ejercicio: Gestión de una Lista de Tareas

Descripción:
Crea un programa que simule la gestión de una lista de tareas. El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar Tarea: El usuario puede agregar una nueva tarea a la lista de tareas.
Listar Tareas: El usuario puede ver todas las tareas actualmente en la lista.
Marcar Tarea como Completada: El usuario puede marcar una tarea como completada.
Eliminar Tarea: El usuario puede eliminar una tarea de la lista.
Salir del Programa: El usuario puede salir del programa.

El programa debe utilizar un bucle while para mostrar un menú de opciones al usuario y manejar las operaciones según la opción seleccionada. 
Se puede usar una lista para almacenar las tareas y una bandera (flag) para controlar la ejecución del bucle while.

Este ejercicio pondrá a prueba tus habilidades en el uso de bucles while, listas, condicionales, entrada y salida de datos, 
así como el manejo de banderas para controlar el flujo del programa. ¡Diviértete programando!

"""

def Agregar_Tarea():
    tareas = []
    while True:
        nombre = input("Ingrese el nombre de la tarea (o escriba 'salir' para volver al menú principal): ")
        if nombre.lower() == "salir":
            break
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea (ALTA, MEDIA, BAJA): ")
        tareas.append({"nombre": nombre, "descripcion": descripcion, "prioridad": prioridad})
        continuar = input("¿Desea agregar otra tarea? (sí/no): ")
        if continuar.lower() != "sí":
            Agregar_Tarea()
            break
    return tareas
        
def Listar_Tareas():
    pass

def MarcarTareas_Cumplidas():
    print("EN DESARROLLO")
    pass
        
def Eliminar_tarea():
    pass

def menu_principal():
    print("Bienvenido al Gestor de Tareas")
    print("1. Agregar Tarea")
    print("2. Listar Tareas")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir del Programa")
    
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            print("Agregando Tarea...")
            tareas_agregadas = Agregar_Tarea()
            print("Tareas agregadas:")
            for tarea in tareas_agregadas:
                print(tarea)
                
        elif opcion == "2":
            Listar_Tareas()
        elif opcion == "3":
            MarcarTareas_Cumplidas()
        elif opcion == "4":
            Eliminar_tarea()
        elif opcion == "5":
            print("Gracias por elegirnos\nQue tenga un excelente dia!")
            break
        else:
            print("Entrada inválida. Ingrese una opción válida.")

if __name__ == "__main__":
    menu_principal()
