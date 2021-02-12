class ErrorDigits(Exception):
    pass

def crearlista():
    lista=[]
    continuar=True
    while continuar==True:
        try:
            entrada=input("Ingrese un número: ")
            while entrada!="-1":
                if entrada not in lista and len(entrada)%2==0:
                    lista.append(entrada)
                    entrada=input("Ingrese un número: ")
                elif entrada in lista:
                    raise ValueError
                elif len(entrada)%2!=0:
                    raise ErrorDigits("Error")
            continuar=False
            print(lista)
        except ValueError:
            pass
        except ErrorDigits:
            pass
        except IOError:
            pass
    

crearlista()