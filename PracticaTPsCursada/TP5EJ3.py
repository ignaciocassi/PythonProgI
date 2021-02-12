"""Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones."""

def numeromes(N):
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    if N<=0 or N>12:
        raise NumeroMesInvalido("El número ingresado no corresponde a un mes válido.")
        devolver=""
    else:
        N=N-1
        if N==0:
            devolver=meses[0]
        elif N==1:
            devolver=meses[1]
        elif N==2:
            devolver=meses[2]
        elif N==3:
            devolver=meses[3]
        elif N==4:
            devolver=meses[4]
        elif N==5:
            devolver=meses[5]
        elif N==6:
            devolver=meses[6]
        elif N==7:
            devolver=meses[7]
        elif N==8:
            devolver=meses[8]
        elif N==9:
            devolver=meses[9]
        elif N==10:
            devolver=meses[10]
        elif N==11:
            devolver=meses[11]
    return devolver

cadena=numeromes(-1)
print(cadena)