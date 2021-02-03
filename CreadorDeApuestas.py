from random import randint

def crearApuestas():
    try:
        arch=open(r"C:\Users\Nacho\Desktop\Python\Práctica\ProgI\ProgI\apuestas2.csv","wt")
        docagregados=[]
        contador=0
        while contador<=100000:
            documento=randint(10000000,60000000)
            agencia=randint(1234,1236)
            if documento not in docagregados:
                docagregados.append(documento)
                numapostados=[]
                for i in range(6):
                    apuesta=randint(0,41)
                    if apuesta not in numapostados:
                        numapostados.append(apuesta)
                    else:
                        print("Apuesta repetida."+str(apuesta))
                arch.write(str(documento)+";"+str(agencia)+";"+";".join([str(numero) for numero in numapostados])+"\n")
            else:
                print("Documento repetido: "+str(documento)+".")
            contador+=1
    except IOError:
        print("Error al intentar crear el archivo. ")
    finally:
        try:
            arch.close()
        except:
            pass

def __main__():
    crearApuestas()

if __name__=="__main__":
    __main__()