import os
print("\033c", end="", flush=True)
print("Alumno: Esteban Leonardo Giraldo Cristancho\nFicha: 2823506 G1\n\nEl siguiente software le indicará si un triángulo es equilátero, isósceles o escaleno.\nSi todos los lados son iguales, le dará una respuesta correcta.\n")
a = float(input("Ingrese la longitud del lado [a]: "))
b = float(input("Ingrese la longitud del lado [b]: "))
c = float(input("Ingrese la longitud del lado [c]: "))
if a == b and b == c:
        print("\nEl triángulo es equilátero.\n")
elif a == b or b == c or a == c:
        print("\nEl triángulo es isósceles.\n")
else:
        print("\nEl triángulo es escaleno.\n")
os.system('pause')