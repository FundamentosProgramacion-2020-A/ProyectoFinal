#Autor: Valeria Huerta Pedregal
#Proyecto Final: Resolver problema de mi carrera (LCMD)

#Problemática: Falta de inspiración o bloqueo de creatividad para generar
#un concepto creativo para una narrativa

from PIL import ImageDraw, Image
from random import randint
import random

def definirPersonaje(genero):
    if genero == 1: #comedia
        lista = ["Una abuela promiscua", "Un niño nerd de 15 años", "Una mujer jóven CEO", "Un hombre joven empezando a trabajar en una empresa",
                 "Un doctor con dos familias"]
        azar = random.choice(lista)
        return azar
    elif genero == 2: #drama
        lista = ["Una mujer divorciada de 40 años", "Un jefe de mafia italiana de 50 años", "Un niño afroamericano homosexual de 15 años",
                 "Un mago ladrón", "Una niña huérfana buscando a sus papás"]
        azar = random.choice(lista)
        return azar
    elif genero == 3: #terror
        lista = ["Un monstruo de la laguna", "Un payaso esquizofrénico", "Un fantasma de alguna leyenda del folclore hispánico",
                 "Un niño diabólico internado en un hospital psiquiatra", "Una muñeca de porcelana"]
        azar = random.choice(lista)
        return azar
    elif genero == 4: #suspenso
        lista = ["Un científico norcoreano con tendencias psicópatas", "Un periodista arriesgado", "Un adolescente sordomudo", "Una niña autista de 10 años",
                 "Un oso polar salvaje"]
        azar = random.choice(lista)
        return azar
    elif genero == 5: #misterio
        lista = ["Un detective corrupto", "Un centauro peligroso", "Un profesor sospechoso", "Un pastor alemán policía", "Una persona que vive entre las paredes"]
        azar = random.choice(lista)
        return azar
    elif genero == 6: #romántico
        lista = ["Una hada madrina ingeniosa", "Un cupido disfrazado de un abuelo", "Un hombre joven recién egresado de la carrera", "Un niño que se enamora de todas las niñas",
                 "Un chofer de camión romántico"]
        azar = random.choice(lista)
        return azar
    elif genero == 7: #acción y aventura
        lista = ["Un policía astuto de 30 años", "Un asesino serial infiltrado en el gobierno", "Un narco mexicano infiltrado en el FBI/CIA","Un bebé ninja",
                 "Un guardaespaldas musulmán del presidente estaodunidense"]
        azar = random.choice(lista)
        return azar
    elif genero == 8: #ciencia ficción
        lista = ["Un virus de computadora personificado", "Un astronauta claustrofóbico", "El primer humano inmortal", "Un cíbnorg asesino",
                 "Un hoyo negro queriendo tragarse la tierra"]
        azar = random.choice(lista)
        return azar

def definirGeografia(genero):
    if genero == 1: #comedia
        lista = ["Buenos Aires, Argentina", "una empresa de botellas ecológicas", "un mundo fantástico", "Cancún, México",
                 "San Francisco, Estados Unidos", "un pueblo mágico"]
        azar = random.choice(lista)
        return azar
    elif genero == 2: #drama
        lista = ["un mundo fantástico", "Los Ángeles, Estados Unidos", "Sídney, Australia", "Antártica", "un salón de música", "una carcel"]
        azar = random.choice(lista)
        return azar
    elif genero == 3: #terror
        lista = ["un mundo fantástico", "el subterráneo de la tierra", "un hotel embrujado", "una casa embrujada", "Transilvania, Rumania", "Praga, República Checa"]
        azar = random.choice(lista)
        return azar
    elif genero == 4: #suspenso
        lista = ["un mundo fantástico", "la casa blanca", "San Antonio, Texas", "Edimburgo, Reino Unido", "un edificio de departamentos", "la selva"]
        azar = random.choice(lista)
        return azar
    elif genero == 5: #misterio
        lista = ["Toronto, Canadá", "Nueva York, Estados Unidos", "CDMX, México","un mundo fantástico", "un castillo europeo", "Londres, Inglaterra"]
        azar = random.choice(lista)
        return azar
    elif genero == 6: #romántico
        lista = ["Chicago, Estados Unidos", "Venecia, Italia", "Miconos, Grecia", "Zacatecas, México", "un suburbio",
                 "un estadio deportivo", "Rio de Janeiro, Brasil", "un mundo fantástico"]
        azar = random.choice(lista)
        return azar
    elif genero == 7: #acción y aventura
        lista = ["Moscú, Rusia", "Singapore, Singapore", "Santiago, Chile", "Hong Kong, Hong Kong", "una ciudad corrupta",
                 "un mundo fantástico"]
        azar = random.choice(lista)
        return azar
    elif genero == 8: #ciencia ficción
        lista = ["el espacio", "Marte", "la luna", "un sótano lleno de equipo tecnológico", "Tokio, Japón", "Berlín, Alemania",
                 "un mundo fantástico"]
        
def definirProblematica(genero):
    if genero == 1: #comedia
        lista = ["se enamora de su vecino", "se convierte en un personaje de libro", "descubre que es alérgico a las tortillas",
                 "viaja al pasado en un sillón", "quiere reemplazar a su jefe en el trabajo"]
        azar = random.choice(lista)
        return azar
    elif genero == 2: #drama
        lista = ["descubre que muere su último familiar", "pierde todo lo que tiene", "le detectan un tumor en la boca", "tiene un paro respiratorio",
                 "escribe un libro sobre su vida", "desea llegar a la fama cinematográfica"]
        azar = random.choice(lista)
        return azar
    elif genero == 3: #terror
        lista = ["atormenta a una familia rica", "le lava los cerebros a toda la población", "despierta a tres entes demoniacos",
                 "contagia una enfermedad que hace que las personas quieran suicidarse", "se quiere adueñar del alma de una persona"]
        azar = random.choice(lista)
        return azar
    elif genero == 4: #suspenso
        lista = ["busca venganza de su enemigo de la infancia", "secuestra a su vecino", "funda el primer club de asesinos seriales",
                 "investiga un mito de una casa embrujada", "escribe canciones y hace que se vuelvan realidad"]
        azar = random.choice(lista)
        return azar
    elif genero == 5: #misterio
        lista = ["busca resolver el caso de la celebridad desaparecida", "intenta escaparse de una cárcel", "investiga un cartel de drogas colombiano",
                 "se roba un artefacto precioso de la reina de Inglaterra", "descubre los secretos del vaticano"]
        azar = random.choice(lista)
        return azar
    elif genero == 6: #romántico
        lista = ["se enamora de una persona completamente opuesta a él/ella", "se enamora de su némesis", "se enamora de sí mismo",
                 "lee un libro sobre cómo evitar enamorarse y lo vuelve su filosofía de vida",
                 "logra vender café mágico que hace que los enamorados desconocidos se encuentren"] 
        azar = random.choice(lista)
        return azar
    elif genero == 7: #acción y aventura
        lista = ["desea matar al presidente del país", "busca salvar al mundo de una raza caníbal", "quiere revelar los secretos del gobierno",
                 "es el chofer del jefe de la mafia", "combate una especie alienígena que quiere dominar la Tierra"]
        azar = random.choice(lista)
        return azar
    elif genero == 8: #ciencia ficción
        lista = ["es el último recurso para salvar a la humanidad", "busca la paz mundial", "hace que los animales se vuelvan locos",
                 "diseña el primer robot serpentino", "destruye las partículas de oxígeno de la atmósfera"]
        azar = random.choice(lista)
        return azar
    
def definirEpoca(genero):
    if genero == 1: #comedia
        lista = ["actual.", "en la cual Trump entró a la presidencia.", "en la cual AMLO entró a la presidencia.", "prehistórica.",
                 "del nacimiento del reggaetón.", "del Porfiriato.", "del nacimiento de Tinder."] 
        azar = random.choice(lista)
        return azar
    elif genero == 2: #drama
        lista = ["actual.", "en la cual cayó el muro de Berlin.", "del ataque terrorista 9/11.", "de los 50s.", "de la Edad Media."
                 "de los esclavos."]
        azar = random.choice(lista)
        return azar
    elif genero == 3: #terror
        lista = ["actual.", "de la Edad media.", "de los 80s.", "de los 00s.", "de los 20s.", "apocalíptica."]
        azar = random.choice(lista)
        return azar
    elif genero == 4: #suspenso
        lista = ["actual.", "de los 80s.","del holocausto.", "100 años en el futuro.",
                 "en la cual mataron a John F. Kennedy."]
        azar = random.choice(lista)
        return azar
    elif genero == 5: #misterio
        lista = ["actual.", "de los 70s.", "del escándalo de Watergate.", "de la Edad media.", "del Renacimiento.",
                 "de la Revolución industrial."]
        azar = random.choice(lista)
        return azar
    elif genero == 6: #romántico
        lista = ["actual.", "de las antiguas civilizaciones.", "de Martin Luther King.", "de los 90s.",
                 "en la cual los 49ers ganaron el Superbowl en los 90s."]
        azar = random.choice(lista)
        return azar
    elif genero == 7: #acción y aventura
        lista = ["actual.", "500 años en el futuro.", "100 años en el futuro.", "del bombardeo de Hiroshima y Nagasaki.",
                 "del terremoto del 85 en México."]
        azar = random.choice(lista)
        return azar
    elif genero == 8: #ciencia ficción
        lista = ["actual.", "500 años en el futuro.", "1000 años en el futuro.", "de la cuarentena del Coronavirus.",
                 "del primer hombre en la luna."]
        azar = random.choice(lista)
        return azar
    
def hacerPaleta(genero,canvas):
    for x in range(50,501,100):
        y = 200
        puntoArriba = (x,y)
        puntoAbajo = (x+100,y+100)
        
        if genero == 1: #comedia
            rojo = randint (0,255)
            verde = randint (0,255)
            azul = randint (0,255)
            canvas.rectangle(puntoArriba + puntoAbajo, (rojo, verde, azul))
        elif genero == 2 or genero == 4 or genero == 5: #drama y suspenso y misterio
            rojo = randint (0,100)
            verde = randint (0,100)
            azul = randint (0,150)
            canvas.rectangle(puntoArriba + puntoAbajo, (rojo, verde, azul))
        elif genero == 3: #terror
            rojo = randint (0,80)
            verde = randint (0,80)
            azul = randint (0,80)
            canvas.rectangle(puntoArriba + puntoAbajo, (rojo, verde, azul))
        elif genero == 6: #romántico
            rojo = randint (0,255)
            verde = randint (0,100)
            azul = randint (0,255)
            canvas.rectangle(puntoArriba + puntoAbajo, (rojo, verde, azul))
        elif genero == 7: #acción y aventura
            rojo = randint (0,150)
            verde = randint (0,150)
            azul = randint (0,150)
            canvas.rectangle(puntoArriba + puntoAbajo, (rojo, verde, azul))
        elif genero == 8: #ciencia ficción
            rojo = randint (0,50)
            verde = randint (0,150)
            azul = randint (0,150)
            canvas.rectangle(puntoArriba + puntoAbajo, (rojo, verde, azul))

def sacarPalabras():
    numeroLinea = 1
    a = open("Adjetivos.txt", encoding = "UTF-8")
    lista = a.readlines()
    print("Adjetivos:")
    for palabra in range(1,6):
        palabra = random.choice(lista)
        palabra2 = palabra.rstrip()
        print(numeroLinea,palabra2)
        numeroLinea += 1
    
    print("")
    print("Verbos: ")
    numeroLinea2 = 1
    b = open("Verbos.txt", encoding = "UTF-8")
    lista2 = b.readlines()
    for palabra in range(1,6):
        palabra = random.choice(lista2)
        palabra2 = palabra.rstrip()
        print(numeroLinea2,palabra2)
        numeroLinea2 += 1

def correrAplicacion():
    print("""¡Bienvenido!
¡Esta aplicación te ayudará a crear un concepto para tu narrativa!
 Selecciona una de las siguientes opciones para generar tu concepto,
 palabras clave y paleta de colores:\n
1. Comedia
2. Drama
3. Terror
4. Suspenso
5. Misterio
6. Romántico
7. Acción y aventura
8. Ciencia ficción
9. Salir de la aplicación""")
    print("\n¿Cuál genero quieres para tu historia?")
    opcion = int(input("Teclea el número de la opción: "))
    
    while opcion > 0:
        if opcion >= 1 and opcion <= 8:
            personaje = definirPersonaje(opcion)
            problematica = definirProblematica(opcion)
            geografia = definirGeografia(opcion)
            epoca = definirEpoca(opcion)
            
            if opcion == 1:
                print("\nTu concepto narrativo de comedia es:")
            elif opcion == 2:
                print("\nTu concepto narrativo de drama es:")
            elif opcion == 3:
                print("\nTu concepto narrativo de terror es:")
            elif opcion == 4:
                print("\nTu concepto narrativo de suspenso es:")
            elif opcion == 5:
                print("\nTu concepto narrativo de mimsterio es:")
            elif opcion == 6:
                print("\nTu concepto narrativo de romance es:")
            elif opcion == 7:
                print("\nTu concepto narrativo de acció ny aventura es:")
            elif opcion == 8:
                print("\nTu concepto narrativo de ciencia ficción es:")
            
            print(personaje,problematica,"en", geografia,"durante la época", epoca) 
            print("")
            sacarPalabras()
            img = Image.new("RGB", (600,600), "white")
            canvas = ImageDraw.Draw(img)
            hacerPaleta(opcion,canvas)
            img.show()
            
            opcion = int(input("\n¿Desea teclear de nuevo una opción?: "))
        elif opcion == 9:
            print("\nGracias por utilizar la aplicación, ¡vuelva pronto!")
            break
        elif opcion > 9:
            opcion = int(input("\nError, por favor teclea un número del 1-9: "))

def main():
    print("¡Bienvenido! Tiene dos opciones:\n1. Acerca de\n2. Iniciar aplicación\n")
    opcion1 = int(input("Indica el número de la opción que desea realizar: "))
                  
    if opcion1 == 1:
        imagen = Image.open("acercaDe.jpg")
        imagen.show()
        
    elif opcion1 == 2:
        print("")
        correrAplicacion()

main()