"""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
éste sea correcto. Escribir también un programa que permita probar el correcto
funcionamiento de la misma"""

def numeronatural():
    error=True
    while error==True:
        try:
            N=int(input("Ingrese un número natural:"))
            error=False
        except ValueError:
            print("No se ingresó un número natural.")
            error=True
        if N<=0:
            raise NumeroNegativo("El número es negativo")
            error=True
    print("El número ingresado es: ",N)
    
numeronatural()