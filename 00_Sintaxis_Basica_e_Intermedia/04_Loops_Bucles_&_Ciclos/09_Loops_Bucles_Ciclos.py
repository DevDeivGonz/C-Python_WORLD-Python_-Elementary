
my_list = [35, 24, 17, 68, 52, 30, 17]

for element in my_list: # este bucle esta atado un numero finito de datos
    print(element)
  
my_tuple = (35, 1.71, "Deivid", "Gonzalez", "De Colombia")

for element in my_tuple: 
    print(element)
    
my_set = {"Deiv", "Gonz", 21} 
for element in my_set: 
    print(element)
    
my_dict = {"Nombre": "Deivid",  "Apellido": "Gonzalez","Edad": 21, 1:"Python"}
for element in  my_dict: 
    print(element)
    break
else:
    print("El bucle for ha finalizado")
    
    # Ejemplo con if, else, elif, while y for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par.")
    elif numero % 3 == 0:
        print(f"{numero} es múltiplo de 3 pero no es par.")
    else:
        print(f"{numero} no es par ni múltiplo de 3.")

""" Elif es una abreviatura de "else if". Se utiliza para evaluar una condición adicional si la condición 
en el if no se cumple.
Puedes tener múltiples bloques elif después de un if, y estos se evaluarán en orden secuencial.
Si se encuentra una condición elif que sea verdadera, se ejecutará el bloque de código correspondiente y 
el resto de los bloques elif y el else se omitirán. """


contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("El bucle while ha terminado.")


    
    
    
    
    