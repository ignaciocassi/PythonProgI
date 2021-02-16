"""Escribir una función que reciba como parámetro una cadena de caracteres en la
que las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada
una."""

def corregirespacios(cadena):
    'Recibe una cadena como parámetro y la devuelve ordenada alfabeticamente con sólo un espacio entre cada palabra.'
    lista=cadena.split()
    lista.sort()
    cadenares=" ".join(lista)
    return cadenares


def __main__():
    cadena=input("Ingese una cadena para corregir sus espacios y ordenarla albabeticamente: ")
    cadenares=corregirespacios(cadena)
    print(cadenares)
    
if __name__=="__main__":
    __main__()