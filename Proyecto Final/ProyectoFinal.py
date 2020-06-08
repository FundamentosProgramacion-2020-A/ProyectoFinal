#Autor: Ana Fernanda Martinez Garcia
#Historia Interactiva, Proyecto

from playsound import playsound
import time
import random
from PIL import Image

items = []

#Para imprimir con tiempo (time.sleep)
#3 segundos
def print_sleep(cosaImprimir):
    print(cosaImprimir)
    time.sleep(3)
    
#2 segundos
def print_sleep1(cosaImprimir):
    print(cosaImprimir)
    time.sleep(2)
    
#1 segundo   
def print_sleep2(cosaImprimir):
    print(cosaImprimir)
    time.sleep(1)

#poner música de fondo en todo el juego   
def musica():

    playsound ("Night.mp3",0)
    
def print_1(cosaImprimir):
    print(cosaImprimir)
 
#Intro de la historia
def intro():
    print_sleep("En tu camino regresando de un evento te pierdes")
    print_sleep("muy irresponsable de ti por no guardar la cuarentena...")
    print_sleep("Te encuentras en un bosque obscuro y solitario...")
    image = Image.open('n1.png')
    image.show()
    print_sleep("Frente a ti hay tres caminos.")
    print_sleep("Ves una casa abandonada al final del primer camino,")
    print_sleep("escuchas un estraño y lúgubre sonido del segundo camino")
    print_sleep("y puedes escuchar un autobús al final del tercer camino.")

#Preguntas de Inicio
def begining():
    print("\n")
    print_sleep("1.¿Quieres ver si hay ayuda esperando en la casa abandonada? ")
    print_sleep("2.¿Quieres ver qué fue ese extraño ruido?")
    print_sleep("3.¿O quisieras ir al autobús?")
    print_sleep2("¿Por cual camino quisieras ir?")
    
#Poner ganardor random con lista
def ganadorRandom():
    image = Image.open('9.jpg')
    image.show()
    listaGanador = ["Buen trabajo","Bien hecho...Sherlock","Hey, no moriste",":) Bien hecho"]
    print_sleep(random.choice(listaGanador))
    
    
#Jugador Pierde
def lost_play_again():
    print_sleep("¡HAS MUERTO!")
    image = Image.open('over.jpg')
    image.show()
    print_sleep("Game Over...")
    print_sleep("¿Te gustaría jugar de nuevo?")
    answer = input("ingresa y/n\n")
    if answer == "y":
        game()
    elif answer == "n":
        print_sleep("Gracias por jugar,")
        print_sleep("más suerte para la próxima...")
        exit()
    else:
        print_sleep("No entiendo...")
   
#  Camino 1
def passageway_1():
    print("\n")
    print_sleep("Caminas hacia la casa ...")
    if "key" in items:
        print_sleep("Pones tu llave en la cerradura")
        print_sleep("y logras abrirla")
        print_sleep("todo esta lleno de telarañas y un extraño olor a moho.")
        print_sleep("Caminas y encuentras un papel azul brillante")
        image = Image.open('ticket.jpg')
        image.show()
        print_sleep("decides agarrarlo, quizar sirva para algo")
        print_sleep("regresas de donde venias")
        items.append("ticket")
    elif "key" not in items:
        print_sleep("te hacercas a la puerta...")
        print_sleep("la puerta esta cerrada.")
        print_sleep("Intentas romper la puerta, pero el monstruo de la casa te ataca!")
        lost_play_again()
 
# Camino 2
def passageway_2():
    print("\n")
    if "key" not in items:
        print_sleep("Mientras caminas por el pasillo, el sonido extraño comienza a desvanecerse")
        print_sleep("¡aparece una caja de tesoro brillante!")
        print_sleep("La abres y encuntras una llave")
        image = Image.open('key.jpg')
        image.show()
        print_sleep("Decides quedarte con la llave y regresar")
        items.append("key")
    elif "key"  in items:
        print_sleep("Decides volver")
        print_sleep("Fue una muy mala idea ...")
        print_sleep("¡El ruido ha regresado y resulta ser un aullido de monstruo con grandes antenas!")
        answer = input("¿Qué haces? ¡Escribe 1 para correr y 2 para actuar muerto!\n")
        if answer == "1":
            print_sleep("Corres lo más rapido que puedes, pero el monstruo es más rápido...")
            print_sleep("Te come y mueres!")

            lost_play_again()
        elif answer == "2":
            print_sleep("Te haces el muerto, pero el monstruo tiene hambre...")
            print_sleep(" Te come y mueres...")
            lost_play_again()
# Camino 3          
def passageway_3():
    print("\n")
    if "ticket" in items:
        print_sleep("Le das el ticket al conductor del bus,")
        print_sleep("te deja cerca de una estación del metro,")
        print_sleep("regresas a casa sano y salvo.")
        ganadorRandom()
        print_sleep("¡¡Lo hiciste, felicidades!!")
        print_sleep("¿Quieres jugar de nuevo?")
        answer=input("responde y/n\n")
        if answer == "y":
            game()
        elif answer == "n":
            print_sleep2("Gracias por jugar")
            exit()
        else:
            print_sleep("No entiendo...")
            answer=input("por favor responde y/n\n")
            if answer == "y":
                game()
            elif answer == "n":
                print_sleep2("Gracias por jugar")
                exit()

    else:
        print_sleep("El conductor del autobús habría tomado dinero en efectivo para llevarte,")
        print_sleep("pero debido a las regulaciones por el Covid-19 no se le permite tomar efectivo")
        print_sleep("Te encuentras frente a los tres caminos de nuevo...")
 

# Créditos del juego
def creditos():
 
    print("\n")
    print("Mayo 2020")
    print("\n") 
    print( "Ana Fernanda Martínez García           A01377832")
    print("\n")
    print ('-'*50)
    print( "             Fundamentos de Programación")
    print ('-'*50)
    print("\n")
    print("Música: Night in the Woods-Main Theme")
    print("\n")

#Main 
def game():
    print("\n")
    print('^'*100)
    print("\n")
    print('\n')
    print ('-'*100)
    print('                                  Noche de Cuarentena - El Juego'.title())
    print ('-'*100)
    print("Este es un juego con recursos audiovisuales")
    print("\n")
    print("Sube el volumen para la música y recuerda que puede haber imagenes emergentes")
    print("ajusta las ventanas para una mejor visualización.")
    print('\n')
    print ("Bienvenido! En este juego eres alguien que no guardo la cuarentena, y estas perdido en un bosque, buena suerte regresando a casa.")
    print('\n')
 
    
    musica()
    
    a= 1
    while (a > 0):

        a = int(input("""
        1. Iniciar
        2. Créditos
        3. Salir
        
        Por favor ingresa 1, 2 o 3 \n """))

        if a == 1:
            print("\n")
            intro()
            while True:
                 begining()
                 passageway = input("Por favor ingresa 1, 2 o 3 \n")
                 if passageway == "1":
                     passageway_1()
                 elif passageway == "2":
                     passageway_2()
                 elif passageway == "3":
                     passageway_3()
                     
        elif a == 2:
            print("\n")
            creditos()
            
        elif a == 3:
            print_sleep2("hasta la próxima...")
            exit()
            
        else:
             print_sleep("No entiendo...")

         
game()