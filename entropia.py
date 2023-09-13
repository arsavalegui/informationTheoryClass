import random
import math 

def entropia(datos):

    entropia = 0

    total = len(datos)
    umbral = [1,9,12,7,9,18]

    if total == 0:
        return entropia

    frecuencias = {}
    
    for valor in umbral:
        conteo = datos.count(valor)
        if conteo > 0:
            frecuencias[valor] = conteo

    print(frecuencias)

    for frecuencia in frecuencias.values():
        prob = frecuencia/total
        entropia -= prob * math.log2(prob)

    return entropia

datos = [random.randint(1, 20) for _ in range(20)]
# datos = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

print(f"El conjunto de datos es: {datos}")
print("La entropia es: ", entropia(datos))
