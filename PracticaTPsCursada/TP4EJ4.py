"""Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y lo convierta en un número romano,
devolviéndolo en una cadena de caracteres. ¿En qué cambiaría la función si el rango de valores fuese diferente?"""

def numeroromano(numero):
    romano=""
    if numero<0 or numero>3999:
        devolver="El número ingresado es inválido"
    while numero>=1000:
        romano=romano+"M"
        numero-=1000
    while numero>=500:
        romano=romano+"D"
        numero-=500
    while numero>=100:
        romano=romano+"C"
        numero-=100
    while numero>=50:
        romano=romano+"L"
        numero-=50
    while numero>=10:
        romano=romano+"X"
        numero-=10
    while numero>=5:
        romano=romano+"V"
        numero-=5
    while numero>=1:
        romano=romano+"I"
        numero-=1
    return romano

def __main__():
    numero=int(input("Ingrese un número para convertirlo a romano:"))
    print(numeroromano(numero))
    
if __name__=="__main__":
    __main__()