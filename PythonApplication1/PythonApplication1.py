import aspose.words as aw
import os

def conviertePDFaTXT(archivo, nombreAr):#convertir el archivo dpf a txt 
        doc = aw.Document(archivo)
        print("Generando el .txt")
        doc.save("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".txt")
        print("Documento Generado")

def borrar(nombreAr):
    archivoTxt= os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".txt")
    l1 = []
    with open(archivoTxt, 'r') as fp:
        l1 = fp.readlines()
    with open(archivoTxt, 'w') as fp:
        for number, line in enumerate(l1):
           if number in [4,5,6,45,46,47,48,49,50,51,52,53,54,67,69]:
               if number == 4: #RFC
                    print(number, line)
                    print(len(line))
                    if (len(line) == 12):#corroborar longitud del RFC
                         fp.write(line)
                         print(line)
                    elif(len(line)== 13):
                         fp.write(line)
                         print(line)
                    elif(len(line)>=14):
                        rfc=line.split(' ')
                        fp.write(rfc[0]+"\n")
                        print(line)
               if number == 5: #razon social
                    print(number, line)
                    print(len(line))
                    if (len(line)!=35):
                        fp.write(line)
                        print(line)
               if number ==  6:
                   print(number, line)
                   print(len(line))
                   if(len(line)!=38):#razon social con cadena encimado de 'Nombre'
                        raSo=line.split(' ')
                        raSoArr=[]
                        for i in raSo:
                            if (i != 'Nombre,'):
                                raSoArr.append(i)
                            elif (i=='Nombre,'):
                                break
                        fp.write(" ".join(raSoArr)+"\n")
                        print(" ".join(raSoArr)+"\n")
               if number == 45: #codigo postal
                     print(number, line)
                     print(len(line))
                     if (len(line)!=1):
                         if (len(line) == 21):#division del codigo postal 
                             cp=line.split(':')
                             fp.write(cp[1])
                             print(line)
                         else:
                             fp.write(line)
                             print(line)
               if number == 46: #codigo postal y nombre de vialidad 
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                      if (len(line) == 21): #division del codigo postal 
                             cp=line.split(':')
                             fp.write(cp[1])
                             print(cp[1])
                      elif(len(line) >=22): #numero interior
                              numInt=line.partition('NÃºmero Interior:') 
                              numIntl=list(cp)
                              print(numIntl)
                              fp.write(numIntl[0]+"\n") #guarda nombre de vialidad 
                              fp.write(numIntl[1]+" "+numIntl[2])#guarda numero interior
                              print(numIntl[0])
                              print(numIntl[1]+" "+numIntl[2])

               if number == 47:#codigo postal y nombre de vialidad
                    print(number, line)
                    print(len(line))
                    if (len(line)!=1):
                      if (len(line)!=1):
                        if(len(line) >=22): #numero interior
                              numInt=line.partition('NÃºmero Interior:')
                              if ('NÃºmero Interior:' in numInt):
                                  print("true")
                                  numIntl=list(numInt)
                                  print(numIntl)
                                  fp.write(numIntl[0]+"\n") #guarda nombre de vialidad 
                                  fp.write(numIntl[1]+" "+x1[2])#guarda numero interior
                                  print(numIntl[0])
                                  print(numIntl[1]+" "+numIntl[2])

               if number == 48:#nombre de vialidad, quitar linea nombre entidad federativa 
                    print(number,line)
                    print(len(line))
                    if (len(line)!=1):
                        if(len(line) >=22): #numero interior
                              numInt=line.partition('NÃºmero Interior:')
                              if ('NÃºmero Interior:' in numInt):
                                  print("true")
                                  numIntl=list(numInt)
                                  print(numIntl)
                                  fp.write(numIntl[0]+"\n") #guarda nombre de vialidad 
                                  fp.write(numIntl[1]+" "+numIntl[2])#guarda numero interior
                                  print(numIntl[0])
                                  print(numIntl[1]+" "+numIntl[2])
                              else:
                                  nomLoc=line.partition('Nombre de la Localidad:')
                                  if('Nombre de la Localidad:' in nomLoc):
                                        print("nombre de la localidad no se guarda")
               if number == 49:# quitar linea nombre entidad federativa 
                    print(number,line)
                    nomLoc=line.partition('Nombre de la Localidad:')
                    if('Nombre de la Localidad:' in nomLoc):#nombre de la localidad no se guarda en el txt
                        print("nombre de la localidad no se guarda")
                    else: 
                        nomEnt=line.partition('Nombre de la Entidad Federativa:')
                        if('Nombre de la Entidad Federativa:' in nomEnt):#nombre de la entidad no se guarda en el txt
                             print("no se imprime nombre de la entidad federativa")
                        else:
                            telfijo=line.partition('Tel. Fijo Lada:')#tel fijo no se guarda
                            if('Tel. Fijo Lada:' in telfijo):
                                print("no se imprime el telefono fijo")
                            else:
                                fp.write(line)
                                print(line)
               if number == 50:#quitar linea nombre entidad federativa 
                    print(number,line)
                    nomEnt=line.partition('Nombre de la Entidad Federativa:')
                    if('Nombre de la Localidad:' in nomEnt):#nombre de la localidad no se guarda en el txt
                         print("nombre de la entidad no se guarda")
                    else: 
                        entid=line.partition('Nombre de la Entidad Federativa:')
                        if('Nombre de la Entidad Federativa:' in entid):#nombre de la entidad no se guarda en el txt
                             print("no se imprime nombre de la entidad federativa")
                        else:
                            telfijo=line.partition('Tel. Fijo Lada:')#tel fijo no se guarda
                            if('Tel. Fijo Lada:' in telfijo):
                                print("no se imprime el telefono fijo")
                            else:
                                fp.write(line)
                                print(line)
               if number == 52:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 53:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 54:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 67:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               if number == 69:
                    print(number,line)
                    if (1==1):
                        fp.write(line)
               #fp.write(line)
    os.system("Pause")


def inicio():#funcion en donde se introduce la ruta del archivo y el nombre del archivo 
        nombreAr = input("introduzca el nombre del archivo que se encuentra en la direccion: C:/Users/mmartinez/Documents/CSF/")
        archivo =  os.path.join("C:/Users/mmartinez/Documents/CSF/" + nombreAr +".pdf")
        conviertePDFaTXT(archivo,nombreAr)
        borrar(nombreAr)

inicio()#inici del programa