def funcion(cad1,cad2):
    while True:
        try:
            num1=int(cad1)
            num2=int(cad2)
            suma=num1+num2
            break
        except ValueError:
            print("Error al intentar convertir una cadena a entero.")
            suma=-1
            break
    return suma

cad1="2"
cad2="3"
print(funcion(cad1,cad2))