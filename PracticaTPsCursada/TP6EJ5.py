def LeerArchivo1():
    try:
        archivo1=open("C:\\Users\\Nacho\\Desktop\\archivo1.txt","rt")
        archivo1traducido=open("C:\\Users\\Nacho\\Desktop\\archivo1traducido.txt","wt")
        linea=archivo1.readline()
        linea=linea.replace(" ","")
        linea=linea.replace("\n","")
        contador=0
        limite=contador+10
        lista=[]
        while linea:
            for caracter in linea:
                contador+=1
                if contador==limite:
                    cadena=linea[limite-10:limite]
                    lista.append(cadena)
                    limite+=10
            archivo1traducido.write(",".join(lista))
            linea=archivo1.readline()
        
    except IOError:
        print("Error al intentar abrir el archivo.")
    finally:
        archivo1.close()
        archivo1traducido.close()

LeerArchivo1()
                
            