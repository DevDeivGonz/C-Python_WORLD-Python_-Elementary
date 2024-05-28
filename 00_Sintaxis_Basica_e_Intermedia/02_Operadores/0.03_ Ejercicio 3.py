"""
    
Ejercicio 3: Calcular el Aumento de Salario

Dado un salario inicial y un porcentaje de aumento, calcula el nuevo salario después del aumento.

Paso 1: Solicita al usuario que ingrese el salario inicial y el porcentaje de aumento que la empresa va aumentar.
Paso 2: Calcula el aumento salarial multiplicando el salario inicial por el porcentaje de aumento (expresado como decimal).
Paso 3: Suma el aumento salarial al salario inicial para obtener el nuevo salario.
Paso 4: Imprime el nuevo salario después del aumento.

¡Este ejercicio te permitirá practicar el cálculo de porcentajes y aplicarlos a situaciones prácticas como el aumento de 
salarios! Si tienes alguna pregunta o necesitas ayuda adicional, ¡no dudes en preguntar!
"""

print("Bievenido Admi")
nombresApellidos_empleado = input("Ingrese el nombre del empleado ")
salario_asig = float(input("Ingrese el salario actual del empleado "))
aumento_salario = float(input("Ingrese el aumento en (%) del salario del empleado "))

salario_final = salario_asig + salario_asig * aumento_salario

print(f"El nuevo salario del empleado {nombresApellidos_empleado} es de {salario_final}")
