# Autor: Paloma Argelia Cueto González
# Programa que ayuda a saber que concentración escoger en la carrera de LAD

from PIL import Image

# Función para definir el menú
def menuPrincipal():
    
    print ("Qué deseas hacer?")
    print (" ")
    print ("1.Conocer las concentraciones con las que cuenta el Tec para LAD")
    print ("2. Acerca del programa")
    print (" ")
    opcion = int(input("Inserta el número de lo que quieras hacer: "))
    return opcion

def menuAcercaDe(numero):
    lista = ["Paloma Cueto","A01746765","Fundamentos de programación", "LAD","Programa que ayuda a escoger concentración"]
    tipo = lista[numero]
    return tipo
    
def menuConcentraciones():
    print ("------------------------------------------------------------")
    print ("Las concentraciones con las que cuenta el Tec son:")
    print (" ")
    print ("1. Animación")
    print ("2. Efectos visuales")
    print ("3. Videojuegos")
    print ("4. Desarrollo visual")
    print ("0. Salir")
    print (" ")
    opcion = int (input("Inserta el número del área que te interese más: "))
    return opcion

def preguntasAnimacion():
    print ("Ingresa 1 si tu respuesta es SI")
    print ("Ingresa 0 si tu respuesta es NO")

    print (" ")
    pre = int (input ("¿Te gusta generar emociones a tráves de los modelos? "))
    pre1 = int (input ("¿Eres bueno aplicando los 12 principios de la animación? "))
    pre2 = int (input ("¿Te gusta el rigging? "))
    pre3 = int (input ("¿Sabes programar? "))
    pre4 = int (input ("¿Estás interesado en lightning? "))
    pre5 = int (input ("¿Sabías que las texturas son parte fundamental de la animación? "))
    print (" ")
    
    respuestas = pre + pre1 + pre2 + pre3 + pre4 + pre5
    
    if respuestas >= 4:
        return True
    else:
        return False
        
def materiasAnimacion():
    print ("Estas son las materias que lleva la concentración de animación:")
    print (" ")
    print ("-Imagen en movimiento")
    print ("-Generación de esqueletos")
    print ("-Animación avanzada")
    print ("-Proyecto integrador de arte")
    print ("-Luz y textura para Arte Digital")
    print ("-Animación digital 2D")
    print (" ")
    
    
    campus = int (input("¿Te gustaría saber en que campus se imparte esta concentración? "))
        
    if campus == 1:
        print ("Guadalajara, Queretaro, Monterrey, Puebla, Santa Fe y Ciudad de México")
        print (" ")        
    else:
        print ("Gracias por participar en esta encuesta")
        
def preguntasVFX():
    print ("Ingresa 1 si tu respuesta es SI")
    print ("Ingresa 0 si tu respuesta es NO")

    print (" ")
    pre = int (input ("¿Conoces el uso de la pantalla verde? "))
    pre1 = int (input ("¿Tu nivel de after effects es avanzado? "))
    pre2 = int (input ("¿Te gusta agregar efectos a escenas ya grabadas? "))
    pre3 = int (input ("¿Estas informado sobre el pipeline de postproducción? "))
    pre4 = int (input ("¿Te gusta la realización cinematográfica? "))
    pre5 = int (input ("¿Estás interesado en el MoCap? "))
    print (" ")
    
    respuestas = pre + pre1 + pre2 + pre3 + pre4 + pre5
    
    if respuestas >= 4:
        return True
    else:
        return False
    
def materiasVFX():
    print ("Estas son las materias que lleva la concentración de efectos visuales:")
    print (" ")
    print ("-Proyecto integrador de efectos visuales")
    print ("-Realización cinematográfica")
    print ("-Captura de movimiento")
    print ("-Composición digital avanzada para FX")
    print ("-Producción de efectos visuales para medios digitales")
    print ("-Postproducción digital")
    print (" ")
    
    
    campus = int (input("¿Te gustaría saber en que campus se imparte esta concentración? "))
    print (" ")
        
    if campus == 1:
        print ("Guadalajara, Monterrey, Estado de México, Santa Fe y Ciudad de México")
        print (" ")        
    else:
        print ("Gracias por participar en esta encuesta")
        
def preguntasVideojuegos():
    print ("Ingresa 1 si tu respuesta es SI")
    print ("Ingresa 0 si tu respuesta es NO")

    print (" ")
    pre = int (input ("¿Conoces el proceso para el diseño de personajes? "))
    pre1 = int (input ("¿Sabes programar? "))
    pre2 = int (input ("¿Te gusta crear escenarios virtuales? "))
    pre3 = int (input ("¿Sabes sacar uv´s para texturizar los modelos? "))
    pre4 = int (input ("¿Te gusta modelar? "))
    pre5 = int (input ("¿Sabes usar Substance Painter? "))
    print (" ")
    
    respuestas = pre + pre1 + pre2 + pre3 + pre4 + pre5
    
    if respuestas >= 4:
        return True
    else:
        return False
    
def materiasVideojuegos():
    print ("Estas son las materias que lleva la concentración de videojuegos:")
    print (" ")
    print ("-Desarrollo de videojuegos")
    print ("-Diseño de contenido para videojuegos")
    print ("-Ambientes virtuales")
    print ("-Modelación y texturizado para videojuegos")
    print ("-Animación interactiva para dispositivos móviles")
    print ("-Gráficas computacionales")
    print (" ")
    
    
    campus = int (input("¿Te gustaría saber en que campus se imparte esta concentración? "))
    print (" ")
        
    if campus == 1:
        print ("Guadalajara, Queretaro y Estado de México")
        print (" ")        
    else:
        print ("Gracias por participar en esta encuesta")
    
def preguntasDVisual():
    print ("Ingresa 1 si tu respuesta es SI")
    print ("Ingresa 0 si tu respuesta es NO")

    print (" ")
    pre = int (input ("¿Conoces el proceso del storyboard? "))
    pre1 = int (input ("¿Te gusta diseñar personajes? "))
    pre2 = int (input ("¿Tu nivel de anatomia es alto? "))
    pre3 = int (input ("¿Te gusta crear escenarios? "))
    pre4 = int (input ("¿Sabes usar la teoría del color? "))
    pre5 = int (input ("¿Te gusta transmitir mensajes a tráves del dibujo? "))
    print (" ")
    
    respuestas = pre + pre1 + pre2 + pre3 + pre4 + pre5
    
    if respuestas >= 4:
        return True
    else:
        return False
    
def materiasDVisual():
    print ("Estas son las materias que lleva la concentración de desarrollo visual:")
    print (" ")
    print ("-Dirección de arte para medios visuales")
    print ("-Técnicas avanzadas de representación digital")
    print ("-Arte secuencial")
    print ("-Dibujo digital de escenarios")
    print ("-Escultura 3D")
    print ("-Proyecto integrador de arte y tecnología")
    print (" ")
    
    
    campus = int (input("¿Te gustaría saber en que campus se imparte esta concentración? "))
    print (" ")
        
    if campus == 1:
        print ("Guadalajara, Monterrey, Estado de México, Santa Fe y Ciudad de México")
        print (" ")        
    else:
        print ("Gracias por participar en esta encuesta")
        
def graficaRespuestas(respuestas):
    
    if respuestas == True:
        imagen = Image.open("respuesta0.png")
        imagen.show()
    else:
        imagen = Image.open("respuesta1.png")
        imagen.show()
    
def main():
    print ("¡Bienvenido!")
    print ("---------------------------------------------------------------")
    menu = menuPrincipal()
    
    if menu == 1:
        opcion = menuConcentraciones()
        while opcion != 0:
            if opcion == 1:        
                imagen = Image.open("rigging.png")  #imprimir imagenes
                imagen.show()
                imagen2 = Image.open("modelado.jpg")
                imagen2.show()
                print ("------------------------------------------------------------------")
                print ("Estos son ejemplos de animación, veamos si es lo tuyo")
                print (" ")
                respuestas = preguntasAnimacion()
                graficaRespuestas(respuestas)
                if respuestas == True:
                    print ("---------------------------------------------------------------")
                    print ("Esta parece ser una concentración para ti")
                    print ("---------------------------------------------------------------")
                    imagenA = Image.open("animacion.png")
                    imagenA.show()
                    materiasAnimacion()
                else:
                    print ("---------------------------------------------------------------")
                    print("Esta no parece ser una concentración para ti, intenta de nuevo")
                    print ("---------------------------------------------------------------")
            elif opcion == 2:
                imagen = Image.open("vfx1.jpg")
                imagen.show()
                imagen2 = Image.open("vfx2.jpg")
                imagen2.show()
                print ("------------------------------------------------------------------")
                print ("Estos son ejemplos de efectos visuales, veamos si es lo tuyo")
                print (" ")
                respuestas = preguntasVFX()
                graficaRespuestas(respuestas)
                if respuestas == True:
                    print ("---------------------------------------------------------------")
                    print ("Esta parece ser una concentración para ti")
                    print ("---------------------------------------------------------------")
                    imagenA = Image.open("efectosVisuales.png")
                    imagenA.show()
                    materiasVFX()
                else:
                    print ("---------------------------------------------------------------")
                    print("Esta no parece ser una concentración para ti, intenta de nuevo")
                    print ("---------------------------------------------------------------")
            elif opcion == 3:
                imagen = Image.open("game1.jpg")
                imagen.show()
                imagen2 = Image.open("game2.jpg")
                imagen2.show()
                print ("------------------------------------------------------------------")
                print ("Estos son ejemplos de videojuegos, veamos si es lo tuyo")
                print (" ")
                respuestas = preguntasVideojuegos()
                graficaRespuestas(respuestas)
                if respuestas == True:
                    print ("---------------------------------------------------------------")
                    print ("Esta parece ser una concentración para ti")
                    print ("---------------------------------------------------------------")
                    imagenA = Image.open("videojuegos.png")
                    imagenA.show()
                    materiasVideojuegos()
                else:
                    print ("---------------------------------------------------------------")
                    print("Esta no parece ser una concentración para ti, intenta de nuevo")
                    print ("---------------------------------------------------------------")
            elif opcion == 4:
                imagen = Image.open("Dvisual1.jpg")
                imagen.show()
                imagen2 = Image.open("Dvisual2.jpg")
                imagen2.show()
                print ("------------------------------------------------------------------")
                print ("Estos son ejemplos de efectos visuales, veamos si es lo tuyo")
                print (" ")
                respuestas = preguntasDVisual()
                graficaRespuestas(respuestas)
                if respuestas == True:
                    print ("---------------------------------------------------------------")
                    print ("Esta parece ser una concentración para ti")
                    print ("---------------------------------------------------------------")
                    imagenA = Image.open("desarrolloVisual.png")
                    imagenA.show()
                    materiasDVisual()
                else:
                    print ("---------------------------------------------------------------")
                    print("Esta no parece ser una concentración para ti, intenta de nuevo")
                    print ("---------------------------------------------------------------")
            else:
                print ("---------------------------------------------------------------")
                print ("ERROR, favor de insertar un número del 0 al 4")
                print ("---------------------------------------------------------------")
            opcion = menuConcentraciones()
                
        
    else:
        print ("---------------------------------------------------------------")    #Acerca de 
        print ("0. Nombre del alumno")
        print ("1. Matrícula del alumno")
        print ("2. Materia")
        print ("3. Carrera del alumno")
        print ("4. Función del programa")
        print (" ")
        numero = int (input("Ingresa el número de lo que quieres conocer acerca del programa: "))
        dato = menuAcercaDe(numero)
        print (dato)
    
    
main()