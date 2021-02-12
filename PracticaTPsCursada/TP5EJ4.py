"""Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar un programa para imprimir los números
enteros entre 1 y 100000, y que solicite confirmación al usuario antes de detenerse cuando se presione Ctrl-C"""
continuar=True
while continuar==True:
    try:
        N=1
        while N<=100000:
            print (N)
            N=N+1
    except KeyboardInterrupt:
        prompt=input("¿Desea detener la ejecución? S/N")
        if prompt=="S":
            continuar=False
        elif prompt=="N":
            continue