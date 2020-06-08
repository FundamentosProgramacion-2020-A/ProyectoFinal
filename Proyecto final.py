#Autor: Guadalupe Iveth Serrano Hernández
#Poyecto final: programa que recomienda aplicaciones para facilitar el trabajo en areas como el diseño de arte y la edicion.

from PIL import Image

def menu():                    #Menú de la página principal
    print('''Bienvenido. Te ayudaremos a encontrar una herramienta que te ayude a realizar tus tareas en el area de diseño de arte,
    edicion de video y/o edicion de imagen. A continuacion te mostramos un menu para empezar, selecciona una opcion.
    *Para iniciar directamente selecciona las opciones 2, 3 o 4.
    1. Acerca de
    2. Diseño de arte
    3. Edición de video
    4. Edición de imagen
    0. Salir''')
    opcion = int(input("Seleccione el área de interes de la plataforma que busca o acerca del desarrollador: "))
    return opcion
    
    
def mostrarInformacion():               #informacion
    print('''
            ¡Hola! mi nombre es Guadalupe Iveth Serrano Hernández soy estudiante de Comunicacion y medios digitales de cuarto semetre.
            Tengo 21 años y he decidido hacer esta aplicaciòn con el fin de orientar a personas de la carrera o que estèn
            interesados en àreas y que no sepan o tengan dudas acerca de las herramientas que pueden utilizar con el fin de que
            conozcan algunas de ellas. ¡Bienvenido!''')


def cargarImagen(archivo):
    img = Image.open(archivo)
    return img


def mostrarDisenoArte():                 #Opciòn 1 de aplicaciones
    preguntaUsuario = input('''Teclea el nùmero de la opciòn que desees
                            1. Diseñar paleta de color
                            2. Obtener elementos del set
                            ''')
    if preguntaUsuario == "1":
        imagen = cargarImagen("colorViewfinder.jpg")
        imagen.show()
        print('''
              Color viewfinder es una herramienta que te permite elegir una una imagen desde tu galeria, detecta los
              colores y actua rapidamente para convertirla en una paleta de color, ademàs es totalmente gratis.
              ''')
    elif preguntaUsuario == "2":
        img = cargarImagen("movieMagic.jpg")
        img.show()
        print('''
                Movie magic sheduling es un software profesional que usado principalmente para la organizaciòn de un rodaje,
                sin embargo tambièn es muy util para realizar un desgloce de todos los elementos que se usaràn en el diseño
                de arte a la hora del rodaje. ¿Estàs listo para usarla?''')
    else:
        print("Algo saliò mal, teclea nuevamente con los nùmeros correspondientes(1 o 2)")


def mostrarEdicionVideo():               #Opciòn 2 aplicaciones
    preguntaUsuario = input('''Teclea el npumero de la opcion que desees
                            1. Edicion de video
                            2. Correccion de color
                            ''')
    if preguntaUsuario == "1":
        pregunta = input("¿Deseas pagar por tu aplicacion? (responde con si o no sin acentos y en minùsculas): ")
        if pregunta == "si":
            imagen = cargarImagen("premiere.png")
            imagen.show()
            print('''
                   Adobe Premiere Pro es una aplicaciòn desarrollada por Adobe y publicada como parte de Adobe Creative Cloud.
                   Está orientada a la edición de vídeos profesionales y te permite realizar acciones de ensamblaje,
                   edición, color, efectos, audio y títulos.
                    ''')
        else:
            pregunta == "no"
            imagen = cargarImagen("lightworks.png")
            imagen.show()
            print('''
                    Lightworks editor de video es un sistema profesional de edición de vídeo no lineal que resulta muy útil para editar
                    y masterizar películas en diferentes formatos, con resoluciones 2K y 4K, y producciones televisivas en formatos de
                    alta definición, PAL y NTSC. La versiòn gratuita es ideal para ti como estudiante.
                    ''')
    elif preguntaUsuario == "2":
        respuesta = input("¿Deseas pagar por tu aplicacion? ")
        if respuesta == "si":
            imagen = cargarImagen("davinciResolve.png")
            imagen.show()
            print('''
                    Davinci Resolve ofrece herramientas de edición, efectos visuales, gráficos en movimiento, corrección de color y
                    post producción de audio. Resulta muy util ya que la versión gratuita del programa incluye todas las prestaciones
                    para editar y etalonar. ¡Animate a probarla!
                    ''')
        else:
            respuesta == "no"
            img = cargarImagen("afterEffects.png")
            img.show()
            ('''
                es un software de motion graphics y composición digital publicado por Adobe. Se usa principalmente para posproducción de
                imágenes en movimiento, animar, alterar y componer creaciones en espacios 2D y 3D con varias herramientas nativas y plugins
                de terceros como la correcciòn de color y etalonaje. Wow, cuàntas funciones ¿no?''')
        
def mostrarEdicionImagen():               #Opciòn 3 aplicaciones
    preguntar =input('''Teclea el npumero de la opcion que desees
                            1. Edicion de fotografìa e imagen
                            2. Generar gràficos
                            ''')
    if preguntar == "1":
        pregunta = input("¿Deseas pagar por tu aplicacion? (responde con si o no sin acentos y en minùsculas): ")
        if pregunta == "si":
            imagen = cargarImagen("photoshop.jpg")
            imagen.show()
            print('''
                   Photoshop es unaherramienta de edición de imágenes y fotografía, un programa que se utiliza en PC para retocar
                   fotos y hacer montajes de carácter profesional. ¿lo mejor? es accesible para usuarios que llevan poco tiempo
                   experimentando en ese terreno.
                    ''')
        else:
            pregunta == "no"
            imagen = cargarImagen("gimp.png")
            imagen.show()
            print('''
                    The GIMP es un programa referente para retocar fotos por sus características muy avanzadas. Ofrece una potente
                    capacidad de manejar capas, filtros, ajustes de color, herramientas para dibujo o pintura, etc. Ademàs es posiblemente
                    la mejor alternativa gratis, la más potente y profesional a Photoshop, ¿te animas a usarla?
                    ''')
    elif preguntaUsuario == "2":
        pregunta = input("¿Deseas pagar por tu aplicacion? (responde con si o no sin acentos y en minùsculas): ")
        if pregunta == "si":
            imagen = cargarImagen("illustrator.png")
            imagen.show()
            print('''
                    Adobe Illustrator es un editor de gráficos vectoriales en forma de taller de arte está destinado a la creación
                    artística de dibujo y pintura para ilustración, para crear y diseñar imágenes. 
                    ''')
        else:
            pregunta == "no"
            imagen = cargarImagen("mediBangPaint.png")
            imagen.show()
            print('''
                    Medibang Paint es una programa para dibujar y pintar que está centrado en el cómic y la ilustración. También podremos
                    encontrarnos con una inmensa cantidad de tutoriales para aprender a dominar esta aplicación asì como su función
                    colaborativa para que puedas trabajar junto con otras personas. ¡Suena interesante!
                    ''')
      
      
def main():
    
    opcion = menu()         #menú va imprimir las opciones
    while opcion != 0:
        if opcion == 1:
            mostrarInformacion()
        elif opcion == 2:
            mostrarDisenoArte()
        elif opcion == 3:
            mostrarEdicionVideo()
        elif opcion == 4:
            mostrarEdicionImagen()
        else:
            print("Opción incorrecta, debes teclear [1, 2, 3 o 4 y 0 para salir]")
        
        opcion = menu()
        
    print("Gracias por tu visita, esperamos haberte ayudado.")
    
    
main()