"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""

def subcadena(cadena,N):
    'Devuelve los últimos N caracteres de una cadena'
    inic=len(cadena)-N
    subcadena=cadena[inic:]
    return subcadena

def __main__():
    cad=subcadena(input("ingrese una cadena: "),int(input("Ingrese el número N: ")))
    print(cad)
    
if __name__=="__main__":
    __main__()