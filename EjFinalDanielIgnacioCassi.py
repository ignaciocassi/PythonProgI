class MesInvalido(Exception):
    pass

def generarInformeMes(directorio,mes):
    """Recibe el directorio del archivo fuente y el número de mes para bsucar las ventas que se hayan generado en el mismo.
    Luego para cada venta que corresponda al mes buscado, agrega su información a la estructura de datos Informe:
    Luego devuelve el informe.
    Elegí una lista de tuplas porque considero que es until poder separar los datos de cada registro, y poder acceder a cada dato mediante un índice."""

    try:
        arch=open(directorio,"rt")
        linea=arch.readline()
        informe=[]
        while linea:
            linea=linea.replace("\n","")
            mesVenta=int(linea[10:12])
            if mesVenta==mes:
                numVendedor=linea[0:2]
                codProducto=int(linea[2:4])
                cantVendida=int(linea[4:8])
                informe.append((numVendedor,codProducto,cantVendida))
            linea=arch.readline()
        return informe,mes
    except IOError:
        print("Error al intentar abrir el archivo. ")
    finally:
        try:
            arch.close()
        except:
            pass
        
def mostrarInforme(informe,mes):
    """Recibe el informe generado anteriormente y el número de mes para obtener el nombre del mes correspondiente.
    Luego para cada elemento en el informe, muestra la información recopilada de forma clara y legible."""

    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

    restar1=lambda x:x-1
    print("Informe de ventas para el mes de "+meses[restar1(mes)]+": ")
    print(" ")
    for i in range(len(informe)):
        #print("N° de vendedor: "+str(informe[i][0])+" Cód. de producto: "+str(informe[i][1])+" Cantidad vendida: "+str(informe[i][2])+".")
        print("N° de vendedor: "+str(informe[i][0])+" Cód. de producto: "+str(informe[i][1])+" Cantidad vendida: "+str(informe[i][2])+".")
    
def solicitarDatos():
    """Solicita por teclado el número del mes para generar el informe, verifica que sea un mes válido y finalmente solicita el directorio del archivo fuente."""
    while True:
        try:
            mes=int(input("Ingrese el mes para generar el informe de ventas: "))
            if mes<0 or mes>12:
                raise MesInvalido
            elif mes==-1:
                break
            break
        except MesInvalido:
            print("El número de mes ingresado no es válido, reintente: ")
        except ValueError:
            print("El número de mes ingresado no es válido, reintente: ")
    while True:
        try:
            directorio=input("Ingrese el directorio del archivo de ventas: ")
            break
        except IOError:
            print("Error al intentar abrir el archivo. (directorio inválido)")
        except TypeError:
            print("No se ha encontrado el archivo especificado, reintente: ")
    return directorio,mes

def __main__():
    directorio,mes=solicitarDatos()
    informe,mes=generarInformeMes(directorio,mes)
    mostrarInforme(informe,mes)

if __name__=="__main__":
    __main__()