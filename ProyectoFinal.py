#Autor: Elena R.Tovar
#Proyecto Final
#Pide datos al usuario para ayudar a calcular precios de comisiones


def menuInicio():        #menú Principal
    x=int(input("""Elija la opción que desea:
                Teclee 1 para calcular el costo de sus comisiones
                Teclee 2 para ver la información del programa
                Teclee 3 para salir
                """))
    return x

def detallesComision():                                     #Recopila etapas de trabajo necesarias para una comisión
    etapasDesarrollo=[]
    etapa=input("Ingrese las etapas de desarrollo de su trabajo, como boceto, lineart, color, etc. Una vez finalizado, teclee FIN  ")
    etapa=etapa.upper()
    etapasDesarrollo.append(etapa)
    while etapa!="FIN":
        etapa=input(""" Después de cada etapa, presione enter.
                    Una vez finalizado, teclee FIN             """)
        etapa=etapa.upper()
        if etapa=="FIN":
            break
        else:
            etapasDesarrollo.append(etapa)
    return etapasDesarrollo


        
def detallesTrabajo(dComm):                                #Recopila el tiempo de trabajo por etapa
    indice=0
    time=[]
    j=len(dComm)
    z=dComm[indice]
    
    print("Cuantas horas se tarda en realizar la siguiente etapa?")
    ti=float(input(z))
    time.append(ti)
    indice=indice+1
    while j>indice:
        z=dComm[indice]
        ti=float(input(z))
        time.append(ti)
        indice= indice+1
    return time

def horsTrabajo(dias,vac,horast):          #Calcula las horas de trabajo al año del artista
    sem=52
    
    semef=(sem-vac)
    dief=dias*semef
    horsef=dief*horast
    return horsef

def gastoAnual(com, trans, rent, serv, soft, otro):         #Calcula el costo de vida al año del artista
    gasto=(com+trans+rent+serv+soft+otro)*12
    return gasto

def gastosExtra(exp,fact):             #Crea un modificador de precio para calcular el costo final de trabajo por hora
    factura=fact.upper()
    modfact=1
    modexp=exp*0.3
    if factura=="SI":
        modfact=modfact+0.3
    else:
        modfact=modfact
    modfact=modfact+modexp
    return modfact

def gastosHardware(añosd,costd,hT):    #Calcula el costo de hardware por hora de trabajo
    costoAño=costd/añosd
    costoHora=costoAño/hT
    return costoHora
       
def calcCosto():               #Calcula el costo de cada hora laboral
    #Cuestionario para el usuario
    dias=float(input("¿Cuántos días a la semana trabaja?  "))
    vac= float(input("¿Cuántas semanas de vacaciones toma al año?  "))
    horast=float(input("¿Cuántas horas trabaja comúnmente en un día laboral?  "))
    print("¿A cuánto ascienden sus gastos mensuales de...?  ")
    com=float(input("Comida  "))
    trans=float(input("Transporte  "))
    rent= float(input("Renta  "))
    serv= float(input("Servicios  "))
    soft= float(input("Licencias de software  "))
    otro= float(input("Otros "))
    exp= float(input("¿Con cuántos años de experiencia laboral cuenta?  "))
    fact=input("¿Emite factura?  SI/NO ")
    añosd=float(input("¿Cada cuántos años reemplaza su equipo de trabajo?  "))
    costd=float(int(input("¿Cuál es el costo de su equipo?  ")))
    
    hT=horsTrabajo(dias,vac,horast)                        #Calcula las horas de trabajo al año
    gA=gastoAnual(com, trans, rent, serv, soft,otro)      #Calcula un estimado del costo de vida anual del artista
    gE=gastosExtra(exp,fact)                              #Crea un modificador para añadir consideraciones extra de acuerdo con la experiencia y servicio que ofrece en artista
    cE=gastosHardware(añosd,costd,hT)                     #Calcula el costo de hardware por hora laboral
    
    vidaHora=(gA/hT)+cE                                  
    
    costoHora=vidaHora*gE
    
    return costoHora
    

def costoPorDetalle(dWork, costoHora):        #Recopila en una lista el costo de cada una de las etapas del trabajo de comisión
    costoDetalle=[]
    indice=0
    j=len(dWork)
    while indice<j:
        z=costoHora*dWork[indice]
        costoDetalle.append(z)
        indice=indice+1
    return costoDetalle
    
    

def calculaCosto():
    print("Bienvenido a la calculadora de costo de comisiones")
    print("Por favor responda las preguntas con sinceridad")
    print("")
    dComm= detallesComision()                 #Recopila en una lista las etapas de trabajo de la comisión
    dWork= detallesTrabajo(dComm)             #Recopila en una lista el tiempo que tarda cada una de las etapas de trabajo
    costoHora= calcCosto()                    #Calcula el costo por hora del trabajo del artista
    
    costDet=costoPorDetalle(dWork, costoHora)         #Recopila en una lista el costo de cada una de las etapas del trabajo de comisión
    
    
    j=len(dComm)
    indice=0
    total=0
    
    print(".............................................")
    print("El costo de cada una de sus horas de trabajo es de $%0.2fMXN" %(costoHora))
    print("A continuación podrá ver el costo de cada una de las etapas de sus comisiones")
    print(".............................................")
    while indice<j:
        print(dComm[indice],"............  $%0.2f MXN" %(costDet[indice]))
        total=total+costDet[indice]
        indice=indice+1
    print("TOTAL .............$%0.2f MXN"%(total))
    

def main():
    opcion = menuInicio()
    while opcion !=3:
        if opcion==1:
            calculaCosto()
        elif opcion==2:
            print("""Este proyecto fue desarrollado como parte de la materia de Fundamentos de Programación
                    Alumno: Elena R.Tovar
                    Matrícula: A01376318
                    Profesor: Roberto Martínez Román
                    Semestre: Febrero-Junio 2020""")
        else:
            print("COMANDO NO VÁLIDO")
        opcion =menuInicio()
    print("END")
        
    
main()