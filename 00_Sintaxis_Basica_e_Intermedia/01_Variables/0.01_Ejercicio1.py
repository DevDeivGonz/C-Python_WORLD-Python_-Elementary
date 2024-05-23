my_list = []

print("Bienvenido")
nombre_apellido = input("Ingrese su nombre y apellido ")
jornada = input("Ingrese a la jornada a la que pertenece")
edad = int(input("Ingrese su edad"))

my_list = [{nombre_apellido}, {jornada}, {edad} ]
print(f"Bienvenudo {nombre_apellido}, usted pertenece a la jornada {jornada} y su edad es {edad} años de edad")
if edad < 18:
    print(f"Usted es menor de edad")
else:
    print(f"Usted es mayor de edad")
    
if edad > 18:
    print(f"Usted es mayor de edad")
else:
    print(f"Usted es menor de edad")


        