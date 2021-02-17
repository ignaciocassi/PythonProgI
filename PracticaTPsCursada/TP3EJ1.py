def matrizteclado():
    F=int(input("Ingrese las filas de la matriz: "))
    C=int(input("Ingrese las columnas de la matriz: "))
    matriz=[]
    for f in range(F):
        matriz.append([])
        for c in range(C):
            matriz[f].append(int(input("Ingrese un número: ")))
    return matriz

def ordenarfilas(matriz):
    for f in range(len(matriz)):
        matriz[f].sort()

def intercambiarfilas(matriz,fila1,fila2):
    aux=matriz[fila1]
    matriz[fila1]=matriz[fila2]
    matriz[fila2]=aux
    
matriz=matrizteclado()
print(matriz)

def calcularpromedio(matriz,fila):
    

        




#ordenarfilas(matriz)
#print(matriz)
#intercambiarfilas(matriz,1,2)
#print(matriz)
calcularpromedio(matriz,2)