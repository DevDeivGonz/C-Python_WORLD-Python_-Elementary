"""

Crear un programa que calcule el area de figuras geometricas
 
"""


print("Bienvenido, aqui se calculara el area de figuras geometricas, por favor use el . y no ,")

longitud = float(input("Ingrese la longitud del rectangulo"))
anchura = float(input("Ingrese la anchura del rectangulo"))
area_del_rectagulo = longitud * anchura 

print(f"El area del rectangulo es: {area_del_rectagulo}")

lado_a = float(input("Ingrese la medida del lado A del cuadrado"))
lado_b = float(input("Ingrese la medida del lado B del cuadrado"))
area_del_cuadrado = lado_a * lado_b 

print(f"El area del cuadrado es: {area_del_cuadrado}")

base = float(input("Ingrese la base del triangulo"))
altura = float(input("Ingrese la altura del triangulo"))
area_del_triangulo = base * altura / 2  

print(f"El area del triangulo es {area_del_triangulo}" )