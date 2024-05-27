# Lista de números
numeros = [10, 21, 3, 45, 15, 7, 30, 14, 29, 35]

# 1. Encuentra el número máximo y mínimo de la lista
numero_maximo = max(numeros)
numero_minimo = min(numeros)

# 2. Calcula la suma y la media de los números
suma_numeros = sum(numeros)
media_numeros = suma_numeros / len(numeros)

# 3. Crea una nueva lista que contenga los números mayores que la media
numeros_mayores_que_media = list(filter(lambda x: x > media_numeros, numeros))

# 4. Ordena la lista original en orden descendente
numeros_ordenados_desc = sorted(numeros, reverse=True)

# 5. Convierte la lista de números en una lista de cadenas
numeros_como_cadenas = list(map(str, numeros))

# Resultados
print(f"Número máximo: {numero_maximo}")
print(f"Número mínimo: {numero_minimo}")
print(f"Suma de los números: {suma_numeros}")
print(f"Media de los números: {media_numeros}")
print(f"Números mayores que la media: {numeros_mayores_que_media}")
print(f"Números ordenados en orden descendente: {numeros_ordenados_desc}")
print(f"Números como cadenas: {numeros_como_cadenas}")
