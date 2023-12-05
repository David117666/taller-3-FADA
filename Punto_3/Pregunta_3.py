
import random

import time

# Quick-Sort
def  quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    pivote = arreglo[len(arreglo) // 2]
    izquierda = [x for x in arreglo if x < pivote]
    medio = [x for x in arreglo if x == pivote]
    derecha = [x for x in arreglo if x > pivote]

    return quicksort(izquierda) + medio + quicksort(derecha)

# Insertion-Sort
def insertion_sort(arreglo):
    n = len(arreglo)

    for i in range(1, n):
        valor_actual = arreglo[i]
        posicion = i

        while posicion > 0 and arreglo[posicion - 1] > valor_actual:
            arreglo[posicion] = arreglo[posicion - 1]
            posicion -= 1

        arreglo[posicion] = valor_actual

    return arreglo

# Merge-Sort

def merge_sort(arreglo):
    if len(arreglo) > 1:
        medio = len(arreglo) // 2
        izquierda = arreglo[:medio]
        derecha = arreglo[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arreglo[k] = izquierda[i]
                i += 1
            else:
                arreglo[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arreglo[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arreglo[k] = derecha[j]
            j += 1
            k += 1

    return arreglo


# Arreglos aleatorios para la tabla de comparacion

vectorTamaño10A = [random.randint(1, 9) for _ in range(10)]

vectorTamaño10B = [random.randint(1, 9) for _ in range(10)]

vectorTamaño10C = [random.randint(1, 9) for _ in range(10)]

# _____________________________________________________________________

vectorTamaño50A = [random.randint(1, 9) for _ in range(50)]

vectorTamaño50B = [random.randint(1, 9) for _ in range(50)]

vectorTamaño50C = [random.randint(1, 9) for _ in range(50)]
# _____________________________________________________________________

vectorTamaño100A = [random.randint(1, 9) for _ in range(100)]

vectorTamaño100B = [random.randint(1, 9) for _ in range(100)]

vectorTamaño100C = [random.randint(1, 9) for _ in range(100)]

# _____________________________________________________________________

vectorTamaño500A = [random.randint(1, 9) for _ in range(500)]

vectorTamaño500B = [random.randint(1, 9) for _ in range(500)]

vectorTamaño500C = [random.randint(1, 9) for _ in range(500)]

# _____________________________________________________________________

vectorTamaño1000A = [random.randint(1, 9) for _ in range(1000)]

vectorTamaño1000B = [random.randint(1, 9) for _ in range(1000)]

vectorTamaño1000C = [random.randint(1, 9) for _ in range(1000)]

# _____________________________________________________________________

vectorTamaño2000B = [random.randint(1, 9) for _ in range(2000)]

vectorTamaño2000A = [random.randint(1, 9) for _ in range(2000)]

vectorTamaño2000C = [random.randint(1, 9) for _ in range(2000)]

# _____________________________________________________________________

vectorTamaño5000A = [random.randint(1, 9) for _ in range(5000)]

vectorTamaño5000B = [random.randint(1, 9) for _ in range(5000)]

vectorTamaño5000C = [random.randint(1, 9) for _ in range(5000)]

# _____________________________________________________________________

vectorTamaño10000A = [random.randint(1, 9) for _ in range(10000)]

vectorTamaño10000B = [random.randint(1, 9) for _ in range(10000)]

vectorTamaño10000C = [random.randint(1, 9) for _ in range(10000)]

# _____________________________________________________________________



#_______________________________________________________________________
# Tiempos de ejecucion de los algoritmos de ordenamiento
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño10A)
fin_tiempo = time.time()
tiempo_ejecucion10A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño10B)
fin_tiempo = time.time()
tiempo_ejecucion10B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño10C)
fin_tiempo = time.time()
tiempo_ejecucion10C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño50A)
fin_tiempo = time.time()
tiempo_ejecucion50A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño50B)
fin_tiempo = time.time()
tiempo_ejecucion50B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño50C)
fin_tiempo = time.time()
tiempo_ejecucion50C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño100A)
fin_tiempo = time.time()
tiempo_ejecucion100A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño100B)
fin_tiempo = time.time()
tiempo_ejecucion100B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño100C)
fin_tiempo = time.time()
tiempo_ejecucion100C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño500A)
fin_tiempo = time.time()
tiempo_ejecucion500A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño500B)
fin_tiempo = time.time()
tiempo_ejecucion500B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño500C)
fin_tiempo = time.time()
tiempo_ejecucion500C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño1000A)
fin_tiempo = time.time()
tiempo_ejecucion1000A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño1000B)
fin_tiempo = time.time()
tiempo_ejecucion1000B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño1000C)
fin_tiempo = time.time()
tiempo_ejecucion1000C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño2000A)
fin_tiempo = time.time()
tiempo_ejecucion2000A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño2000B)
fin_tiempo = time.time()
tiempo_ejecucion2000B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño2000C)
fin_tiempo = time.time()
tiempo_ejecucion2000C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño5000A)
fin_tiempo = time.time()
tiempo_ejecucion5000A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño5000B)
fin_tiempo = time.time()
tiempo_ejecucion5000B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño5000C)
fin_tiempo = time.time()
tiempo_ejecucion5000C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño10000A)
fin_tiempo = time.time()
tiempo_ejecucion10000A = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño10000B)
fin_tiempo = time.time()
tiempo_ejecucion10000B = fin_tiempo - inicio_tiempo
#_______________________________________________________________________
inicio_tiempo = time.time()
quicksort(vectorTamaño10000C)
fin_tiempo = time.time()
tiempo_ejecucion10000C = fin_tiempo - inicio_tiempo
#_______________________________________________________________________


# Tabla de Comparacion de tiempos de ejecucion de los algoritmos de ordenamiento

print("______________________________________________________________________________________________________________\n")
print("     Algoritmo       |    Entrada (n)          |  Tiempo Real (segundos)    |   Complejidad      |    Constantes ")
print("       Nombre        |    Tamaño del Arreglo   |                            |                    |    ")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        10               | {tiempo_ejecucion10A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        10               | {tiempo_ejecucion10B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        10               | {tiempo_ejecucion10C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        10               | {tiempo_ejecucion10A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        10               | {tiempo_ejecucion10B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        10               | {tiempo_ejecucion10C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        10               | {tiempo_ejecucion10A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        10               | {tiempo_ejecucion10B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        10               | {tiempo_ejecucion10C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        50               | {tiempo_ejecucion50A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        50               | {tiempo_ejecucion50B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        50               | {tiempo_ejecucion50C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        50               | {tiempo_ejecucion50A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        50               | {tiempo_ejecucion50B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        50               | {tiempo_ejecucion50C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        50               | {tiempo_ejecucion50A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        50               | {tiempo_ejecucion50B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        50               | {tiempo_ejecucion50C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        100              | {tiempo_ejecucion100A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        100              | {tiempo_ejecucion100B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        100              | {tiempo_ejecucion100C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        100              | {tiempo_ejecucion100A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        100              | {tiempo_ejecucion100B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        100              | {tiempo_ejecucion100C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        100              | {tiempo_ejecucion100A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        100              | {tiempo_ejecucion100B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        100              | {tiempo_ejecucion100C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        500              | {tiempo_ejecucion500A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        500              | {tiempo_ejecucion500B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        500              | {tiempo_ejecucion500C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        500              | {tiempo_ejecucion500A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        500              | {tiempo_ejecucion500B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        500              | {tiempo_ejecucion500C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        500              | {tiempo_ejecucion500A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        500              | {tiempo_ejecucion500B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        500              | {tiempo_ejecucion500C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        1000             | {tiempo_ejecucion1000A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        1000             | {tiempo_ejecucion1000B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        1000             | {tiempo_ejecucion1000C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        1000             | {tiempo_ejecucion1000A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        1000             | {tiempo_ejecucion1000B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        1000             | {tiempo_ejecucion1000C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        1000             | {tiempo_ejecucion1000A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        1000             | {tiempo_ejecucion1000B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        1000             | {tiempo_ejecucion1000C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        2000             | {tiempo_ejecucion2000A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        2000             | {tiempo_ejecucion2000B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        2000             | {tiempo_ejecucion2000C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        2000             | {tiempo_ejecucion2000A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        2000             | {tiempo_ejecucion2000B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        2000             | {tiempo_ejecucion2000C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        2000             | {tiempo_ejecucion2000A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        2000             | {tiempo_ejecucion2000B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        2000             | {tiempo_ejecucion2000C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        5000             | {tiempo_ejecucion5000A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        5000             | {tiempo_ejecucion5000B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        5000             | {tiempo_ejecucion5000C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        5000             | {tiempo_ejecucion5000A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        5000             | {tiempo_ejecucion5000B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        5000             | {tiempo_ejecucion5000C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        5000             | {tiempo_ejecucion5000A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        5000             | {tiempo_ejecucion5000B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        5000             | {tiempo_ejecucion5000C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     quicksort       |        10000            | {tiempo_ejecucion10000A:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        10000            | {tiempo_ejecucion10000B:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print(f"     quicksort       |        10000            | {tiempo_ejecucion10000C:.20f}     |   O(n^2)           |    C1 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     insertion_sort  |        10000            | {tiempo_ejecucion10000A:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        10000            | {tiempo_ejecucion10000B:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print(f"     insertion_sort  |        10000            | {tiempo_ejecucion10000C:.20f}     |   O(n^2)           |    C2 = 0.0009999275207519531")
print("______________________________________________________________________________________________________________")
print(f"     merge_sort      |        10000            | {tiempo_ejecucion10000A:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        10000            | {tiempo_ejecucion10000B:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print(f"     merge_sort      |        10000            | {tiempo_ejecucion10000C:.20f}     |   O(n^2)           |    C3 = 0.0009999275207519531")
print("\n________________________________________________________________________________________________________________\n")
print("                                                                                                 |    Constante : ")
print("__________________________________________________________________________________________________________________")