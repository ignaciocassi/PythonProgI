"""Ingresar una frase desde el teclado y eliminar las palabras repetidas, dejando un
solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su
longitud. La eliminación de las palabras duplicadas debe realizarse a través de un
conjunto."""

entrada=input("Ingrese una frase: ")
lista=entrada.split(" ")
dic={}
for palabra in lista:
    if palabra not in dic:
        dic[palabra]=1
    else:
        dic[palabra]+=1
        
palabras=list(dic.keys())

palabras.sort(key=len)
print (palabras)
        