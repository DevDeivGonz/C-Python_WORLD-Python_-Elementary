"""
    

Ejercicio: Calcular el Volumen de un Cilindro

Dado un cilindro con un radio de la base `r` y una altura `h`, calcula su volumen utilizando operadores aritméticos.

**Paso 1:** Define las variables `r` y `h` con los valores del radio de la base y la altura del cilindro, respectivamente.

**Paso 2:** Utiliza el operador de potencia (`**`) para elevar el radio al cuadrado y luego multiplica por la altura y por el valor de π (pi) para calcular el volumen del cilindro.

**Paso 3:** Imprime el resultado del cálculo del volumen.

¡Prueba a calcular el volumen de un cilindro y verifica si obtienes el resultado correcto!

"""
import math 
pi = math.pi
r_radio = float(input("Ingrese el Radio del cilindro"))
h_altura = float(input("Ingrese la Altura del cilindro"))
volumen = pi * r_radio**2 * h_altura
print (f"El volumen del cilindro es: {volumen}")