#Autor: Sharone Márquez, A01746940
#Proyecto final de programación sobre una aplicación que genera paletas de color
from PIL import Image

def cargarImagenes(archivo):  #CARGA DE IMAGENES PARA MOSTRAR
    imagen= Image.open(archivo)
    return imagen

def menu(): #MENU PRINCIPAL
    print("MENÚ PRINCIPAL")
    print('''¡Hola! este es un generador de paletas de color básico para ayudarte en tu ilustración y partirá de los colores primarios como base. ¿Qué opción quisieras ver?
Ver paleta de color rojo (1)
Ver paleta de color azul (2)
Ver paleta de color amarillo (3)
Acerca de (4)
Salir del programa (0)''')
    print(" ")
    opcion= int(input('''PRESIONE el número que está a lado de la opción para mostrar.
: '''))
    print(" ")
    
    return opcion
    
def main():  #PROGRAMA PRINCIPAL
    opcion = menu()
#------------------------------------------------ COLOR ROJO -------------------------------------------------    
    while opcion != 0:
        if opcion == 1:
            print("PALETA DE COLOR ROJO")
            colorRojo= int(input('''Estas son tus opciones para la paleta de color rojo. PRESIONE el número que aparece a lado de las opciones para mostrar:
Combinación genérica (1)
Variación del color (2)
Combinación especial (3)
: '''))
            print(" ")
            if colorRojo == 1: #mostrar la muestra no. 1
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(0, 4):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_rojo1.png")
                imagen.show()
                print(" ")
            
            elif colorRojo == 2: #mostrar la muestra no. 2
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(5, 9):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_rojo2.png")
                imagen.show()
                print(" ")
                
            elif colorRojo == 3: #mostrar la muestra no. 3
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(9, 13):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_rojo3.png")
                imagen.show()
                print(" ")
                
            elif colorRojo != 1 or colorRojo != 2 or colorRojo != 3:
                print("-------------------------------------------------------------------")
                print("Esta opción es inválida, debes PRESIONAR un número del 1 al 3.")
                print(" ")

            respuesta = input("¿Te gustaría ver dos opciones más? ESCRIBE SOLAMENTE si o no: ")  #------>> SI QUIERE PROBAR OTRA OPCIÓN
            print(" ")
            if respuesta == 'si' or respuesta == 'Si' or respuesta == 'SI':
                tono = input('''¿Qué tonalidad quisieras ver? ESCRIBE la opción para mostrar:
1. Claro
2. Oscuro
: ''')
                print(" ")
                if tono == 'claro' or tono == 'Claro' or tono == 'CLARO': #mostar la opcion pastel
                    gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                          '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                          '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                    for i in range(13, 17):
                        print(gama[i])
 
                    imagen= cargarImagenes("muestra_roclaro.png")
                    imagen.show()
                    print(" ")
                    salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                    print("--------------------------------------------------------------------------------------- ")
                    if salida == 0:
                        imagen= cargarImagenes("grafica.png")
                        imagen.show()
                    else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
                        
                elif tono == 'oscuro' or tono == 'Oscuro' or tono == 'OSCURO': #mostrar la opcion oscura
                    gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                          '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                          '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                    for i in range(17, 21):
                        print(gama[i])
                        
                    imagen= cargarImagenes("muestra_rooscuro.png")
                    imagen.show()
                    print(" ")
                    salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                    print("--------------------------------------------------------------------------------------- ")
                    if salida == 0:
                        imagen= cargarImagenes("grafica.png")
                        imagen.show()
                    else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
                             
                else:
                    print("-------------------------------------------------------------------")
                    print("Esta opción es inválida, debe ESCRIBIR la opción para mostrar. Vuelve a intentarlo.")
                    print(" ")
                    
                    
            elif respuesta == 'no' or respuesta == 'No' or respuesta == 'NO':
                print(" ")
                salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                print("--------------------------------------------------------------------------------------- ")
                if salida == 0:
                    imagen= cargarImagenes("grafica.png")
                    imagen.show()
                else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
            
            else:
                print("-------------------------------------------------------------------")
                print("Esta opción es inválida, debe ESCRIBIR la opción para mostrar. Vuelve a intentarlo.")
                print(" ")
#-------------------------------------------------------- COLOR AZUL -----------------------------------------------            
        elif opcion == 2:
            print("PALETA DE COLOR AZUL")
            colorAzul= int(input('''Estas son tus opciones para la paleta de color azul. PRESIONE el número que aparece a lado de las opciones para mostrar:
Combinación genérica (1)
Variación del color (2)
Combinación especial (3)
: '''))
            print(" ")
            if colorAzul == 1: #mostrar la muestra no. 1
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(0, 4):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_azul1.png")
                imagen.show()
                print(" ")
            
            elif colorAzul == 2: #mostrar la muestra no. 2
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(5, 9):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_azul2.png")
                imagen.show()
                print(" ")
                
            elif colorAzul == 3: #mostrar la muestra no. 3
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(9, 13):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_azul3.png")
                imagen.show()
                print(" ")
                
            elif colorAzul != 1 or colorAzul != 2 or colorAzul != 3:
                print("-------------------------------------------------------------------")
                print("Esta opción es inválida, debes PRESIONAR un número del 1 al 3.")
                print(" ")

            respuesta = input("¿Te gustaría ver dos opciones más? ESCRIBE SOLAMENTE si o no: ")  #------>> SI QUIERE PROBAR OTRA OPCIÓN
            print(" ")
            if respuesta == 'si' or respuesta == 'Si' or respuesta == 'SI':
                tono = input('''¿Qué tonalidad quisieras ver? ESCRIBE la opción para mostrar:
1. Claro
2. Oscuro
: ''')
                print(" ")
                if tono == 'claro' or tono == 'Claro' or tono == 'CLARO': #mostar la opcion pastel
                    gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                          '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                          '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                    for i in range(13, 17):
                        print(gama[i])
 
                    imagen= cargarImagenes("muestra_azuclaro.png")
                    imagen.show()
                    print(" ")
                    salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                    print("--------------------------------------------------------------------------------------- ")
                    if salida == 0:
                        imagen= cargarImagenes("grafica.png")
                        imagen.show()
                    else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
                        
                elif tono == 'oscuro' or tono == 'Oscuro' or tono == 'OSCURO': #mostrar la opcion oscura
                    gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                          '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                          '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                    for i in range(17, 21):
                        print(gama[i])
                        
                    imagen= cargarImagenes("muestra_azuoscuro.png")
                    imagen.show()
                    print(" ")
                    salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                    print("--------------------------------------------------------------------------------------- ")
                    if salida == 0:
                        imagen= cargarImagenes("grafica.png")
                        imagen.show()
                    else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
                             
                else:
                    print("-------------------------------------------------------------------")
                    print("Esta opción es inválida, debe ESCRIBIR la opción para mostrar. Vuelve a intentarlo.")
                    print(" ")
                    
                    
            elif respuesta == 'no' or respuesta == 'No' or respuesta == 'NO':
                print(" ")
                salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                print("--------------------------------------------------------------------------------------- ")
                if salida == 0:
                    imagen= cargarImagenes("grafica.png")
                    imagen.show()
                else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
            
            else:
                print("-------------------------------------------------------------------")
                print("Esta opción es inválida, debe ESCRIBIR la opción para mostrar. Vuelve a intentarlo.")
                print(" ")
#-------------------------------------------------------- COLOR AMARILLO ------------------------------------------
        elif opcion == 3:
            print("PALETA DE COLOR AMARILLO")
            colorAmarillo= int(input('''Estas son tus opciones para la paleta de color amarillo. PRESIONE el número que aparece a lado de las opciones para mostrar:
Combinación genérica (1)
Variación del color (2)
Combinación especial (3)
: '''))
            print(" ")
            if colorAmarillo == 1: #mostrar la muestra no. 1
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(0, 4):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_amarillo1.png")
                imagen.show()
                print(" ")
            
            elif colorAmarillo == 2: #mostrar la muestra no. 2
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(5, 9):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_amarillo2.png")
                imagen.show()
                print(" ")
                
            elif colorAmarillo == 3: #mostrar la muestra no. 3
                gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                      '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                      '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                for i in range(9, 13):
                    print(gama[i])
                    
                imagen= cargarImagenes("muestra_amarillo3.png")
                imagen.show()
                print(" ")
                
            elif colorAmarillo != 1 or colorAmarillo != 2 or colorAmarillo != 3:
                print("-------------------------------------------------------------------")
                print("Esta opción es inválida, debes PRESIONAR un número del 1 al 3.")
                print(" ")

            respuesta = input("¿Te gustaría ver dos opciones más? ESCRIBE SOLAMENTE si o no: ")  #------>> SI QUIERE PROBAR OTRA OPCIÓN
            print(" ")
            if respuesta == 'si' or respuesta == 'Si' or respuesta == 'SI':
                tono = input('''¿Qué tonalidad quisieras ver? ESCRIBE la opción para mostrar:
1. Claro
2. Oscuro
: ''')
                print(" ")
                if tono == 'claro' or tono == 'Claro' or tono == 'CLARO': #mostar la opcion pastel
                    gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                          '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                          '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                    for i in range(13, 17):
                        print(gama[i])
 
                    imagen= cargarImagenes("muestra_amaclaro.png")
                    imagen.show()
                    print(" ")
                    salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                    print("--------------------------------------------------------------------------------------- ")
                    if salida == 0:
                        imagen= cargarImagenes("grafica.png")
                        imagen.show()
                    else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
                        
                elif tono == 'oscuro' or tono == 'Oscuro' or tono == 'OSCURO': #mostrar la opcion oscura
                    gama=['#F01010', '#FFF600', '#82E94E', '#1F9F29', '#1F9F29', '#F01010', '#FF8300', '#FFF600', '#F01010', '#FF8300', '#00BAE2', '#C2F9FF', '#FF4D4D', '#FF8364', '#FDB87D', '#FEFBD5', '#9F0D0A', '#C52E25', '#590000', '#170000',\
                          '#0098FF', 'FFF600', '#FF8300', '#F01010', '010336', '#0098FF', '#00BAE2', '#FFF600', '#0098FF', '#C52E25', '#F01010', '#EAEAEA', '#5EC2FF', '#88B9FF', '#B2E2FF', '#9FC4DB', '#041B34', '#0F1570', '#2C68B8', '#001E8A',\
                          '#FFF600', '#FF8300', '#444444', '#FEFFDB', '#FFF600', '#F8F1D0', '#0B8434', '#096C47', '#244090', '#FFF600', '#FFAD49', '#FF6A6A', '#FFFF64', '#D5C455', '#EDE59A', '#F6F4E6', '#D8C43C', '#C2AC17', '#877811', '#4E4505']
                    for i in range(17, 21):
                        print(gama[i])
                        
                    imagen= cargarImagenes("muestra_amaoscuro.png")
                    imagen.show()
                    print(" ")
                    salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                    print("--------------------------------------------------------------------------------------- ")
                    if salida == 0:
                        imagen= cargarImagenes("grafica.png")
                        imagen.show()
                    else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
                             
                else:
                    print("-------------------------------------------------------------------")
                    print("Esta opción es inválida, debe ESCRIBIR la opción para mostrar. Vuelve a intentarlo.")
                    print(" ")
                    
                    
            elif respuesta == 'no' or respuesta == 'No' or respuesta == 'NO':
                print(" ")
                salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
                print("--------------------------------------------------------------------------------------- ")
                if salida == 0:
                    imagen= cargarImagenes("grafica.png")
                    imagen.show()
                else:
                        print("Esta opción es incorrecta, debe PRESIONAR 0")
                        print(" ")
            
            else:
                print("-------------------------------------------------------------------")
                print("Esta opción es inválida, debe ESCRIBIR la opción para mostrar. Vuelve a intentarlo.")
                print(" ")
#------------------------------------------------------- ACERCA DE -------------------------------------------------   
        elif opcion == 4:
            for linea in open ("AcercaDe.txt", encoding='UTF-8'):
                cadena = linea.strip()
                print (cadena)
            
            print(" ")
            salida = int(input("Gracias por utilizar este programa. PRESIONE 0 para volver al menú principal: ")) #MENSAJE DE DESPEDIDA
            print("--------------------------------------------------------------------------------------- ")
            if salida == 0:
                print(" ")
            else:
                print("Esta opción es incorrecta, debe PRESIONAR 0")
                print(" ")
                
        else:
            print("-------------------------------------------------------------------")
            print("Esta opción es inválida, debe PRESIONAR un número del 0 al 4. Vuelve a intentarlo.")
            print(" ")
        
        opcion= menu() #MENU PRINCIPAL 
#----------------------------------------------------- CERRAR PROGRAMA -------------------------------------    
    print("El programa ha terminado.")
    
        
main()