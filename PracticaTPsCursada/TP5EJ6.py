"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda."""

def crearlista():
    lista=[]
    entrada=int(input("Ingrese un número para la lista: "))
    while entrada!=-1:
        lista.append(entrada)
        entrada=int(input("Ingrese un número para la lista: "))
    return lista

def buscarindice(lista):
    valores=[]
    errores=0
    entrada=int(input("Ingrese un número para buscar su posición en la lista: "))
    while entrada!=-1 and errores<3:
        try:
            posicion=lista.index(entrada)
            print("El valor ",entrada," se encontró en la posición: ",posicion," de la lista.")
        except ValueError:
            print("El valor no se encontró.")
            errores+=1
            pass
        entrada=int(input("Ingrese un número para buscar su posición en la lista: "))
    
def __main__():
    lista=crearlista()
    print("La lista creada es: ",lista)
    buscarindice(lista)
    
    
if __name__=="__main__":
    __main__()