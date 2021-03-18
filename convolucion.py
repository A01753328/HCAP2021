import numpy as np

def convolucion(imagenO, kernel):
    fr = len(imagenO) - (len(kernel)-1)
    cr = len(imagenO[0]) - (len(kernel[0])-1)
    matrizR = np.zeros((fr,cr))

    #For para recorrer filas
    for i in range(len(matrizR)):
        #For para recorrer columnas
        for j in range(len(matrizR[0])):
            suma = 0
            #for para calcular las multiplicaciones y las sumas
            for m in range(len(kernel)):
                for n in range(len(kernel[0])):
                    suma += kernel[m][n] * imagenO[m+i][n+j]
            matrizR[i][j] = suma
    return matrizR

K = [[-1,0,1],[-1,0,1],[-1,0,1]]
I = [[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]

#imagenes de numpy arrays

In = np.array(I)
Kn = np.array(K)

#funcion de convolucion
R = convolucion(In,Kn)
print(R)

            
