""". Escribir una función que reciba un número entero N y devuelva un diccionario con
la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar
la función."""

def funcion(N):
    dic={}
    contador=0
    while contador<=12:
        multiplicacion=N*contador
        print(N,"*",contador,"=",multiplicacion)
        contador+=1
        
funcion(5)