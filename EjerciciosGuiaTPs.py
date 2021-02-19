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
                        pass
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

def crearMatrizFullCeros():
    #dimensiones=int(input("Ingrese el tamaño de la matriz: "))
    dimensiones=4
    matriz=[]
    for fila in range(dimensiones):
        matriz.append([])
        for columna in range(dimensiones):
            matriz[fila].append(0)
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
    
"""Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro."""
def calcularPromedioFila(matriz,fila):
    cantidad=0
    suma=0
    for numero in range(len(matriz[fila])):
        cantidad+=1
        suma+=matriz[fila][numero]
    promedio=suma/cantidad
    return promedio

"""Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
"""
def calcularPorcentajeImparEnColumna(matriz,columna):
    total=0
    impares=0
    for i in range(len(matriz[0])):
        if matriz[i][columna]%2!=0:
            impares+=1
        total+=1
    porcentajeImpar=(impares*100)/total
    return porcentajeImpar

"""Determinar si la matriz es simétrica con respecto a su diagonal principal."""
def simetriaDiagonalPrincipalMatriz(matriz):
    simetria=True
    primero=0
    ultimo=len(matriz)-1
    for i in range(len(matriz)//2):
        if matriz[primero][primero]==matriz[ultimo][ultimo]:
            simetria=True
            primero+=1
            ultimo-=1
        else:
            simetria=False
            break
    return simetria

"""Determinar si la matriz es simétrica con respecto a su diagonal secundaria."""

def simetriaDiagonalSecundariaMatriz(matriz):
    simetria=True
    primero=0
    ultimo=len(matriz)-1
    for i in range(len(matriz)//2):
        if matriz[primero][ultimo]==matriz[ultimo][primero]:
            primero+=1
            ultimo-=1
            simetria=True
        else:
            simetria=False
            break
    return simetria

def columnasCapicuasMatriz(matriz):
    colCapicuas=[]
    for columna in range(len(matriz[0])):
        primeraFila=0
        capicua=False
        ultimaFila=len(matriz)-1
        while primeraFila<ultimaFila:
            if matriz[primeraFila][columna]==matriz[ultimaFila][columna]:
                primeraFila+=1
                ultimaFila-=1
                capicua=True
            else:
                capicua=False
                break
        if capicua==True:
            colCapicuas.append(columna)
    return colCapicuas

def crearMatriz1():
    matriz=crearMatrizFullCeros()
    indice=0
    valor=1
    for fila in range(len(matriz)):
        matriz[fila][indice]=valor
        indice+=1
        valor+=2
    mostrarMatriz(matriz)

def crearMatriz2():
    matriz=crearMatrizFullCeros()
    indice=len(matriz[0])-1
    valor=27
    for fila in range(len(matriz)):
        matriz[fila][indice]=valor
        indice-=1
        valor=valor//3
    mostrarMatriz(matriz)
    
def crearMatriz3():
    matriz=crearMatrizFullCeros()
    valor=4
    limite=1
    for fila in range(len(matriz)):
        for col in range(limite):
            matriz[fila][col]=valor
        limite+=1
        valor-=1
    mostrarMatriz(matriz)

def crearMatriz4():
    matriz=crearMatrizFullCeros()
    valor=1
    for fila in range(len(matriz)-1,-1,-1):
        for col in range(len(matriz[0])):
            matriz[fila][col]=valor
        valor=valor*2
    mostrarMatriz(matriz)

def crearMatriz5():
    matriz=crearMatrizFullCeros()
    valor=1
    entrarEn0=False
    for fila in matriz:
        if entrarEn0==False:
            for i in range(len(fila)):
                if i%2==0:
                    pass
                else:
                    fila[i]=valor
                    valor+=1
            entrarEn0=True
        else:
            for i in range(len(fila)):
                if i%2==0:
                    fila[i]=valor
                    valor+=1
                else:
                    pass
            entrarEn0=False
    mostrarMatriz(matriz)

def crearMatriz6():
    matriz=crearMatrizFullCeros()
    hasta=len(matriz)-2
    valor=1
    for fila in matriz:
        for i in range(len(fila)-1,hasta,-1):
            fila[i]=valor
            valor+=1
        hasta-=1
    mostrarMatriz(matriz)

def crearMatriz7():
    matriz=crearMatrizFullCeros()
    valor=1
    fila=0
    columna=0
    while valor<=16:
        while(columna<=len(matriz[0])-1 and matriz[fila][columna]==0):
            matriz[fila][columna]=valor
            valor+=1
            if columna+1!=len(matriz[0]):
                columna+=1
        fila+=1
        while(fila<=len(matriz)-1 and matriz[fila][columna]==0):
            matriz[fila][columna]=valor
            valor+=1
            if fila+1!=len(matriz):
                fila+=1
        columna-=1
        while(columna>=0 and matriz[fila][columna]==0):
            matriz[fila][columna]=valor
            valor+=1
            if columna-1!=-1:
                columna-=1
        fila-=1
        while(matriz[fila][columna]==0):
            matriz[fila][columna]=valor
            valor+=1
            if matriz[fila-1][columna]==0:
                fila-=1
        columna+=1
    mostrarMatriz(matriz)

def cadenaCapicua(cadena):
    capicua=False
    primeraletra=0
    ultimaletra=len(cadena)-1
    while primeraletra<len(cadena)//2:
        if cadena[primeraletra:primeraletra+1]==cadena[ultimaletra:ultimaletra-1:-1]:
            capicua=True
            primeraletra+=1
            ultimaletra-=1
        else:
            capicua=False
            break
    return capicua

def mostrarCadenaCentrada():
    cadena=input("Ingrese una cadena para mostrarla centrada: ")
    print(cadena.center(80," "))

def obtenerClavesDeClaveMaestra():
    claveMaestra=input("Ingrese la clave maestra: ")
    clave1=claveMaestra[::2]
    clave2=claveMaestra[1::2]
    print(clave1)
    print(clave2)

def filtrarPalabrasNormal(frase,N):
    palabras=frase.split(" ")
    listaFraseFiltrada=[]
    for palabra in palabras:
        if len(palabra)>=N:
            listaFraseFiltrada.append(palabra)
    fraseFiltrada=" ".join(listaFraseFiltrada)
    return fraseFiltrada

def cantChars(palabra,N=4):
    if len(palabra)>=N:
        return True
    else:
        return False

def filtrarPalabrasFilter(frase,N):
    listaPalabras=frase.split(" ")
    listaPalabrasFiltradas=list(filter(cantChars,listaPalabras))
    fraseFiltrada=" ".join(listaPalabrasFiltradas)
    return fraseFiltrada

def filtrarPalabrasComprension(frase,N=4):
    listaPalabras=frase.split(" ")
    palabrasFiltradas=[palabra for palabra in listaPalabras if len(palabra)>=N]
    fraseFiltrada=" ".join(palabrasFiltradas)
    return fraseFiltrada

def extraerSubcadena(cadena,posSubcadena,cantCaractSubcadena):
    subcadena=cadena[posSubcadena:posSubcadena+cantCaractSubcadena]
    return subcadena

def extraerSubcadenaSinRebanadas(cadena,posSubcadena,cantCaractSubcadena):
    contador=0
    listaLetrasSubcadena=[]
    subadena=""
    for letra in cadena:
        if contador>=posSubcadena and contador<=posSubcadena+cantCaractSubcadena:
            listaLetrasSubcadena.append(letra)
            contador+=1
        else:
            contador+=1
    subcadena="".join(listaLetrasSubcadena)
    return subcadena

def eliminarSubcadena(cadena,posSubcadena,cantCaractSubcadena):
    listaLetrasCadena=list(cadena)
    print(listaLetrasCadena)
    listaLetrasCadena[posSubcadena:posSubcadena+cantCaractSubcadena]=[]
    subcadena="".join(listaLetrasCadena)
    return subcadena

def controlarEspaciosYOrdernarPalabras(cadena):
    lista=cadena.split()
    lista.sort()
    cadenaControlada=" ".join(lista)
    return cadenaControlada

def contarLetrasyNum(cadena):
    letras=0
    numeros=0
    for letra in cadena:
        if letra.isalpha():
            letras+=1
        elif letra.isdigit():
            numeros+=1
    return letras,numeros



def __main__():
    
    #listarCuadrados()
    #print(superposicion([1,2,3],[4,5,6]))
    #print(sumaAcumulada([1,2,3,4,5]))
    #cadena=input("Ingrese la frase: ")
    #eliminar=input("Ingrese las palabras a eliminar de la frase: ")
    #print(eliminarPalabrasDeCadena(cadena,eliminar))
    #print(concatenar(1234,5678))
    #print(tomarImpares())
    #matriz=crearMatriz()
    #ordenarFilasMatriz(matriz)
    #intercambiarFilas(matriz)
    #intercambiarColumnasFacil(matriz)
    #intercambiarColumnasComplicado(matriz)
    #intercambiarFilaporColumna(matriz)
    #interponerMatriz(matriz)
    #matriz=crearMatriz()
    #fila=int(input("Ingrese una fila para calcular su promedio: "))
    #promedio=calcularPromedioFila(matriz,fila)
    #print("El promedio de la fila "+str(fila)+" es: "+str(promedio)+".")
    #columna=int(input("Ingrese una columna: "))
    #porcentaje=calcularPorcentajeImparEnColumna(matriz,columna)
    #porcentaje=round(porcentaje,2)
    #print("El porcentaje de items impares en la columna "+str(columna)+" es del "+str(porcentaje)+"%")
    #print(simetriaDiagonalPrincipalMatriz(matriz))
    #print(simetriaDiagonalSecundariaMatriz(matriz))
    #print("Las columnas capicúas de la matriz son: "+str(columnasCapicuasMatriz(matriz)))
    #mostrarMatriz(matriz)
    #print("Matriz 1: ")
    #print("")
    #crearMatriz1()
    #print("")
    #print("Matriz 2: ")
    #print("")
    #crearMatriz2()
    #print("")
    #print("Matriz 3: ")
    #print("")
    #crearMatriz3()
    #print("")
    #print("Matriz 4: ")
    #print("")
    #crearMatriz4()
    #print("")
    #print("Matriz 5: ")
    #print("")
    #crearMatriz5()
    #print("")
    #print("Matriz 6: ")
    #print("")
    #crearMatriz6()
    #print("")
    #print("Matriz 7: ")
    #print("")
    #crearMatriz7()
    #print("")
    #print("Matriz 8: ")
    #print("")
    #crearMatriz8()
    #print("")
    #print(cadenaCapicua("abcdcba"))
    #mostrarCadenaCentrada()
    #obtenerClavesDeClaveMaestra()
    #print(filtrarPalabrasNormal("Hola soy Nacho",4))
    #print(filtrarPalabrasFilter("Hola soy Nacho",4))
    #print(filtrarPalabrasComprension("Hola soy Nacho",4))
    #cadena="El número de teléfono es 4356-7890"
    #posSubcadena=25
    #cantCaractSubcadena=9
    #print(eliminarSubcadena(cadena,posSubcadena,cantCaractSubcadena))
    #cadenaControlada=controlarEspaciosYOrdernarPalabras("hola soy  nacho  ahre    xd")
    #print(cadenaControlada)
    #cadena="letras 1234"
    #letras,numeros=contarLetrasyNum(cadena)
    #print("En la cadena '"+cadena+"' hay "+str(letras)+" letras y "+str(numeros)+" numeros.")

    
if __name__=="__main__":
    __main__()