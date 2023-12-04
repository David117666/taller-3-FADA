from collections import Counter
import random


def encuentra_mas_repetido(vector, inicio=0, fin=None):
    if fin is None:
        fin = len(vector) - 1

    # Caso base: si el subvector tiene un solo elemento, ese es el número más repetido
    if inicio == fin:
        return vector[inicio]

    # Divide el vector en dos mitades
    medio = (inicio + fin) // 2

    # Encuentra los números más repetidos en cada mitad
    izquierda_mas_repetido = encuentra_mas_repetido(vector, inicio, medio)
    derecha_mas_repetido = encuentra_mas_repetido(vector, medio + 1, fin)

    # Combina los resultados
    if izquierda_mas_repetido == derecha_mas_repetido:
        return izquierda_mas_repetido

    # Cuenta la frecuencia de cada número en cada mitad
    frecuencias_izquierda = Counter(vector[inicio:medio + 1])
    frecuencias_derecha = Counter(vector[medio + 1:fin + 1])

    # Encuentra el número más repetido en general
    if frecuencias_izquierda[izquierda_mas_repetido] > frecuencias_derecha[derecha_mas_repetido]:
        return izquierda_mas_repetido
    else:
        return derecha_mas_repetido


# Ejemplo de uso vectores de tamaño 10 , 100 , 1000 y 10000

vectorTamaño10 = [random.randint(1, 9) for _ in range(10)]
print(f"El vector tamaño 10 es: {vectorTamaño10}")
print(f"El número que más se repite en el vector de tamaño 10 es: {encuentra_mas_repetido(vectorTamaño10)}\n")

# _____________________________________________________________________

vectorTamaño100 = [random.randint(1, 9) for _ in range(100)]
print(f"El vector tamaño 100 es: {vectorTamaño100}")
print(f"El número que más se repite en el vector de tamaño 100 es: {encuentra_mas_repetido(vectorTamaño100)}\n")

# _____________________________________________________________________

vectorTamaño1000 = [random.randint(1, 9) for _ in range(1000)]
print(f"El vector tamaño 1000 es: {vectorTamaño1000}")
print(f"El número que más se repite en el vector de tamaño 1000 es: {encuentra_mas_repetido(vectorTamaño1000)}\n")

# _____________________________________________________________________

vectorTamaño10000 = [random.randint(1, 9) for _ in range(10000)]
print(f"El vector tamaño 10000 es: {vectorTamaño10000}")
print(f"El número que más se repite en el vector de tamaño 10000 es: {encuentra_mas_repetido(vectorTamaño10000)}")


