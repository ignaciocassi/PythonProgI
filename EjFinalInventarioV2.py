#Compra
#DD MM AAAA DDDDDDDDDDDDDDDDDDDD NNN PPP.PP

#Venta
#DD MM AAAA NNN DDDDDDDDDDDDDDDDDDDD PPP.PP

def procesarInventario(directorio):
    try:
        arch=open(directorio,"rt")
        inventario=dict()
        errores=[]
        inventario2009=dict()
        balance2009=0
        linea=arch.readline()
        numlinea=0
        while linea:
            linea=linea.replace("\n","")
            numlinea+=1
            if linea[32:35].isnumeric() and linea[11:14].isalpha():
                #Si es compra:
                producto=linea[11:31]
                cantidad=int(linea[32:35])
                if producto not in inventario:
                    inventario[producto]=cantidad
                else:
                    inventario[producto]=(inventario[producto]+cantidad)
            elif (linea[32:35].isalnum() and linea[11:14].isnumeric()):
                #Si es venta:
                producto=linea[15:35]
                cantidad=int(linea[11:14])
                if producto not in inventario:
                    errores.append("Se intentó registrar una venta de un producto que no está registrado. ")
                    print("Se detectó una venta de un producto que no está registrado, en la línea número: "+str(numlinea)+".")
                elif (producto in inventario and cantidad>inventario[producto]):
                    errores.append((numlinea,linea,"Se intentó registrar una venta de un producto del que no queda stock."))
                    print("Se detectó una venta de un producto que no está disponible, en la línea número: "+str(numlinea)+".")
                else:
                    inventario[producto]=(inventario[producto]-cantidad)
            else:
                errores.append((numlinea,linea,"La línea no respeta el formato del archivo y no ha sido procesada."))
            #Si es año 2009 y es compra:
            if linea[6:10]=="2009" and linea[32:35].isnumeric() and linea[11:14].isalnum():
                cantidad=float(linea[32:35])
                preciounitario=float(linea[36:42])
                balance2009=balance2009-cantidad*preciounitario
            #Si es año 2009 y es venta:
            elif (linea[6:10]=="2009" and linea[11:14].isnumeric() and linea[32:35].isalnum()):
                cantidad=float(linea[11:14])
                preciounitario=float(linea[36:42])
                balance2009=balance2009+cantidad*preciounitario
            linea=arch.readline()
        return inventario,errores,round(balance2009,ndigits=2)
    except IOError:
        print("Error al intentar abrir el archivo.")
    finally:
        arch.close()

def mostrarInventarioDescendente(inventario):
    #El listado debe mostrarse ordenado en forma descendente según la cantidad en stock.
    inventarioDescendente=list(inventario.items())
    inventarioDescendente.sort(key=lambda item:item[1],reverse=True)

    print("")
    print("Inventario actual: ")
    print("")
    print("| Producto             | Cant |")
    for producto in inventarioDescendente:
        print("| "+producto[0]+" | "+str(producto[1])+"   |")

def mostrarErrores(errores):
    if len(errores)==0:
        print("")
        print("No se han producido errores. ")
        print("")
    else:
        print("")
        print("Las siguientes líneas causaron un error de venta de producto inexistente: ")
        print(" ")
        print("| N° | Producto              | Cantidad | Causa del error                                                       |")
        for error in errores:
            print("| "+str(error[0])+" | "+error[1][15:35]+"  | "+error[1][11:14]+"      | "+error[2]+" |")
        print("")

def mostrarBalance2009(balance2009):
    print("")
    print("El balance para el año 2009 fue de: $"+str(balance2009)+".")

def __main__():
    directorio=r"C:/Users/Nacho/Desktop/Python/Práctica/ProgI/ProgI/inventario.txt"
    inventario,errores,balance2009=procesarInventario(directorio)
    mostrarInventarioDescendente(inventario)
    mostrarBalance2009(balance2009)
    mostrarErrores(errores)

if __name__=="__main__":
    __main__()