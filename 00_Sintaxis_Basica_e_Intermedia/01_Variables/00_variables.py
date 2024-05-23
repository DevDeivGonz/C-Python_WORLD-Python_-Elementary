# variables 

""" 

Variables y Tipos de Datos en Python
Variables

Una variable es un nombre que se asigna a un valor que se almacena en memoria. Se crea utilizando el operador =.

"""

""" int (Enteros) """

age = 30

# Operaciones Básicas:

a = 10
b = 3
sum = a + b        # 13
difference = a - b # 7
product = a * b    # 30
quotient = a // b  # 3 (división entera)
remainder = a % b  # 1
power = a ** b     # 1000 (10^3)

# Ejemplo Avanzado:

large_number = 123456789012345678901234567890
bitwise_and = a & b # 2 (AND bit a bit)
bitwise_or = a | b  # 11 (OR bit a bit)

""" float (Números de Punto Flotante) """

price = 19.99

# Operaciones Básicas:

a = 5.7
b = 2.3
sum = a + b        # 8.0
difference = a - b # 3.4
product = a * b    # 13.11
quotient = a / b   # 2.4782608695652173

# Ejemplo Avanzado:

import math
result = math.sqrt(16.0) # 4.0
rounded = round(2.34567, 2) # 2.35

""" str (Cadenas de Texto) """

# Ejemplo Básico:

name = "Alice"

# Operaciones Básicas:

greeting = "Hello, " + name # "Hello, Alice"
length = len(name)          # 5
character = name[0]         # 'A'

# Ejemplo Avanzado:

multiline = """This is a 
multiline string."""
formatted = f"{name} is {age} years old." # "Alice is 30 years old."
split_str = "Alice, Bob, Charlie".split(", ") # ['Alice', 'Bob', 'Charlie']


""" bool (Booleanos) """

# Valores de verdad: True o False.
# Ejemplo Básico:

is_active = True

# Operaciones Básicas:

a = True
b = False
conjunction = a and b # False
disjunction = a or b  # True
negation = not a      # False

# Ejemplo Avanzado:

comparison = (5 > 3) # True
is_equal = (5 == 5)  # True
combined = (5 > 3) and (5 == 5) # True

#######################################################################################################################################################################################

my_str_variable = "my string variable"
print (my_str_variable)

my_int_variable = 5
print (my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print (my_bool_variable)

#concatenacion de variables en un print 
print(type(print (my_str_variable, str(my_int_to_str_variable), my_bool_variable)))
print(type(print ("My cadena de Texto xd")))
print("este es el valor de:", my_bool_variable)

#Algunas Funciones de sistema 

print(len(my_int_to_str_variable))

#variables en una sola Linea ! cuidado con abusar de esa sintaxis!
name, surname, alias, age = "Brains", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ",Mi edad es:", age,"Y mi alias es", 35)

# Inputs
""""
#name = input("Cual es su nombre? ")
#age = input("Cuantos años tienes? ")
print(name)
print(age)
"""""

# Cambiamos su tipo
name = 35
age = "Brians"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion"
address = True 
address = 5
print (type(address))

#42intput pide datos 