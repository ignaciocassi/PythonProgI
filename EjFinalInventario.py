def obtenerInventario(directorio):
    try:
        archivo=open(directorio,"rt")
        inventario=dict()
        totalcompra2009=float()
        totalventa2009=float()
        linea=archivo.readline()
        while linea:
            linea=linea.replace("\n","")
            #Si es compra:
            if (linea[32:35].isnumeric() and linea[11:14].isalpha() and linea[31:32]==" "):
                producto=linea[11:31]
                cantidad=linea[32:36]
                precio=linea[36:]
                if (linea[6:10]=="2009"):
                    totalcompra2009=totalcompra2009+(float(cantidad)*float(precio))
                if producto not in inventario:
                    inventario[producto]=int (cantidad)
                else:
                    inventario[producto]+=int(cantidad)
            #Si es venta:
            else:
                producto=linea[15:35]
                cantidad=linea[11:15]
                precio=linea[36:]
                if (linea[6:10]=="2009"):
                    totalventa2009=totalventa2009+(float(cantidad)*float(precio))
                if producto not in inventario:
                    print("Venta de producto que no existe en el inventario.")
                else:
                    inventario[producto]-=int(cantidad)
            linea=archivo.readline()
        return totalcompra2009,totalventa2009,list(inventario.items())
    except IOError:
        print("Error al intentar abrir el archivo.")
    finally:
        archivo.close()

def ordenarInventario(inventario):
    for i in range(len(inventario)):
        for j in range(i+1,len(inventario)):
            if (inventario[j][1]>inventario[i][1]):
                aux=inventario[i]
                inventario[i]=inventario[j]
                inventario[j]=aux

def mostrarInventario(inventario):
    for i in range(len(inventario)):
        print("Producto: "+inventario[i][0]+" Cantidad: "+str(inventario[i][1])+".")

def mostrarTotal2009(totalcompra2009,totalventa2009):
    print("En el año 2009, el balance fue de: "+str(round(totalventa2009-totalcompra2009,2))+".")

def __main__():
    directorio=r"C:/Users/Nacho/Desktop/Python/finales/inventario.txt"
    totalcompra2009,totalventa2009,inventario=obtenerInventario(directorio)
    ordenarInventario(inventario)
    mostrarInventario(inventario)
    mostrarTotal2009(totalcompra2009,totalventa2009)

if __name__=="__main__":
    __main__()