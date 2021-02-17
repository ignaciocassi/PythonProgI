"""Los números de claves de dos cajas fuertes están intercalados dentro de un nú-mero entero llamado "clave maestra",
cuya longitud no se conoce. Realizar un pro-grama para obtener ambas claves,
donde la primera se construye con los dígitos impares de la clave maestra y la segunda con los dígitos pares.
Los dígitos se numeran desde la izquierda. Ejemplo: Si clave maestra = 18293, la clave 1 sería 123 y la clave 2
sería 89."""

def obtenerclaves(clavemaestra):
    clave1=clavemaestra[0::2]
    clave2=clavemaestra[1::2]
    return clave1,clave2

def __main__():
    clavemaestra=input("Ingrese la clave maestra: ")
    clave1,clave2=obtenerclaves(clavemaestra)
    print("La clave1 es: ",clave1," y la clave 2 es: ",clave2,".")

if __name__ == "__main__":
    __main__()