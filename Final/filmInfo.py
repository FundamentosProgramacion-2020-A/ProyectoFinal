#Autor: Anayansi Alexia Tafoya Soto
# Aplicación que ayudará al crew de cualquier filmación al momento de grabación.

from PIL import Image, ImageOps  #de la libreria PIL, importamos Image, (ImageOps) hace operaciones con las imagenes.

from playsound import playsound  #de la librería playsound, importa las notas y lo ejecuta
import time



def menu ():
    print  ('''
        1. Escena 01
        2. Escena 02
        3. Escena 03
        4. Escena 04
        5. Escena 05
        6. Melodía
        0. Salir
    ''')
    opcion = int (input ("Teclea tu opción: "))
    return opcion


def cargarImagen (archivo):
    imagen = Image.open(archivo)
    return imagen


def tocarNota(nota, duracion):  #opcion06 
    playsound ("notas/Piano_" + nota + ".mp3", False)
    time.sleep(duracion)
  

def tocarMelodia():
    negra = 0.5
    blanca = 2*negra
    negraLarga =1.5*negra
    redonda = 4*negra
    duracion = 0
    
    melodia = ["E6", blanca, "E6", blanca, "D6", negra, "E6", blanca, "F6", negra, "E6", blanca,\
               "D6", negra, "C6", negra, "B5", blanca, "C6", blanca, "B5", negra, "C6", negra, "D6", blanca, \
               "E6", redonda, "C6", negra, "D6", negra, "E6", blanca ,"D6", negra, "E6", negra, "F6", blanca,\
               "G6", blanca, "F6", negra, "E6", blanca, "D6", negra, "C6", redonda, "C6", blanca, "C6", negra,\
               "A5", negra, "B5", negra, "C6", blanca, "B5", negra, "C6", negra, "D6", blanca, "C6", negra,\
               "B5", negraLarga, "A5", negra, "B5", negra, "C6", blanca, "B5", negra, "C6", negra, "D6", blanca,\
               "C6", redonda, "C6", blanca, "A5", negra, "B5", negra, "C6", blanca, "B5", negra, "C6", negra,\
               "D6", blanca, "C6", blanca, "B5", blanca, "A5", negra, "Ab5", negra, "A5", redonda, "A5", blanca,\
               "A5", redonda, "A5", blanca]
    
    for i in range  (0, len(melodia), 2):
        nota = melodia [i]
        duracion = melodia [i+1]
        tocarNota (nota, duracion)
        
    playsound ("notas/Piano_Silencio.mp3")

def main():
    print ("Las siguientes opciones mostrarán el storyboard, la paleta de colores y un texto con las especificaciones corresppondientes de la escena, deberás ingersar el número de la escena que necesites grabar.")
    print ("El video seleccionado fue la canción Piano Duet de la película: El cadaver de la Novia")
    
    opcion = menu()      
    while opcion !=0 :
        if opcion==1:
            imagen = cargarImagen("Escena01.jpg")
            imagen.show()    #Muestra el storyboard de la escena 01 en la pantalla
            
            paleta = cargarImagen("paleta01.jpg")
            paleta.show()    #Muestra la paleta de colores en la pantalla
            
            print ("\n")
            for linea in open ("01.txt"):
                cadena = linea.rstrip()
                print (cadena)
            
        elif opcion==2:
            imagen = cargarImagen("Escena02.jpg")
            imagen.show()    #Muestra el storyboard de la escena 02 en la pantalla
            
            paleta = cargarImagen("paleta02.jpg")
            paleta.show()    #Muestra la paleta de colores en la pantalla
            colores = cargarImagen("colores02.jpg")
            colores.show()    
            
            print ("\n")
            for linea in open ("02.txt"):
                cadena = linea.rstrip()
                print (cadena)
            
        elif opcion==3:
            imagen = cargarImagen("Escena03.jpg")
            imagen.show()    #Muestra el storyboard de la escena 03 en la pantalla
            
            paleta = cargarImagen("paleta03.jpg")
            paleta.show()    #Muestra la paleta de colores en la pantalla
            colores = cargarImagen("colores03.jpg")
            colores.show()    
            
            print ("\n")
            for linea in open ("03.txt"):
                cadena = linea.rstrip()
                print (cadena)
            
        elif opcion==4:
            imagen = cargarImagen("Escena04.jpg")
            imagen.show()    #Muestra el storyboard de la escena 04 en la pantalla
            
            paleta = cargarImagen("paleta04.jpg")
            paleta.show()    #Muestra la paleta de colores en la pantalla
            de = cargarImagen("de04.jpg")
            colores.show()    
            colores = cargarImagen("colores04.jpg")
            colores.show()
            
            print ("\n")
            for linea in open ("04.txt"):
                cadena = linea.rstrip()
                print (cadena)
            
        elif opcion==5:
            imagen = cargarImagen("Escena05.jpg")
            imagen.show()    #Muestra el storyboard de la escena 05 en la pantalla
            
            paleta = cargarImagen("paleta05.jpg")
            paleta.show()    #Muestra la paleta de colores en la pantalla
            de = cargarImagen("de05.jpg")
            de.show()    
            colores = cargarImagen("colores05.jpg")
            colores.show()    
            
            print ("\n")
            for linea in open ("05.txt"):
                cadena = linea.rstrip()
                print (cadena)
            
        elif opcion==6:
            tocarMelodia()
            
        else:
            print ("Opción incorrecta, debes teclear [01, 02]")
        opcion = menu()
        
        
    print ("Termina")
    

main()