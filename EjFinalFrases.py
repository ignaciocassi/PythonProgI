def leerArchivo(directorio):
    """Lee el archivo una vez y obtiene todas sus palabras en una cadena."""
    try:
        arch=open(directorio,"rt")
        lineasarchivo=arch.read()
        return lineasarchivo
    except IOError:
        print("Error al intentar abrir el archivo. ")
    finally:
        try:
            arch.close()
        except:
            pass
    
def obtenerLineas(lineasarchivo):
    """Recibe todas las palabras del archivo en una cadena, obtiene cada linea en una lista, borra el salto de línea y las convierte a minúscula finalmente devuelve la lista."""
    lineas=lineasarchivo.split("\n")
    for i in range(len(lineas)):
        lineas[i]=lineas[i].replace("\n","")
        lineas[i]=lineas[i].lower()
    return lineas

def obtenerDatosLineas(lineas):
    """Para cada linea: quita los caracteres no alfabeticos, cuenta los caracteres mediante funcion recursiva y si son más de 3: verifica si existen en dicc
    para contar sus repeticiones. """
    datos=dict()
    for i in range(len(lineas)):
        linealimpia="".join([item for item in lineas[i] if item.isalpha()]) #Obtiene la cadena sin puntuacion
        lineas[i]=linealimpia                                           #La reemplaza en la lista
        caracteres=contarCaracteresRecursiva(lineas[i])                 #Cuenta los caract
        if caracteres>3:                                                #Si la palabra tiene más de 3 caracteres
            if lineas[i] not in datos:
                datos[lineas[i]]=1
            else:
                datos[lineas[i]]+=1
    return datos
            
def mostrarDatosLineas(datos):
    """Ordena alfabeticamente el diccionario con los datos y para cada palabra: muestra la misma y sus repeticiones."""
    listadatos=list(datos.items())
    listadatos.sort(key=lambda item:item[0])
    for i in range(len(listadatos)):
        print("Palabra: "+listadatos[i][0]+" Repeticiones: "+str(listadatos[i][1])+".")

def contarCaracteresRecursiva(cadena,caracteres=0):
    """Cuenta los caracteres de una palabra mediante un contador(caracteres) que se incrementa en cada ejecución de la función recursiva.
    Caso base: caracteres es igual al largo de la cadena"""
    if caracteres==len(cadena):
        return caracteres
    else:
        caracteres+=1
        return contarCaracteresRecursiva(cadena,caracteres)
    
def crearMatriz(N=3):
    matriz=[]
    for f in range(N):
        matriz.append([])
        for c in range(N):
            matriz[f].append(0)
    fila=0
    filas=1
    contador=0
    numero=1
    while contador<N*N:
        while contador<N:
            matriz[][contador]=numero
        fila+=1
        filas+=1
    mostrarMatriz(matriz)
    
def mostrarMatriz(matriz):
    for fila in range(len(matriz)):
        print(matriz[fila])
def __main__():
    #Ejercicio 1
    print("Ejercicio 1: ")
    print("")
    lineasarchivo=leerArchivo(r"C:\Users\Nacho\Desktop\frases.txt")
    lineas=obtenerLineas(lineasarchivo)
    datos=obtenerDatosLineas(lineas)
    mostrarDatosLineas(datos)
    print("")
    
    #Ejercicio 2
    crearMatriz(4)
    
    
if __name__=="__main__":
    __main__()