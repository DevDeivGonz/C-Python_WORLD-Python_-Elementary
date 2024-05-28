print("MAYOR O MENOR")

while True:
    numero_uno = int(input("Ingrese el primero numero"))
    seg_numero = int(input("Ingrese el segundo numero para compararlo"))
    
    if  numero_uno > seg_numero:
        print(f"{numero_uno} es mayor que {seg_numero}")
    elif numero_uno < seg_numero:
        print(f"{numero_uno} es menor que {seg_numero}")
    else:
        print("Los números son iguales. Se detiene la ejecucion")
        break
    
    print("El ejercicio ha terminado")
 