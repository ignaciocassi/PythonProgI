"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares.
Escribir además un programa que permita verificar su funcionamiento"""

def cadenacapicua(cad):
    mitad=len(cad)//2
    inicio=0
    fin=len(cad)
    capicua=True
    while inicio<mitad and capicua==True:
        if (cad[inicio:inicio+1] == cad[fin-1:fin]):
            capicua=True
            inicio+=1
            fin-=1
        else:
            capicua=False
    return capicua
            
def __main__():
    cad=input("Ingrese una cadena: ")
    print(cadenacapicua(cad))
    
if __name__ == "__main__":
    __main__()