from random import randint
import os

def clear():
    os.system("cls")

"""TP2EJ3 Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista."""
def listarCuadrados():
    while True:
        try:
            N=int(input("Ingrese el número N o -1 para salir: "))
            if N<=0 and N!=-1:
                print("El número debe ser positivo: ")
            elif (N==-1):
                print("Saliendo del programa.")
                break
            else:
                if N!=-1:
                    lista=[]
                    for i in range(0,N):
                        lista.append(i**3)
                    print(lista[-10:])
                else:
                    pass
                break
        except ValueError:
            print("Debe ingresarse un número, reintente...")

"""Definir una función superposición() que reciba como parámetros dos listas de cualquier tipo y devuelva True si tienen al menos un elemento en común, o False en
caso contrario. Desarrollar un programa para verificar su comportamiento."""
def superposicion(listaA,listaB):
    superp=False
    for item in listaA:
        if item in listaB:
            superp=True
            break
    return superp

"""Escribir un programa que calcule la suma acumulada a partir de una lista de números. El programa debe generar una nueva lista donde el primer elemento es el mismo de la lista original, 
el segundo elemento es la suma del primero más el segundo, el tercer elemento es la suma del primero más el segundo más el tercero y así
sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6]."""
def sumaAcumulada(lista):
    nuevalista=[]
    suma=0
    for numero in lista:
        nuevalista.append(numero+suma)
        suma=suma+numero
    return nuevalista

"""Eliminar de una lista de palabras las palabras que se encuentren en una segunda
lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante."""
def eliminarPalabrasDeCadena(cadena,eliminar):
    palabras=cadena.split(" ")
    for indice in range(len(palabras)):
        if palabras[indice] in eliminar:
            palabras.pop(indice)
    return " ".join(palabras)

"""Desarrollar una función que reciba como parámetros dos números enteros y devuelva el número que resulte de concatenar ambos valores. Por ejemplo, si recibe
1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no
vistas en clase."""
def concatenar(numeroA,numeroB):
    return str(numeroA)+str(numeroB)

""" Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con
los elementos de la primera que sean impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla. """
def tomarImpares():
    numeros=[randint(1,100) for numero in range(10)]
    impares=[elemento for elemento in numeros if elemento%2!=0]
    return impares

def crearMatriz():
    dimensiones=int(input("Ingrese el tamaño de la matriz: "))
    matriz=[]
    for fila in range(dimensiones):
        matriz.append([])
        for columna in range(dimensiones):
            matriz[fila].append(int(input("Ingrese un número:")))
    return matriz

def mostrarMatriz(matriz):
    for fila in range(len(matriz)):
        print(matriz[fila])

def ordenarFilasMatriz(matriz):
    for fila in range(len(matriz)):
        matriz[fila].sort()

def intercambiarFilas(matriz):
    while True:
        try:
            mostrarMatriz(matriz)
            print("")
            print("La matriz tiene "+str(len(matriz))+" filas: "+str([numero for numero in range(0,(len(matriz)))]))
            print("")
            filaA=int(input("Ingrese una fila para intercambiarla con otra: "))
            filaB=int(input("Ingrese la otra fila: "))
            matriz[filaA],matriz[filaB]=matriz[filaB],matriz[filaA]
            break
        except ValueError:
            print("Deben ingresarse números, reintente... ")
        except IndexError:
            print("Las filas ingresadas no existen, reintente... ")
    
def intercambiarColumnas(matriz):
    while True:
        try:
            mostrarMatriz(matriz)
            print("")
            print("La matriz tiene "+str(len(matriz[0]))+" columnas: "+str([numero for numero in range(0,(len(matriz[0])))]))
            print("")
            columnaA=int(input("Ingrese una fila para intercambiarla con otra: "))
            columnaB=int(input("Ingrese la otra fila: "))
            for fila in range(len(matriz)):
                matriz[fila][columnaA],matriz[fila][columnaB]=matriz[fila][columnaB],matriz[fila][columnaA]
            break
        except ValueError:
            print("Deben ingresarse números, reintente... ")
        except IndexError:
            print("Las filas ingresadas no existen, reintente... ")

def intercambiarColumnasComplicado(matriz):
    while True:
        try:
            print("La matriz original: ")
            print("")
            mostrarMatriz(matriz)
            print("")
            print("La matriz tiene "+str(len(matriz[0]))+" columnas: "+str([numero for numero in range(0,(len(matriz[0])))]))
            print("")
            columnaA=int(input("Ingrese una fila para intercambiarla con otra: "))
            columnaB=int(input("Ingrese la otra fila: "))
            clear()
            for fila in range(len(matriz)):
                aux=matriz[fila][columnaA]
                matriz[fila][columnaA]=matriz[fila][columnaB]
                matriz[fila][columnaB]=aux
            break
        except ValueError:
            print("Deben ingresarse números, reintente... ")
        except IndexError:
            print("Las filas ingresadas no existen, reintente... ")
            
def intercambiarFilaporColumna(matriz):
    """Solicita una fila y una columna de la matriz por teclado, y las intercambia."""
    fila=int(input("Ingrese una fila: "))
    columna=int(input("Ingrese una columna:"))
    ultimafila=len(matriz[0])-1
    for i in range(len(matriz)-1):
        aux=matriz[fila][i]
        matriz[fila][i]=matriz[ultimafila][columna]
        matriz[ultimafila][columna]=aux
        ultimafila-=1
        
def interponerMatriz(matriz):
    for f in range(len(matriz)//2+1):
        for c in range(len(matriz[0])):
            aux=matriz[f][c]
            matriz[f][c]=matriz[c][f]
            matriz[c][f]=aux
    
def __main__():
    #listarCuadrados()
    #print(superposicion([1,2,3],[4,5,6]))
    #print(sumaAcumulada([1,2,3,4,5]))
    #cadena=input("Ingrese la frase: ")
    #eliminar=input("Ingrese las palabras a eliminar de la frase: ")
    #print(eliminarPalabrasDeCadena(cadena,eliminar))
    #print(concatenar(1234,5678))
    #print(tomarImpares())
    matriz=crearMatriz()
    #ordenarFilasMatriz(matriz)
    #intercambiarFilas(matriz)
    #intercambiarColumnasFacil(matriz)
    #intercambiarColumnasComplicado(matriz)
    #intercambiarFilaporColumna(matriz)
    interponerMatriz(matriz)
    mostrarMatriz(matriz)
    
    
if __name__=="__main__":
    __main__()