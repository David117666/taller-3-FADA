import random

def stooge_sort(arr, i=0, j=None):


    if j is None:
        j = len(arr) - 1

    if arr[i] >= arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

    if i + 1 >= j:
        return

    k = (j - i + 1) // 3
    stooge_sort(arr, i, j - k)
    stooge_sort(arr, i + k, j)
    stooge_sort(arr, i, j - k)

    return arr

# Ejemplo de uso vectores de tamaño 10 , 100 , 1000 y 10000

vectorTamaño10 = [random.randint(1, 9) for _ in range(10)]
print(f"El arreglo de tamaño 10 ordenado:{stooge_sort(vectorTamaño10)}")

# _____________________________________________________________________

vectorTamaño100 = [random.randint(1, 9) for _ in range(100)]
print(f"El arreglo de tamaño 100 ordenado: {stooge_sort(vectorTamaño100)}")

# _____________________________________________________________________

vectorTamaño1000 = [random.randint(1, 9) for _ in range(1000)]
print(f"El arreglo de tamaño 1000 ordenado: {stooge_sort(vectorTamaño1000)}")

# _____________________________________________________________________

vectorTamaño10000 = [random.randint(1, 9) for _ in range(10000)]
print(f"El arreglo de tamaño 10000 ordenado: {stooge_sort(vectorTamaño10000)}")
