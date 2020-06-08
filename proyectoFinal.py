#Autor; Fernando Pérez, A01376508
#Proyecto final de programación: Encontrar vocación dentro de la realización de un producto audiovisual

from PIL import Image

def menu(): #imprime el menú 
    print('''
        Hola, bienvenido a esta aplicación que te ayudará a encontrar tu lugar dentro de la creación de un producto audiovisual
        como lo puede ser una película, un cortometraje, documental, entre otros.
        Las tres grandes áreas dentro de la creación son preproducción, producción o postproducción.
        Escribe el número que corresponda a tu área de interés.
        1. Preproducción: Es la fase de preparación, desde que nace la idea hasta que comienza la creación.
        2. Producción: Es lo que pone en práctica todo lo estipulado en la preproducción, es cuando realizas el producto.
        3. Postproducción: Es lo que convierte todo el producto bruto en en una obra audiovisual.
        4. Conocer todas las profesiones posibles.
        5. Acerca del desarrollador y de la aplicación
        0. Salir de la aplicación. 
        ''')
    opcion = int(input("Teclea tu opción: "))
    return opcion


def preguntarPreproduccion(): #si elegiste preproducción te arroja estas preguntas
    print("Elegiste preproducción. A continuación deberás contestar las características con si o no en minúsculas y sin acéntos")
    p1 = input("1. Puedes crear una idea y transmitirla con claridad: ")
    p2 = input("2. Cuando escribes puedes visualizar tu idea hecha realidad: ")
    p3 = input("3. Tienes presente como se podría ver algo a través de la cámara, en textura y color: ")
    p4 = input("4. Puedes visualizar espacios y perspectivas cuando lees una historia para generar una atmósfera inmersiva: ")
    p5 = input("5. Puedes identificar si un actor es bueno para un papel y su capacidad de colaboración: ")
    p6 = input("6. Cuando te imaginas a un personajes sabes que perfil más allá de lo físico debe tener: ")
    if p1 == "si" and p2 == "si":
        print('''
        Guionista
        Como su nombre lo menciona es el que hace el guión. Debe dar forma  a una trama que tenga
        sentido, para el medio que se va a publicar, al igual que conocer las limitaciones del mismo.
        ''')
        imagen = Image.open("Guionista.jpg")
        imagen.show()
    elif p3 == "si" and p4 == "si":
        print('''
        Director de arte
        Propone las características sobre la estética que se verá en el producto audiovisual. Peinado,
        vestuario, paleta de colores que se va a usar, utilería y escenografía que se quiere lograr para
        una muy buena credibilidad. 
        ''')
        imagen = Image.open("DirectorDeArte.jpg")
        imagen.show()
    elif p5 == "si" and p6 == "si":
        print('''
        Director de casting
        Es la persona que debe tener conocimientos actorales profundos, debe encontrar en las personas un
        perfil profundo, que no solo sea físico, sino también emocional. Busca personas que transmitan en
        persona, a la cámara y a la historia las emociones que se busca dar a conocer. 
        ''')
        imagen = Image.open("DirectorDeCasting.jpg")
        imagen.show()
    else:
        print("Puede que tu vocación no esté en esta área o no escribiste correctamente las opciones.")
    
    
def preguntarProduccion(): #si elegista producción te arroja estas preguntas
    print("Elegiste producción. A continuación deberás contestar las características con si o no, en minúsculas y sin acéntos")
    p1 = input("1. Eres una persona muy organizada que sabe pedir cosas: ")
    p2 = input("2. Puedes elaborar cuestiones administrativas al igual que el plan para realizar el producto final: ")
    p3 = input("3. Podrías detectar errores una escena con haber leído el guión: ")
    p4 = input("4. Puedes visualizar espacios y perspectivas cuando lees una historia para generar una atmósfera inmersiva: ")
    p5 = input("5. Puedes construir una atmósfera a través de sonidos: ")
    p6 = input("6. Puedes crear sonidos a partir de un concepto: ")
    p7 = input("7. Puedes identificar características de un personaje con solo verlo: ")
    p8 = input("8. Puedes crear a un personaje con base en su vestimenta y maquillaje: ")
    if p1 == "si" and p2 == "si": #cada profesión arroja una descripción y una imagen con el nombre de la misma 
        print('''
        Asistente de dirección
        Se encarga del desarrollo de la película, hacer los horarios y calendarios de las escenas que se
        van a grabar. Debe hacerle saber a todos los departamentos si existe algún cambio. Realiza el
        desglose del guión y comunica que se necesita para realizar las escenas en tiempo y forma. 
        ''')
        imagen = Image.open("AsistenteDeDireccion.jpg")
        imagen.show()
    elif p3 == "si" and p4 == "si":
        print('''
        Continuidad
        Supervisa que se debe llevar un orden lógico en lo que se está grabando, debe saber la duración de
        las escenas. Debe ver la coherencia de todos los departamentos, que luces se usaron, qué maquillaje,
        peinado, que utileria está en escena. Todas las acciones de los personajes. Si se llega a repetir
        una escena esta persona es la indicada para realizarla.
        ''')
        imagen = Image.open("Continuidad.jpg")
        imagen.show()
    elif p5 == "si"and p6 == "si":
        print('''
        Diseñador sonoro
        Durante la grabación se encarga de capturar el sonido lo más real que se pueda para generar la atmósfera
        que se quiera transmitir. Esto incluye sonido de ambiente, diálogos y los foleys. Crea el mundo sonoro de
        la película, en aspectos técnicos y artísticos. 
        ''')
        imagen = Image.open("DiseñadorSonoro.jpg")
        imagen.show()
    elif p7 == "si" and p8 == "si":
        print('''
        Maquillaje y vestuario
        Es el que comunica a través de los actores involucrados. Da a conocer la época, características
        relevantes para la construcción de un personaje y cómo se va a desarrollar dentro de la obra.
        Da credibilidad y fortaleza a la atmósfera de la historia. 
        ''')
        imagen = Image.open("MaquillajeVestuario.jpg")
        imagen.show()
    else:
        print("Puede que tu vocación no esté en esta área o no escribiste correctamente las opciones.")
    
    
def preguntarPostproduccion(): #si elegista postproducción te arroja estas preguntas
    print("Elegiste postproducción. A continuación deberás contestar las características con si o no en minúsculas y sin acéntos")
    p1 = input("1. Sabes cómo armar una historia al ver los elementos separados: ")
    p2 = input("2. Puedes identificar que tipo de escenas pueden mejorar la narrativa de la historia: ")
    p3 = input("3. Tienes presente como se podría ver algo a través de la cámara, en textura y color: ")
    p4 = input("4. Puedes interpretar situaciones a través de tonalidades: ")
    if p1 == "si" and p2 == "si":
        print('''
        Editor de video
        Aquel que se encarga de montar la película para que tenga coherencia y funcione la narrativa.
        Se dice que a veces en el proceso de edición se reescribe la película, porque se puede encontrar
        una diferente lógica. Esta persona sabe que es lo que funciona narrativamente para comunicar un mensaje. 
        ''')
        imagen = Image.open("Editor.jpg")
        imagen.show()
    elif p3 == "si" and p4 == "si":
        print('''
        Colorista
        Artista encargado de llevar a cabo la corrección de color. Hila y perfecciona la continuidad de
        los elementos representados en la película mediante tonalidades. Al igual que mantiene la armonía
        visual en color y luz.
        ''')
        imagen = Image.open("Colorista.jpg")
        imagen.show()
    else:
        print("Puede que tu vocación no esté en esta área o no escribiste correctamente las opciones.")


def mostrarProfesiones(): #en esta función ves todas las profesiones en una lista y elijes de la que quieras conocer más
    lista = ["1. Guionista", "2. Director de arte", "3. Director de casting", "4. Asistente de dirección", "5. Continuidad", "6. Diseñador sonoro", "7. Maquillaje y vestuario", "8. Editor de video", "9. Colorista"]
    for dato in lista:
        print(dato)
    profesion = int(input("Escribe el número de la profesión que te atrae: "))
    if profesion == 1:
        print('''
        Como su nombre lo menciona es el que hace el guión. Debe dar forma  a una trama que tenga
        sentido, para el medio que se va a publicar, al igual que conocer las limitaciones del mismo.
        ''')
    elif profesion == 2:
        print('''
        Propone las características sobre la estética que se verá en el producto audiovisual. Peinado,
        vestuario, paleta de colores que se va a usar, utilería y escenografía que se quiere lograr para
        una muy buena credibilidad. 
        ''')
    elif profesion == 3:
        print('''
        Es la persona que debe tener conocimientos actorales profundos, debe encontrar en las personas un
        perfil profundo, que no solo sea físico, sino también emocional. Busca personas que transmitan en
        persona, a la cámara y a la historia las emociones que se busca dar a conocer. 
        ''')
    elif profesion == 4:
        print('''
        Se encarga del desarrollo de la película, hacer los horarios y calendarios de las escenas que se
        van a grabar. Debe hacerle saber a todos los departamentos si existe algún cambio. Realiza el
        desglose del guión y comunica que se necesita para realizar las escenas en tiempo y forma. 
        ''')        
    elif profesion == 5:
        print('''
        Supervisa que se debe llevar un orden lógico en lo que se está grabando, debe saber la duración de
        las escenas. Debe ver la coherencia de todos los departamentos, que luces se usaron, qué maquillaje,
        peinado, que utileria está en escena. Todas las acciones de los personajes. Si se llega a repetir
        una escena esta persona es la indicada para realizarla.
        ''')
    elif profesion == 6:
        print('''
        Durante la grabación se encarga de capturar el sonido lo más real que se pueda para generar la atmósfera
        que se quiera transmitir. Esto incluye sonido de ambiente, diálogos y los foleys. Crea el mundo sonoro de
        la película, en aspectos técnicos y artísticos. 
        ''')
    elif profesion == 7:
        print('''
        Es el que comunica a través de los actores involucrados. Da a conocer la época, características
        relevantes para la construcción de un personaje y cómo se va a desarrollar dentro de la obra.
        Da credibilidad y fortaleza a la atmósfera de la historia. 
        ''')
    elif profesion == 8:
        print('''
        Aquel que se encarga de montar la película para que tenga coherencia y funcione la narrativa.
        Se dice que a veces en el proceso de edición se reescribe la película, porque se puede encontrar
        una diferente lógica. Esta persona sabe que es lo que funciona narrativamente para comunicar un mensaje. 
        ''')
    elif profesion == 9:
        print('''
        Artista encargado de llevar a cabo la corrección de color. Hila y perfecciona la continuidad de
        los elementos representados en la película mediante tonalidades. Al igual que mantiene la armonía
        visual en color y luz.
        ''')
        
        
def main():
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            preguntarPreproduccion()
        elif opcion == 2:
            preguntarProduccion()
        elif opcion == 3:
            preguntarPostproduccion()
        elif opcion == 4:
            mostrarProfesiones()
        elif opcion == 5:
            print('''
            Me llamo Fernando Pérez, tengo 20 años y estudio comunicación.
            Realicé esta app con intención de ayudar a encontrar una vocación, a la
            gente que quiera participar en la realización de un producto audiovisual.
            ''')
        else:
            print("Opción incorrecta, debes teclear [1,2,3,4,5,0]") #si el usuario escoge otro número te arroja los que si puedes usar
        
        opcion = menu()
    
    print("Gracias por usar esta aplicación:)") #fin de mi aplicación
        
main()

    