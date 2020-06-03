#Autor: Michelle Ojeda Manjarrez
#Mostrar imagenes y música con especificaciones del usuario


#Importar librería PIL y playsound
from PIL import Image, ImageOps
from playsound import playsound


#Definir la opción del menú
def menu ():
    print ('''
        ¡Bienvenido a Encuéntrame! La aplicación que te ayuda a buscar imágenes y música con las especificaciones
        que estás buscando.
        
        MENÚ
        1. Imágenes
        2. Música
        0. Salir
        ''')
    
    opcion = int (input ("¿Qué tipo de material estás buscando hoy?: "))
    return opcion


#Definimos la lista de imagenes
def buscarImagen (formato, color, tamano):
    
    i = 0
    
    lista = ["perroChicoColor.png", "perroMedianoColor.png", "perroGrandeColor.png",
             "perroChicoBN.png","perroMedianoBN.png", "perroGrandeBN.png",
             "perroChicoColor.jpg", "perroMedianoColor.jpg", "perroGrandeColor.jpg",
             "perroChicoBN.jpg", "perroMedianoBN.jpg", "perroGrandeBN.jpg"]
    
    #Formato
    if formato == 1:
        i = 0
        nombre = "PNG"
        print (nombre)
    
    elif formato == 2:
        i = i + 6
        nombre = "JPG"
        print (nombre)
    
            
    #Color
    if color ==1:
        pass
        nombre = "Color"
        print (nombre)
        
    elif color == 2:
        i = i + 3
        nombre = "Blanco y negro"
        print (nombre)
        
        
    #Tamaño
    if tamano == 1:
        pass
        nombre = "Chico"
        print (nombre)
        
    elif tamano ==2:
        i = i + 1
        nombre = "Mediano"
        print (nombre)
        
    elif tamano ==3:
        i = i + 2
        nombre = "Grande"
        print (nombre)
        
    indice = lista[i]
    return(indice)


#Definimos la lista de música
def buscarMusica(duracion, animo, instrumento):
    
    i = 0
    
    lista = ["FelizPiano1.mp3", "FelizBajo1.mp3", "FelizTrompeta1.mp3",
             "TristePiano1.mp3", "TristeBajo1.mp3", "TristeTrompeta1.mp3",
             "InspiradorPiano1.mp3", "InspiradorBajo1.mp3", "InspiradorTrompeta1.mp3",
             "FelizPiano2.mp3", "FelizBajo2.mp3", "FelizTrompeta2.mp3",
             "TristePiano2.mp3", "TristeBajo2.mp3", "TristeTrompeta2.mp3",
             "InspiradorPiano2.mp3", "InspiradorBajo.mp3", "InspiradorTrompeta2.mp3"]
    
    #Duración
    if duracion == 1:
        i = 0
        nombre = "Menos de 30 segs"
        print (nombre)
        
    elif duracion == 2:
        i = i + 9
        nombre = "Más de 30 segs"
        print (nombre)
        
    #Ánimo
    if animo == 1:
        pass
        nombre = "Feliz"
        print (nombre)
    elif animo == 2:
        i = i + 3
        nombre = "Triste"
        print (nombre)
        
    elif animo ==3:
        i = i + 6
        nombre = "Inspirador"
        print (nombre)
        
    #Instrumento
    if instrumento == 1:
        pass
        nombre = "Piano"
        print (nombre)
        
    elif instrumento == 2:
        i = i + 1
        nombre = "Bajo"
        print (nombre)
        
    elif instrumento ==3:
        i = i + 2
        nombre = "Trompeta"
        print (nombre)
    
    indice = lista[i]
    return (indice)


#Función principal
def main ():
    
    opcion = menu()
    
    while opcion != 0:
        
        #Imágenes
        if opcion ==1:
            
            formato = int (input ("¿Qué tipo de formato buscas: 1. png o 2. jpg?: "))
            while formato !=1 and formato != 2:
                print ("ERROR, TECLEA [1,2]")
                formato = int (input ("¿Qué tipo de formato buscas: 1. png o 2. jpg?: "))
            
            color = int (input ("¿Color o blanco y negro? 1. Color, 2. Blanco y negro: "))
            while color !=1 and color != 2:
                print ("ERROR, TECLEA [1,2]")
                color = int (input ("¿Color o blanco y negro? 1. Color, 2. Blanco y negro: "))
                    
            tamano = int (input ("¿De qué tamaño? 1. Chico, 2. Mediano, 3. Grande:"))
            while tamano !=1 and tamano != 2 and tamano !=3:
                print ("ERROR, TECLEA [1,2,3]")
                tamano = int (input ("¿De qué tamaño? 1. Chico, 2. Mediano, 3. Grande:"))
                    
            print ("\n¡Aquí está tu imagen con las características que pediste!: ")

            imagen = buscarImagen (formato, color, tamano)
            print ("\nEl nombre del archivo es: " ,imagen)
            print ("\n")
            
            imagen = Image.open (imagen)
            imagen.show()
            
        #Música
        elif opcion ==2:
            
            duracion = int(input("¿Cúanto quieres que dure: 1.Menos de 30 segs 2.Más de 30 segs?:"))
            while duracion !=1 and duracion != 2:
                print ("ERROR, TECLEA [1,2]")
                duracion = int(input("¿Cúanto quieres que dure: 1.Menos de 30 segs 2.Más de 30 segs?: "))
                 
            animo = int(input("¿Qué tipo de ánimo para la canción buscas: 1.Feliz o 2.Triste o 3.Inspirador?: "))
            while animo !=1 and animo != 2 and animo != 3:
                print ("ERROR, TECLEA [1,2,3]")
                animo = int(input("¿Qué tipo de ánimo para la canción buscas: 1.Feliz o 2.Triste o 3.Inspirador?: "))
                
            instrumento = int(input("¿Qué tipo de instrumento buscas: 1.Piano o 2.Bajo o 3.Trompeta?: "))
            while instrumento !=1 and instrumento != 2 and instrumento != 3:
                print ("ERROR, TECLEA [1,2,3]")
                instrumento = int(input("¿Qué tipo de instrumento buscas: 1.Piano o 2.Bajo o 3.Trompeta?: "))
            
            
            print ("\n¡Aquí está la canción con las características que pediste!:")
            print ("(Se escuchará únicamente 15segs de la canción)")
            
            
            musica = buscarMusica(duracion, animo, instrumento)
            print ("\nEl nombre del archivo es: " ,musica)
            print ("\n")
            
            playsound (musica)
        
            
        else:
            print ("ERROR, debes teclear [1,2,0]")
            
        opcion = menu ()
    
    print ("\n¡Gracias por usar Encuéntrame, regresa pronto!")

main ()