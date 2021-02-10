import math

class NumeroNegativo(Exception):
    pass

def RaizCuadrada():
    while True:
        try:
            numero=int(input("Ingrese un número para calcular su raíz cuadrada: "))
            if numero<=0:
                raise NumeroNegativo
            raiz=math.sqrt(numero)
            break
        except ValueError:
            print("No se ha ingresado un número.")
        except NumeroNegativo:
            print("El número ingresado es negativo. ")
    return raiz

print(RaizCuadrada())
    