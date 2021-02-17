"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N,
y devuelva otra cadena con las palabras que tengan N o más caracteres.
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función,
para cada uno de los siguientes casos:
a.Utilizando sólo ciclos normales. (con split) -
b.Utilizando listas por comprensiónc.
c.Utilizando la función filter. (se ve la prox clase) """

def filtrar_palabras_comprension(frase,N):
    lista =[x for x in frase.split() if len(x)>=N]
    return lista
    
def filtrar_palabras_normal(frase,N):
    palabras = frase.split()
    largas = []
    for i in range(len(palabras)):
        if len(palabras[i])>=N:
            largas.append(palabras[i])
    return largas

def filtrar_mas_largas_que_3(iterable):
    for i in range(len(iterable)):
        if len(iterable[i])>=3:
            return True
        else:
            return False

def __main__():
    frase=input("Ingrese la frase a filtrar: ")
    palabras=frase.split()
    filtradas=list(filter(filtrar_mas_largas_que_3,palabras))
    print(filtradas)
    #comprension=filtrar_palabras_comprension(frase,N)
    #normal=filtrar_palabras_normal(frase,N)
    #print("Filtrado de palabras por comprensión: ",comprension)
    #print("Filtrado de palabras normal: ",normal)
    
if __name__=="__main__":
        __main__()