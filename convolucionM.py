import numpy as np
import cv2

def convolucion(imagenO, kernel):
    fr = len(imagenO) - (len(kernel)-1)
    cr = len(imagenO[0]) - (len(kernel[0])-1)
    matrizR = np.zeros((fr,cr),np.uint8)

    #For para recorrer filas
    for i in range(len(matrizR)):
        #For para recorrer columnas
        for j in range(len(matrizR[0])):
            suma = 0
            #for para calcular las multiplicaciones y las sumas
            for m in range(len(kernel)):
                for n in range(len(kernel[0])): 
                    suma += kernel[m][n] * imagenO[m+i][n+j]
            if suma<=255:    
                matrizR[i][j] = round(suma)
            else:
                matrizR[i][j] = 255     
    return matrizR  

#imagenes  
K = [[-1,0,1],[-1,0,1],[-1,0,1]]
I = [[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]   

#imagenes de numpy ar
In = np.array(I)
Kn = np.array(K)
IRGB = cv2.imread("R2D2.jpg")       
IGS = cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)                                 
print(IGS.shape)

#funcion de convolucion                         
R = convolucion(IGS,Kn) 
print(R)
cv2.imwrite("R2D2C.jpg",R)

