#Roberto Sobrado
#Calcular el costo por puesto del crew y arma una inversion dependiendo de las necesidades del proyecto.

from PIL import ImageDraw, Image #Libreria PIL para importar imagenes.


def cargarImagen(archivo): #función para cargar imagenes
    imagen = Image.open(archivo)
    return imagen

def menuPrincipal(): #Esta función despliega el menu principal.
    
    #menú principal
    print('''
        1. Inicio
        2. Nosotros
        0. SALIR
        ''')
    
    decidir = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while decidir != 0:
        if decidir == 1:
            return (decidir)
        elif decidir == 2:
            return (decidir)
        elif decidir == 4:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        decidir = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
        
def menuDireccion(): #Menú para el departamento de dirección.
    
    print('''
        0. Director
        1. Asistente de Dirección
        2. Script
        3. Second
        4. *Atrás*''')
    
    direccion = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while direccion != 4:
        if direccion == 0:
            return (direccion)
        elif direccion == 1:
            return (direccion)
        elif direccion == 2:
            return (direccion)
        elif direccion == 3:
            return (direccion)
        elif direccion == 4:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        direccion = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
        
    
    
def precioDireccion(dire,diasRodajeD): #calcular costos del departamento de dirección.
    precio = [60000, 30000, 20000, 10000]
    
    costoDia = precio[dire]
    
    costoTotal = costoDia * diasRodajeD
    
    print ("\nEl costo por dia es de $%d" % (costoDia))
    
    return (costoTotal)
    
def menuFoto(): #Menú para el departamento de fotografia
    
    print('''
        0. Director de Fotografía
        1. Asistente de Fotografia
        2. Segundo Asistente
        3. Gaffer
        4. Grip
        5. DIT
        6. *Atrás*''')
    
    
    

    fotografia = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while fotografia != 6:
        if fotografia == 0:
            return (fotografia)
        elif fotografia == 1:
            return (fotografia)
        elif fotografia == 2:
            return (fotografia)
        elif fotografia == 3:
            return (fotografia)
        elif fotografia == 4:
            return (fotografia)
        elif fotografia == 5:
            return (fotografia)
        elif fotografia == 6:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        fotografia = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.

def precioFoto(foto,diasRodajeF): #calcular costos del departamento de fotografía
    precio = [55000, 25000, 15000, 20000, 10000, 5000]
    
    costoDia = precio[foto]
    
    costoTotal = costoDia * diasRodajeF
    
    print ("\nEl costo por dia es de $%d" % (costoDia))
    
    return (costoTotal)

def menuDiseno(): #Menú para el departamento de arte.
    
    print('''
        0. Director de Produccion
        1. Director de Arte
        2. Asistente de Arte
        3. Vestuario
        4. Escenografo
        5. Maquillaje
        6. *Atrás*''')
    
    
    
    
    disenoProd = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while disenoProd != 6:
        if disenoProd == 0:
            return (disenoProd)
        elif disenoProd == 1:
            return (disenoProd)
        elif disenoProd == 2:
            return (disenoProd)
        elif disenoProd == 3:
            return (disenoProd)
        elif disenoProd == 4:
            return (disenoProd)
        elif disenoProd == 5:
            return (disenoProd)
        elif disenoProd == 6:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        disenoProd = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
        
def precioDiseno(diseno,diasRodajeDi): #calcular costos del departamento de arte.
    
    precio = [55000, 40000, 10000, 15000, 20000, 10000]
    
    costoDia = precio[diseno]
    
    costoTotal = costoDia * diasRodajeDi
    
    print ("\nEl costo por dia es de $%d" % (costoDia))
    
    return (costoTotal)

def menuSonido(): #Menú para el departamento de sonido directo.
    
    print('''
        0. Jefe de sonido directo.
        1. Microfonista
        2. Boom
        3. Mixer
        4. *Atrás*''')
    
    
    sonidoDireto = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while sonidoDireto != 4:
        if sonidoDireto == 0:
            return (sonidoDireto)
        elif sonidoDireto == 1:
            return (sonidoDireto)
        elif sonidoDireto == 2:
            return (sonidoDireto)
        elif sonidoDireto == 3:
            return (sonidoDireto)
        elif sonidoDireto == 4:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        sonidoDireto = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.

def precioSonido(sonido,diasRodajeS): #calcular costos del departamento de sonido directo.
    
    precio = [40000, 20000, 10000, 30000]
    
    costoDia = precio[sonido]
    
    costoTotal = costoDia * diasRodajeS
    
    print ("\nEl costo por dia es de $%d" % (costoDia))
    
    return (costoTotal)

def menuEditor(): #Menú para el departamento de postproduccion imagen.
    
    print('''
        0. Chief Editor
        1. Montajista
        2. Editor
        3. Corrección de color
        4. *Atrás*''')
    
    
    sonidoEditor = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while sonidoEditor != 4:
        if sonidoEditor == 0:
            return (sonidoEditor)
        elif sonidoEditor == 1:
            return (sonidoEditor)
        elif sonidoEditor == 2:
            return (sonidoEditor)
        elif sonidoEditor == 3:
            return (sonidoEditor)
        elif sonidoEditor == 4:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        sonidoEditor = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
        
def precioEdicion(editor,minutoMaterial):  #calcular costos del departamento de postproducción imagen.
    
    precio = [6000, 1000, 4000, 2000]
    
    costoMinuto = precio[editor]
    
    costoTotal = costoMinuto * minutoMaterial
    
    print ("\nEl costo por minuto de material es de $%d" % (costoMinuto))
    
    return (costoTotal)
    
def menuEfectos(): #Menú para el departamento de efectos visuales y animación
    
    print('''
        0. Supervisor efectos especiales
        1. VFX
        2. Motion Grafics
        3. Animación 2D
        4. Animación 3D
        5. Rotoscopía
        6. *Atrás*''')
    
    
    
    
    efectosEspeciales = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while efectosEspeciales != 6:
        if efectosEspeciales == 0:
            return (efectosEspeciales)
        elif efectosEspeciales == 1:
            return (efectosEspeciales)
        elif efectosEspeciales == 2:
            return (efectosEspeciales)
        elif efectosEspeciales == 3:
            return (efectosEspeciales)
        elif efectosEspeciales == 4:
            return (efectosEspeciales)
        elif efectosEspeciales == 5:
            return (efectosEspeciales)
        elif efectosEspeciales == 6:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        efectosEspeciales = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
        
def precioEfectos(efectos,minutoMaterial): #calcular costos del departamento de efectos visuales y animación.
    
    precio = [5000, 3000, 1000, 2000, 3000, 2000]
    
    costoMinuto = precio[efectos]
    
    costoTotal = costoMinuto * minutoMaterial
    
    print ("\nEl costo por minuto de material es de $%d" % (costoMinuto))
    
    return (costoTotal)
    
def menuAudio(): #Menú para el departamento de postproduccion en audio
    
    print('''
        0. Supervisor de Audio
        1. Foleys
        2. Diseño sonoro
        3. Musicalización
        4. *Atrás*''')
    
    
    
    
    postAudio = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.
    
    #filtrar la respuesta para solo admitir nuemeros correctos.
    while postAudio != 4:
        if postAudio == 0:
            return (postAudio)
        elif postAudio == 1:
            return (postAudio)
        elif postAudio == 2:
            return (postAudio)
        elif postAudio == 3:
            return (postAudio)
        elif postAudio == 4:
            return (false)
        else:
            print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
            
        
        postAudio = int(input("\n¿Cúal te interesa?: ")) #preguntar al usuario que qiere hacer.

def precioAudio(audio,minutoMaterial): #calcular costos del departamento de postproducción audio.
    
    precio = [5000, 2000, 4000, 5000]
    
    costoMinuto = precio[audio]
    
    costoTotal = costoMinuto * minutoMaterial
    
    print ("\nEl costo por minuto de material es de $%d" % (costoMinuto))
    
    return (costoTotal)
    
    
def menuArea(): #Menú con todos los departamentos 
    print('''
        1. Producción
        2. Dirección
        3. Fotografía
        4. Diseño de Producción
        5. Sonido directo
        6. Edicion
        7. Efectos
        8. Postproducción Audio
        9. Calcular inversión
        
        0. *Atrás*''')
    
    servicio= int(input("\n¿Que desea cotizar?: ")) #preguntar al usuario que qiere hacer.
    
    return (servicio)






def main():
    print ("\nEn NeneFilms sabemos que hay historias que trascienden,\nnos dedicamos a proveer equipo tecnico especializado en\ndistintas areas del arte cinematografico, asi seuramos que\ntendras a un equipo de profesionales.\nCon el fin de contar tu historia.")

    imagen = cargarImagen("herodoto.jpg")
    imagen.show()
    
    decidir = menuPrincipal()
    
    while decidir != 0:
        
        if decidir == 1:
            
            print ("\n¿En que área de la producción te interesa que\ntrabajemos en tu pryecto?") #preguntar al usuario que qiere hacer.
            
            opcion = menuArea()
            costoAcumulado = []
            
            while opcion != 0:
                
                if opcion == 1:
                    
                    print ("\n¡Claro te podemos financiar tu proyecto!.\nAgenda una cita al 56 8532 6654\ny cuentanos tu historia.")
                
                elif opcion == 2:
                    
                    dire = menuDireccion()
                        
                    if dire:
                        diasRodajeD = int(input("\n¿Cuántos dias de rodaje necesitas el servicio?")) #preguntar al usuario que qiere hacer.
                        costoDireccion = precioDireccion(dire,diasRodajeD)
                        
                        costoAcumulado.append(costoDireccion) #agregar costo a lista.
                        
                        print ("\nEl total por %d dias de rodaje es de: $%d" % (diasRodajeD,costoDireccion))
                
                elif opcion == 3:
                    
                    foto = menuFoto()
                    
                    if foto:
                        diasRodajeF = int(input("\n¿Cuántos dias de rodaje necesitas el servicio?")) #preguntar al usuario que qiere hacer.
                        costoFotografia = precioFoto(foto,diasRodajeF)
                        
                        costoAcumulado.append(costoFotografia) #agregar costo a lista.
                        
                        print ("\nEl total por %d dias de rodaje es de: $%d" % (diasRodajeF,costoFotografia))
                    
                elif opcion == 4:
                    
                    diseno = menuDiseno()
                    
                    if diseno:
                        diasRodajeDi = int(input("\n¿Cuántos dias de rodaje necesitas el servicio?")) #preguntar al usuario que qiere hacer.
                        costoDiseno = precioDiseno(diseno,diasRodajeDi)
                        
                        costoAcumulado.append(costoDiseno) #agregar costo a lista.
                        
                        print ("\nEl total por %d dias de rodaje es de: $%d" % (diasRodajeDi,costoDiseno))
                   
                elif opcion == 5:
                    
                    sonido = menuSonido()
                    
                    if sonido:
                        diasRodajeS = int(input("\n¿Cuántos dias de rodaje necesitas el servicio?")) #preguntar al usuario que qiere hacer.
                        costoSonido = precioSonido(sonido,diasRodajeS)
                        
                        costoAcumulado.append(costoSonido) #agregar costo a lista.
                        
                        print ("\nEl total por %d dias de rodaje es de: $%d" % (diasRodajeS,costoSonido))
                    
                elif opcion == 6:
                    
                    editor = menuEditor()
                    
                    if editor:
                        minutoMaterial = int(input("\n¿Cuántos minutos de producto se trabajan?")) #preguntar al usuario que qiere hacer.
                        costoEdicion = precioEdicion(editor,minutoMaterial)
                        
                        costoAcumulado.append(costoEdicion) #agregar costo a lista.
                        
                        print ("\nEl total por %d minutos de material es de: $%d" % (minutoMaterial,costoEdicion))

                elif opcion == 7:
                    
                    efectos = menuEfectos()
                    
                    if efectos:
                        minutoMaterial = int(input("\n¿Cuántos minutos de producto se trabajan?")) #preguntar al usuario que qiere hacer.
                        costoEfectos = precioEfectos(efectos,minutoMaterial)
                        
                        costoAcumulado.append(costoEfectos) #agregar costo a lista.
                        
                        print ("\nEl total por %d minutos de material es de: $%d" % (minutoMaterial,costoEfectos))
                
                elif opcion == 8:
                    
                    audio = menuAudio()
                    
                    if audio:
                        minutoMaterial = int(input("\n¿Cuántos minutos de producto se trabajan?")) #preguntar al usuario que qiere hacer.
                        costoAudio = precioAudio(audio,minutoMaterial)
                        
                        costoAcumulado.append(costoAudio) #agregar costo a lista.
                        
                        print ("\nEl total por %d minutos de material es de: $%d" % (minutoMaterial,costoAudio))
                
                elif opcion ==9:
                    
                    costoTotal = sum(costoAcumulado) #cumar todos los datos de la lista acumulada de costos.
                    print("\nLa inversión para tu proyecto sería de $%d." % (costoTotal))
                
                
                elif opcion <= -1:
                    print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
                
                elif opcion >9:
                    print("\n**ERROR404: teclea una opción válida.**") #Marcar erro por intoduccion de opcion incorrecta, repite respuesta el usuario.
                    
                    
            
                opcion = menuArea()
        
        elif decidir == 2:
            print("\nNeneFilms es una casa productora especializada\nen llevar tu historia a la realidad.\nCon mas de 20 años de experiencia y \nalrededor de 35 peliculas,\nsabemos que somo tu mejor opción.\ninfo@nenefilms.mx\n@nenefilms\ntel. 56 8532 6654.")
            break
        
        decidir = menuPrincipal()
           
    print("Gracias por confiar")

    imagen = cargarImagen("crearteestudiopuma1.jpg")
    imagen.show()

main()