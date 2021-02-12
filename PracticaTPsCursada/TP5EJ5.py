"""La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo"""

from math import sqrt

continuar=True
while continuar==True:
    try:
        N=int(input("Ingrese un número para calcular su raíz: "))
        raiz=sqrt(N)
        continuar=False
    except ValueError:
        print("No se ha ingresado un número natural.")
    print("Raiz: ",raiz)
    
    
        
