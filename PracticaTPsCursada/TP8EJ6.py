def CrearLista():
    lista=[]
    entrada=int(input("Ingrese un número para agregar a la lista: "))
    while entrada!=-1:
        lista.append(entrada)
        entrada=int(input("Ingrese un número para agregar a la lista: "))
    return lista

def BuscarValor(lista):
    errores=0
    while True:
        try:
            while errores<3:
                entrada=int(input("Ingrese un número para buscarlo en la lista: "))
                print("El valor: ",entrada," se encontró en la posición número ",lista.index(entrada)," de la lista.")
            break
        except ValueError:
            print("No se encontró el número en la lista.")
            errores+=1
            pass
    
lista=CrearLista()
BuscarValor(lista)
    