"""Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales,
sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""

def numeroreal(A,B):
    try:
        numero=int(A)+int(B)
    except ValueError:
        numero=-1
    return numero
        
def __main__():
    A=input("Ingrese el número A")
    B=input("Ingrese el número B")
    numero=numeroreal(A,B)
    print(numero)
    
if __name__=="__main__":
    __main__()
    