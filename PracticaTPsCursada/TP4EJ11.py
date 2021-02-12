""". Escribir un programa que permita ingresar una cadena de caracteres y coloque en
mayúscula la primera letra posterior a un espacio, eliminando todos los espacios
que contenga. Imprimir por pantalla la cadena obtenida."""

def capitalizar():
    'Pide una cadena por teclado y devuelve una subcadena con cada palabra con su primer letra en mayús. y sin espacios.'
    cadena=input("Ingese una cadena: ")
    lista=cadena.split()
    for i in range(len(lista)):
        lista[i]=lista[i].capitalize()
    subcadena="".join(lista)
    return subcadena
    
def __main__():
    subcadena=capitalizar()
    print(subcadena)
    
if __name__=="__main__":
    __main__()