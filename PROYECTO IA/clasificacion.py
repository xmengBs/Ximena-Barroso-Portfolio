import numpy as np
import matplotlib.pyplot as plt
from entrenamiento import *

#cargamos las bandas
b1 = np.fromfile("band1.irs", dtype=np.uint8).reshape((512, 512))
b2 = np.fromfile("band2.irs", dtype=np.uint8).reshape((512, 512))
b3 = np.fromfile("band3.irs", dtype=np.uint8).reshape((512, 512))
b4 = np.fromfile("band4.irs", dtype=np.uint8).reshape((512, 512))

#cargamos el archivo .dat
datos = cargarDatos("rsTrain.dat")

Xen = datos.iloc[:, :4].to_numpy()  # características
yen= datos.iloc[:, 4].to_numpy()   # clases


filas, columnas = b1.shape
#se crea una matriz inicial compuesta de ceros
imagen_clasificada = np.zeros((filas, columnas), dtype=np.uint8)


for i in range(filas):
    for j in range(columnas):
        pixel = np.array([b1[i, j], b2[i, j], b3[i, j], b4[i, j]])
        clase = knn_vectorizado(Xen, yen, pixel, k=51) 
        imagen_clasificada[i, j] = clase




plt.imshow(imagen_clasificada, cmap='gray')
plt.title('Clasificación KNN')
plt.show()