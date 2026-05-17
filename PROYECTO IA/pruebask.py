from entrenamiento import *
import numpy as np

#valores de k a analizar
k = [3,7,9,51]

#se carga el archivo de entrenamiento
df = cargarDatos("rsTrain.dat")
print("Numero de filas leídas: ", len(df))
print("Tamaño de conjunto de entramiento (75%): ", len(df.iloc[:150]))
print("Tamaño de conjunto de prueba (25%): ", len(df.iloc[150:]))

for i in k:

    #pruebas
    puntaje = []
    for j in range(30):

        #barajear y seleccionar conjuntos de entreamiento y prueba para cada iteración
        #se deben resetar los indices, si no, no sirve de nada barajear
        df = df.sample(frac=1).reset_index(drop=True)
        aciertos = 0
        #hasta 150 para tomar el 75% del conjunto
        PuntosEntrenamiento = df.iloc[:150]
        #de 150 en adelante para tomar el 25%
        PuntosPrueba = df.iloc[150:]

        #probar clasificación
        
        for l in range(len(PuntosPrueba)):
            #convertir la fila en un objeto iterable (solo hasta el indice 3 debido a que el 4 ocupa el valor de clase)
            x = PuntosPrueba.iloc[l, :4].to_numpy()
            #se obtiene el valor real de la clase de la fila actual para comparar la si el modelo acertó o no
            yVerdadera = PuntosPrueba.iloc[l, 4]
            yresultado = knn_vectorizado(PuntosEntrenamiento.iloc[:, :4], PuntosEntrenamiento.iloc[:, 4], x, i)
            if(yresultado == yVerdadera):
                aciertos += 1
        porcentajeAciertos = (aciertos/50) * 100
        puntaje.append(porcentajeAciertos)

    mejor = np.max(puntaje)
    peor = np.min(puntaje)
    media = np.mean(puntaje)
    desviacion = np.std(puntaje)

    #imprimimos resultados
    print("Valor de K:", i)
    print("Mejor:", mejor)
    print("Peor:", peor)
    print("Media:", media)
    print("Desviación estándar:", desviacion, "\n\n")

