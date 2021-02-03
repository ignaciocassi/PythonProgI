from random import randint

def sortear():
    sorteados=[]
    while len(sorteados)<6:
        azar=randint(0,41)
        if azar not in sorteados:
            sorteados.append(azar)
    return sorteados

def procesarApuestas(directorio,sorteados):
    try:
        arch=open(directorio,"rt")
        linea=arch.readline()
        ganadores=[]
        while linea:
            numeros=[]
            linea=linea.replace("\n","")
            coincidencias=0
            campos=linea.split(";")
            for cadnum in campos[2:8]:
                numeros.append(int(cadnum))
            for numero in numeros:
                if numero in sorteados:
                    coincidencias+=1
            if coincidencias>0:
                documento=campos[0]
                agencia=campos[1]
                ganadores.append([documento,agencia,numeros,coincidencias])
            linea=arch.readline()
        if len(ganadores)>0:
            print("Los números ganadores fueron: ")
            print(*sorteados,sep=", ")
            print("")
            print("Los ganadores fueron: ")
            # Ordenados por documento ascendente ganadores.sort(key=lambda ganador:ganador[0])
            ganadores.sort(key=lambda ganador:ganador[3],reverse=True)
            for ganador in ganadores:
                print("DNI: "+ganador[0]+" N° agencia: "+ganador[1]+" ¡Con "+str(ganador[3])+" aciertos! ")
        else:
            print("No han habido ganadores.")
    except IOError:
        print("Error al intentar abrir el archivo.")
    finally:
        try:
            arch.close()
        except:
            pass

def __main__():
    sorteados=sortear()
    directorio=r"C:\Users\Nacho\Desktop\Python\Práctica\ProgI\ProgI\apuestas2.csv"
    procesarApuestas(directorio,sorteados)

if __name__=="__main__":
    __main__()