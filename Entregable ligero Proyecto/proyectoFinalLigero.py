# Autor: Daniel Rojas
# Proyecto final: Aplicación para realizar una cotización para servicio de producción audiovisual

from PIL import Image

def menu(opciones):      #Despliega las opciones de cada pregunta para que el usuario teclee su respuesta
    respondido = False
    while respondido == False :
        for indice in range(len(opciones)-1): 
            print(indice+1,".",opciones[indice])
        print("\n0 .",opciones[-1])
        respuesta = input("\nTeclea el número de tu respuesta: ")
        if int(respuesta) < 0 or int(respuesta) > (len(opciones)-1):
            print("Error. Debe teclear un número que aparezca entre las opciones\n")
        else:
            respondido = True
    return respuesta


def correrCuestionario():   #Despliega las preguntas que el usuario debe resolver y calcula el costo basándose en las respuestas
    #VARIABLES
    post = 1
    equipoCamara = 1
    equipoIluminacion = 0
    equipoAudio = 0
    satisfecho = 0
    pagoPost = 800
    entrega = 0
    
    #LISTAS
    opciones1 = ["Cobertura de un evento","Video publicitario o institucional","Cancelar (volver al menú)"]
    opciones2 = ["Llamado de un día (12 horas)","Jornada (8 horas)",\
                 "Media jornada (4 horas)","Llamado nocturno (12 horas durante la noche)",\
                 "Cancelar (volver al menú)"]
    opciones3 = ["CDMX","EDOMEX","Cancelar (volver al menú)"]
    opcionesSiNo = ["Sí","No","Cancelar (volver al menú)"]
    urgencia = ["Sí, está perfecta","No, lo necesito con mayor urgencia","Cancelar (volver al menú)"]
    decision = ["Aceptar","Cancelar (volver al menú)"]
    
    #CUESTIONARIO
    print("\nA) ¿Para qué tipo de proyecto requiere el servicio de video?")
    respuesta1 = menu(opciones1)
    if respuesta1 == "1":
        jornada = 1600
        crew = 1
    elif respuesta1 == "2":
        jornada = 1200
        crew = 2
    else:
        return False
    
    print("\nB) ¿Qué tipo de llamado sería?")
    respuesta2 = menu(opciones2)
    if respuesta2 == "1":
        llamado = jornada*1.25
        comidas = 2
    elif respuesta2 == "2":
        llamado = jornada
        comidas = 1
    elif respuesta2 == "3":
        llamado = jornada*0.75
        comidas = 1
    elif respuesta2 == "4":
        llamado = jornada*1.5
        comidas = 2
    else:
        return False
    
    print("\nC)¿En dónde se llevaría a cabo la grabación?",\
"Si su ubicación no se encuentra aquí, contáctenos para una cotización")
    respuesta3 = menu(opciones3)
    if respuesta3 == "1":
        transporte = 500
    elif respuesta3 == "2":
        transporte = 250
    else:
        return False
    
    print("\nD) ¿El video requerirá usar iluminación artificial?")
    respuesta4 = menu(opcionesSiNo)
    if respuesta4 == "1":
        crew += 1
        equipoIluminacion += 1
    elif respuesta4 == "2":
        pass
    else:
        return False
    
    print("\nE) ¿Para el video se necesitarán diálogos grabados en set (sonido directo)?")
    respuesta5 = menu(opcionesSiNo)
    if respuesta5 == "1":
        crew += 1
        equipoAudio += 1
    elif respuesta5 == "2":
        pass
    else:
        return False
    
    print("\nF) ¿Su video requerirá el uso de Motion Graphics?")
    respuesta6 = menu(opcionesSiNo)
    if respuesta6 == "1":
        post += 1
    elif respuesta6 == "2":
        pass
    else:
        return False
    
    while satisfecho < 3:
        costo = ((crew*llamado) + transporte + (crew*comidas*150) + (equipoCamara*100) + (equipoAudio*110) + (equipoIluminacion*50) + (post*pagoPost))*1.30
        print("\nLe proponemos la realización de un video con las siguientes características: ")
        print("-",opciones1[int(respuesta1)-1])
        print("-",opciones2[int(respuesta2)-1])
        print("- Ubicado en",opciones3[int(respuesta3)-1])
        if respuesta4 == "1":
            print("- Iluminación artificial")
        if respuesta5 == "1":
            print("- Sonido directo")
        if respuesta6 == "1":
            print("- Motion Graphics en la postproducción")
        print("- Un crew de ",crew,"personas")
                    
        if satisfecho == 0:
            print("- Un tiempo de entrega de 2 semanas, con posibilidad de 2 revisiones previas")
        elif satisfecho == 1:
            print("- Un tiempo de entrega de 1 semana, con posibilidad de 1 revisión previa")
        elif satisfecho == 2:
            print("- Un tiempo de entrega de 3 días, sin posibilidad de revisión")
                    
        print("\nEsto tendría un costo total de $%.2d MXN (por llamado)" % (costo))
                    
        if satisfecho < 2:
            print("¿Está satisfecho con su cotización?")
            satisfaccion = menu(urgencia)
            if satisfaccion == "1":
                satisfecho = 3
            elif satisfaccion == "2":
                satisfecho += 1
                pagoPost += 400
                entrega += 1
            else:
                return False
        else:
            print("\nYa no se puede modificar más la cotización")
            final = menu(decision)
            if final == "1":
                satisfecho = 3
                break
            else:
                return False
                break
    
    resultado = "Resultados/caso_" + respuesta1 + respuesta2 + respuesta3 + respuesta4 + respuesta5 + respuesta6 + str(entrega) + ".png"
    if resultado == "Resultados/caso_1212112.png" or resultado == "Resultados/caso_2411112.png":
        imagenResultado = Image.open(resultado)
        imagenResultado.show()
    else:
        pass

    return costo    


def main():
    #IMÁGENES
    imagenBienvenida = Image.open("imagenBienvenida.png")
    imagenAcercaDe = Image.open("imagenAcercaDe.png")
    
    acciones = ["Obtener una cotización","Acerca de","Salir de la aplicación"]

    imagenBienvenida.show()
    print("\n¿Qué desea hacer?")
    accion = menu(acciones)
    while accion != "0":
        if accion == "2":
            imagenAcercaDe.show()
        else:
            cuestionario = True
            print("""\nAdvertencia: La cotización que le brinda esta aplicación NO es una cotización final,
sino una estimación para que usted conozca nuestras tarifas.
Para una cotización más detallada, deberá ponerse en contacto y brindarnos
las especificaciones de su proyecto.""")
            while cuestionario == True:
                listo = correrCuestionario()
                if listo == False:
                    cuestionario = False
                    break
                else:
                    print("\n¡Gracias por utilizar la aplicación! Su cotización final fue de $%.2d MXN (por llamado)" % (listo))
                break
        print("\n¿Qué desea hacer?")
        accion = menu(acciones)
    print("FIN. ¡Gracias por visitar PENTA FILMS!")
        
    
main()