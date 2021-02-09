def intercalarListas(listaA,listaB): #invalida
    indice=1
    while(len(listaB)>0):
        numero=listaB.pop()
        listaA.insert(indice,numero)
        indice+=2

def intercalarListas2(listaA,listaB): #con rebanadas
    indice=0
    while(len(listaB)>0):
        if indice%2!=0:
            listaA[indice:indice]=listaB[:1]
            listaB.pop(0)
        indice+=1

def intercalarListas3(listaA,listaB): #con rebanadas
    contador=1
    inicio=0
    fin=len(listaA)+len(listaB)+1
    while(contador<fin):
        listaA[contador:contador]=listaB[inicio:inicio+1]
        contador+=2
        inicio+=1

def __main__():
    listaA=[1,2,3]
    listaB=[7,8,9]
    listaC=intercalarListas4(listaA,listaB)
    print(listaC)

if __name__=="__main__":
    __main__()