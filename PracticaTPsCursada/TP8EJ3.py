def ImprimirNumeros():
    numero=1
    while True:
        try:
            print(numero)
            while numero<=100000:
                numero+=1
                print(numero)
        except KeyboardInterrupt:
            entrada=input("Desea detener la ejecución? S/N: ")
            if entrada=="S":
                break
            elif entrada=="N":
                pass

ImprimirNumeros()        