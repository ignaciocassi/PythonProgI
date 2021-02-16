"""Escribir un programa que permita ingresar una cadena de caracteres e imprima un
mensaje indicando cuántas letras y cuántos números contiene. Por ejemplo, si se
ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números."""

def contarletnum():
    'Pide una cadena por teclado e imprime cuantas letras y números contiene:'
    cadena=input("Ingrese una cadena para contar sus letras y números: ")
    num=0
    let=0
    for i in cadena:
        if i.isdigit():
            num+=1
        elif i.isalpha():
            let+=1
    print("La cadena ingresada contiene: ",num," números y ",let," letras.")
    
def __main__():
    contarletnum()

if __name__=="__main__":
    __main__()