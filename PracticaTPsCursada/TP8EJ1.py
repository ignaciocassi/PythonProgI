class NoEsNatural(Exception):
    pass

class MenorQueCero(Exception):
    pass

def NumerosNaturales():
    while True:
        try:
            entrada=int(input("Ingrese un número natural: "))
            if entrada<=0:
                raise MenorQueCero
            else:
                break
        except ValueError:
            print("No se ha ingresado un número entero.")
        except MenorQueCero:
            print("Se ha ingresado un número menor que cero.")
    return entrada
            
print(NumerosNaturales())