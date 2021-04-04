class MesInvalido(Exception):
    pass

class VendedorInvalido(Exception):
    pass

class CodigoProductoInvalido(Exception):
    pass

def generarInformeMes(directorio,mes):
    try:
        arch=open(directorio,"rt")
        linea=arch.readline()
        diccVentasTotales=dict()
        while linea:
            if int(linea[10:12])==mes:
                linea=linea.replace("\n","")
                numVendedor=linea[0:2]
                if (int(numVendedor)<0 or int(numVendedor)>15):
                    raise VendedorInvalido
                codProd=linea[2:4]
                if (int(codProd)<1 or int(codProd)>99):
                    raise CodigoProductoInvalido
                unidVendidas=int(linea[4:8])
                diaVenta=int(linea[8:10])
                mesVenta=int(linea[10:12])
                añoVenta=int(linea[12:16])
                if str(numVendedor)+str(codProd) not in diccVentasTotales.keys():
                    diccVentasTotales[numVendedor+codProd]=unidVendidas
                else:
                    diccVentasTotales[numVendedor+codProd]+=unidVendidas
            linea=arch.readline()
        return diccVentasTotales,mes
    except IOError:
        print("Error al intentar abrir el archivo.")
    except VendedorInvalido:
        print("El vendedor debe estar entre 0 y 15.")
    except CodigoProductoInvalido:
        print("El código del producto debe estar entre 0 y 99.")
    finally:
        try:
            arch.close()
        except:
            pass
        
def mostrarVentasTotales(diccVentasTotales,mes):
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    restar1=lambda x:x-1
    print("Informe de ventas para el mes de "+meses[restar1(mes)]+": ")
    print(" ")
    for clave in diccVentasTotales.keys():
        print("El número de vendedor "+clave[0:2]+" vendió "+str(diccVentasTotales.get(clave))+" unidades del artículo "+clave[2:4]+" en el mes de "+meses[restar1(mes)]+".")

def solicitarDatos():
    """Solicita por teclado el número del mes para generar el informe, verifica que sea un mes válido y finalmente solicita el directorio del archivo fuente."""
    while True:
        try:
            mes=int(input("Ingrese el mes para generar el informe de ventas: "))
            if mes<0 or mes>12:
                raise MesInvalido
            break
        except MesInvalido:
            print("El número de mes ingresado no es válido, reintente: ")
        except ValueError:
            print("El número de mes ingresado no es válido, reintente: ")
    directorio=input("Ingrese el directorio del archivo de ventas: ")
    return directorio,mes

def __main__():
    directorio,mes=solicitarDatos()
    diccVentasTotales,mes=generarInformeMes(directorio,mes)
    mostrarVentasTotales(diccVentasTotales,mes)

if __name__=="__main__":
    __main__()