def leerArchivo(directorio):
    """Lee una sola vez el archivo y devuelve una cadena que contiene todas las líneas del archivo"""
    try:
        arch=open(directorio,"rt")
        lineasArchivo=arch.read()
        return lineasArchivo
    except IOError:
        print("Error al abrir el archivo. ")
    finally:
        try:
            arch.close()
        except:
            pass

def contarCaracteres(palabra,contador=0):
    """Funcion recursiva: Recibe una cadena y dedvuelve la cantidad de caracteres de la misma"""
    if contador==len(palabra):
        return contador
    else:
        contador+=1
        return contarCaracteres(palabra,contador)

def filtrarLineas(lineasArchivo):
    """Crea una lista con las palabras que contiene la cadena palabras que tengan 3 o mas caracteres
    y para cada palabra: las convierte a minuscula
    quita las puntuaciones y cuenta las apariciones.
    Devuelve un diccionario: "palabra"=repeticiones """
    palabras=lineasArchivo.split("\n")
    datos=dict()
    for palabra in palabras:
        palabra=palabra.lower()
        palabra="".join([letra for letra in palabra if letra.isalpha()])
        cantCaracteres=contarCaracteres(palabra)
        if cantCaracteres>=3:
            if palabra not in datos:
                datos[palabra]=1
            else:
                datos[palabra]=datos[palabra]+1
    return datos

def mostrarDatos(datos):
    items=list(datos.items())
    items.sort(key=lambda x:x[0])
    for item in items:
        print("Palabra: "+item[0]+" Apariciones: "+str(item[1])+".")

def crearMatriz(N=3):
    matriz=[]
    for fila in range(N):
        matriz.append([])
        for columna in range(N):
            matriz[fila].append(0)
    fila=0
    columna=0
    valor=1
    matriz[fila][columna]=valor
    while(valor<N*N):
        if valor%2!=0:
            #Si es impar baja
            valor+=1
            if fila+1!=N:
                fila+=1
                matriz[fila][columna]=valor
            else:
                columna+=1
                matriz[fila][columna]=valor
        elif valor%2==0:
            #Si es par va a la derecha
            valor+=1
            fila-=1
            if columna+1!=N:
                columna+=1
                if matriz[fila][columna]==0:
                    matriz[fila][columna]=valor
                else:
                    fila+=1
                    matriz[fila][columna]=valor
            else:
                fila=fila+2
                columna=columna-(N-1)
                if fila==N:
                    break
                else:
                    matriz[fila][columna]=valor
    return matriz

def mostrarMatriz(matriz):
    for fila in matriz:
        print(fila)

def quitarDuplicados(lista,nuevaLista=[],indice=0):
    if indice==len(lista):
        return nuevaLista
    else:
        if lista[indice] not in nuevaLista:
            nuevaLista.append(lista[indice])
            indice+=1
        else:
            indice+=1
        return quitarDuplicados(lista,nuevaLista,indice)

def __main__():
    print("Ejercicio 1: ")
    print("")
    directorio=r"C:/Users/Nacho/Desktop/Python/Práctica/ProgI/ProgI/frases.txt"
    lineasArchivo=leerArchivo(directorio)
    datos=filtrarLineas(lineasArchivo)
    mostrarDatos(datos)
    print("")

    print("Ejercicio 2:")
    print("")
    try:
        N=int(input("Ingrese las dimensiones de la matriz (N): "))
        matriz=crearMatriz(N)
    except:
        matriz=crearMatriz()
    mostrarMatriz(matriz)
    print("")

    print("Ejericico 3: ")
    print("Lista original: ")
    lista=[1,2,2,3,4,4,5,6,7,7]
    print(lista)
    print("")
    print("Lista sin duplicados: ")
    lista=quitarDuplicados(lista)
    print(lista)
    

if __name__=="__main__":
    __main__()