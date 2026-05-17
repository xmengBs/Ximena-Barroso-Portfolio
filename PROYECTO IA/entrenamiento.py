import numpy as np
import pandas as pd

#función para cargar los datos de entrenamiento
def cargarDatos(archivo):
    df = pd.read_csv(archivo, sep='\s+', encoding="utf-8", header=None)

    return df

#distancia eucludiana calculo, se hace hace debidp a que a y b son vectores con las caracteristicas y no se puede graficar debido a que es de 4 dimensiones
def distancia_euclidiana(a, b):
    return np.linalg.norm(a - b)

#Función de clasificación
def knn(Xen, x, k):
    distancia = []
    #calcular distancias convirtiendo el dataframe a vectores de numpy para poder recorrerlo, se guarda la distancia de ese vector y su clase para poder clasificar despues
    indice = 0
    for i in Xen.to_numpy():
        distancia.append((distancia_euclidiana(x, i[:4]), Xen.iloc[indice, 4]))
        indice += 1
    
    #ordenar de menor a mayor
    distancia = sorted(distancia, key=lambda i:i[0], reverse=False)

    #seleccionamos a los más cercanos en base a k, al k ser el limite y empezar desde 0, entonces se selecciona la cantidad k
    MasCercanos = distancia[:k]

    #contamos cual es la clase con más vecinos cercanos
    cero = 0
    uno = 0
    for i in MasCercanos:
        if(i[1] == 0):
            cero += 1
        else:
            uno +=1
        
    if cero > uno:
        return 0
    else:
        return 1 

def knn_vectorizado(Xen, Yen, x, k):
    # Calcular distancias de xen contra todo X (cada fila)
    distancias = np.linalg.norm(Xen - x, axis=1)
    
    # Obtener los índices de los k vecinos más cercanos
    idx = np.argpartition(distancias, k)[:k]
    
    # Contar las clases de esos k vecinos
    clases_k = Yen[idx].astype(int)
    counts = np.bincount(clases_k)
    
    # Devolver la clase mayoritaria
    return np.argmax(counts)