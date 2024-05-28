"""

OPERADORES MATEMATICOS
Para operaciones avanzadas se usa:

import math 

"""
import math

# Básicos
a = 10
b = 3
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"División Entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

# Avanzados
print(f"Raíz Cuadrada de 16: {math.sqrt(16)}")
print(f"Logaritmo Natural de 10: {math.log(10)}")
print(f"Logaritmo en Base 10 de 100: {math.log10(100)}")
print(f"Seno de π/2: {math.sin(math.pi / 2)}")
print(f"Coseno de 0: {math.cos(0)}")
print(f"Tangente de π/4: {math.tan(math.pi / 4)}")
print(f"Exponencial de 2: {math.exp(2)}")
print(f"Valor Absoluto de -10: {abs(-10)}")
print(f"Redondear 3.6: {round(3.6)}")
print(f"Máximo entre 1, 5, 3: {max(1, 5, 3)}")
print(f"Mínimo entre 1, 5, 3: {min(1, 5, 3)}")





 ### operadores aritmeticos ###
print(3 + 4)
print(3 - 4)
print(3 * 4) 
print(3 / 4)
# se usa el print para ver datos por consola

print(3 + 4)
print(3 + 4)
print(10 % 3)
# python funciona bien para hacer calculos 

print(10 // 3) # siempre dara un numero entero, apesar de que sea decimal

print(10**3) #numeros elevados =

print("Hola" + " Python"+" Que tal mijo?") 

print("Hola " + str(5)) 


print(2**3 + 3 - 7 /1 // 4) # se resuelven de todos modos 


print("Hola" * 5) # se multiplicó el string xd

# print("Hola " * (4 ** 5) ) # se ponen hola el numero de veces elevado

my_float = 2.5 * 2
print("Hola" * int (my_float))

#################################################################################


# Suma
suma = 5 + 3
print("Suma:", suma)

# Resta
resta = 7 - 2
print("Resta:", resta)

# Multiplicación
multiplicacion = 4 * 6
print("Multiplicación:", multiplicacion)

# División
division = 10 / 2
print("División:", division)

resultado = (5 + 3) * 2 - (4 / 2)
print("Resultado:", resultado)

# Potenciación
potencia = 2 ** 3
print("Potencia:", potencia)

# Raíz cuadrada (importando math)
import math
raiz_cuadrada = math.sqrt(16)
print("Raíz cuadrada:", raiz_cuadrada)

# Operaciones con números complejos
complejo1 = 2 + 3j
complejo2 = 1 - 2j

suma_complejos = complejo1 + complejo2
resta_complejos = complejo1 - complejo2
producto_complejos = complejo1 * complejo2
division_complejos = complejo1 / complejo2

print("Suma de complejos:", suma_complejos)
print("Resta de complejos:", resta_complejos)
print("Producto de complejos:", producto_complejos)
print("División de complejos:", division_complejos)

# Potenciación
base = 2
exponente = 3
resultado_potencia = base ** exponente
print("Resultado de la potenciación:", resultado_potencia)

# Raíz cuadrada (importando math)
import math
numero = 16
raiz_cuadrada = math.sqrt(numero)
print("Raíz cuadrada de", numero, ":", raiz_cuadrada)

# Logaritmo natural (base e)
numero_log = 10
logaritmo_natural = math.log(numero_log)
print("Logaritmo natural de", numero_log, ":", logaritmo_natural)

# Logaritmo en base 10
logaritmo_base_10 = math.log10(numero_log)
print("Logaritmo en base 10 de", numero_log, ":", logaritmo_base_10)


############################################################################################################33

## NUMEROS BINARIOS

# Número en base 2 elevado a una potencia
potencia = 78
resultado = 2 ** potencia

# Convertir el resultado a binario
binario = bin(resultado)

print("El número", resultado, "en base 2 es:", binario)

# Número binario base 2
numero_binario = "1010110001"

# Convertir el número binario a entero
numero_entero = int(numero_binario, 2)

print("El número binario", numero_binario, "convertido a entero es:", numero_entero)


# Número en base 8 (octal) usando potenciación
numero_octal = 0o10  # 1 * 8^1 + 0 * 8^0 = 8
print("Número en base 8:", numero_octal)  # Salida: 8 En este ejemplo, 0o10 representa el número en base 8, que es equivalente al número decimal 8. Si deseas realizar operaciones con números en base 8, simplemente usa el prefijo 0o seguido del número en base 8.

# Número binario base 8
numero_binario = "1010"

# Convertir el número binario a entero usando 8 elevado a la potencia
potencia = len(numero_binario) - 1
numero_entero = 0
for bit in numero_binario:
    numero_entero += int(bit) * (8 ** potencia)
    potencia -= 1

print("El número binario", numero_binario, "convertido a entero usando 8 elevado a la potencia es:", numero_entero)

# Convertir números enteros a binarios y hexadecimales ( 16 elevado a la.....)

# Número entero a binario
numero_entero = 42
numero_binario = bin(numero_entero)
print("Número entero", numero_entero, "en binario:", numero_binario)

# Número entero a hexadecimal
numero_hexadecimal = hex(numero_entero)
print("Número entero", numero_entero, "en hexadecimal:", numero_hexadecimal)

# Número binario a entero utilizando base 16
numero_binario = '101010'
entero_base_16 = int(numero_binario, 16)
print("Número binario", numero_binario, "a entero usando base 16:", entero_base_16)

#################################################################################

# Sacar porcentaje a numeros enteros


numero_original = 100
porcentaje = 20
porcentaje_numero = (porcentaje / 100) * numero_original
print("El", porcentaje, "% de", numero_original, "es:", porcentaje_numero)

# Sacar porcentaje a otros porcentajes

otro_numero_original = 200
otro_porcentaje = 30
otro_porcentaje_numero = (otro_porcentaje / 100) * otro_numero_original
print("El", otro_porcentaje, "% de", otro_numero_original, "es:", otro_porcentaje_numero)

# Sacar porcentaje a numeros decimales

numero_decimal_original = 12.5
porcentaje_decimal = 10
porcentaje_numero_decimal = (porcentaje_decimal / 100) * numero_decimal_original
print("El", porcentaje_decimal, "% de", numero_decimal_original, "es:", porcentaje_numero_decimal)

# Sacar porcentajes a numeros fraccionarios

from fractions import Fraction

numero_fraccionario_original = Fraction(3, 4)
porcentaje_fraccionario = 25
numero_decimal_fraccionario = float(numero_fraccionario_original)
porcentaje_numero_fraccionario = (porcentaje_fraccionario / 100) * numero_decimal_fraccionario
print("El", porcentaje_fraccionario, "% de", numero_fraccionario_original, "es:", porcentaje_numero_fraccionario)

#################################################################################################################################################3

# Convertir cualquier número a un decimal
numero = 5  # Puedes cambiar este número a cualquier valor
numero_decimal = float(numero)
print("Número:", numero, "Convertido a decimal:", numero_decimal)

from fractions import Fraction

# Decimal original
decimal_original = 3.75  # Puedes cambiar este número decimal a cualquier valor

# Convertir el decimal a un número entero
numero_entero = int(decimal_original)
print("Parte entera del decimal:", numero_entero)

# Convertir el decimal a fracción
parte_fraccionaria = decimal_original - numero_entero
fraccion = Fraction(parte_fraccionaria).limit_denominator()
print("Fracción del decimal:", fraccion)


############################################################################################################33
angulo = 90  # en grados

# Conversión de grados a radianes
radianes = math.radians(angulo)

# Seno
seno = math.sin(radianes)
print("Seno:", seno)

# Coseno
coseno = math.cos(radianes)
print("Coseno:", coseno)

# Tangente
tangente = math.tan(radianes)
print("Tangente:", tangente)


