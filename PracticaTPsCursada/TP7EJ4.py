"""Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas."""

def sumarecursiva(A,B,suma=0,veces=0):
    if veces==B:
        return suma
    else:
        suma=suma+A
        veces+=1
        return sumarecursiva(A,B,suma,veces)
    
print(sumarecursiva(5,3))