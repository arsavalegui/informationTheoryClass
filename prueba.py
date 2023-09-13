
import math

def calcular_entropia(datos):
    """
    Calcula la entropía de un conjunto de datos.

    :param datos: Una lista de valores que representan el conjunto de datos.
    :return: El valor de entropía.
    """
    entropia = 0
    total = len(datos)

    if total == 0:
        return entropia

    # Calcula la frecuencia de cada valor en el conjunto de datos.
    frecuencias = {}
    for valor in datos:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1

    print(frecuencias)

    # Calcula la entropía usando la fórmula de la entropía de Shannon.
    for frecuencia in frecuencias.values():
        probabilidad = frecuencia / total
        entropia -= probabilidad * math.log2(probabilidad)


    return entropia

# Ejemplo de uso:
conjunto_de_datos = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
entropia_resultante = calcular_entropia(conjunto_de_datos)
print("Entropía del conjunto de datos:", entropia_resultante)
