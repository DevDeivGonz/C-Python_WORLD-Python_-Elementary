import os

lista_usuarios = []
envios = []

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Agregar_Producto():
    productos = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        numero_productos_enBodega = int(input("Ingrese el número de este producto en bodega: "))
        numero_envios_pendientes = int(input("Ingrese el número de envíos pendientes: "))
        
        producto = {
            "Nombre del producto": nombre_producto, 
            "Precio": precio, 
            "Número de productos en Bodega": numero_productos_enBodega, 
            "Número de envíos pendientes": numero_envios_pendientes
        }
        
        productos.append(producto)
        
        continuar = input("¿Desea agregar otro producto? (sí/no): ")
        if continuar.lower() != "sí":
            break
    
    return productos

def Marcar_Envios_Enviados():
    print("Aquí están los envíos pendientes:")
    for envio in envios:
        if envio.get("Número de envíos pendientes", 0) > 0:
            print(envio)
    
    continuar = input("¿Desea seguir viendo los envíos pendientes? Ingrese 'si'.\n¿Desea volver al menú principal? Ingrese 'salir'.\n")
    if "si" in continuar.lower():
        Marcar_Envios_Enviados()
    elif "salir" in continuar.lower():
        return
    else:
        print("ERROR.\nPor favor ingrese una opción válida.")
        Marcar_Envios_Enviados()

def menu_principal():
    limpiar_pantalla()
    while True:
        print("Menú Principal")
        print("1. Agregar Producto")
        print("2. Marcar Envíos Enviados")
        print("3. Ver todos los productos ingresados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            productos = Agregar_Producto()
            envios.extend(productos)
        elif opcion == "2":
            Marcar_Envios_Enviados()
        elif opcion == "3":
            print("Todos los productos ingresados:")
            for envio in envios:
                print(envio)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


menu_principal()