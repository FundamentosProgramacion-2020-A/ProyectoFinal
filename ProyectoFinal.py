#Autor: Alondra Miranda Aguilera A01746742
#Proyecto Final: Enseñando Arte Contemporáneo

from PIL import Image

def menu():
    print('''
    1. Definición de Arte según tu personalidad
    2. Expresionismo Abstracto
    3. Arte Pop
    4. Minimalismo
    5. Quizz
    0. Salir
    ''')
    m = int(input("Elige una opcción: "))
    return m


def cargarImagen(archivo):
    img = Image.open(archivo)
    return img


def arteUno():
    imagen = cargarImagen("arte.jpg")
    imagen.show()
    
    arte = int(input("¿Con cuál imágen te identificas? "))
    if arte == 1:
        return "Manifestación de la actividad humana mediante la cual se interpreta lo real o se plasma lo imaginado"
    elif arte == 3:
        return "Todo lo que te haga sentir algo es arte"
    elif arte == 2:
        return "Arte es la aplicación de la habilidad y del gusto a la producción de una obra, según principios estéticos"
    else:
        return "Numero inválido"
    

def expresionismoAbstracto():
    imagen = cargarImagen("exp.jpg")
    imagen.show()
    
    imagen = cargarImagen("exp2.jpg")
    imagen.show()
    
    imagen = cargarImagen("exp3.jpg")
    imagen.show()
    
    print('''

    EXPRESIONISMO ABSTRACTO
    
    Fue un movimiento estadounidence originado en New York en la época de postguerra.
    Alfed Barr le dio nombre a este movimiento.
    
    Expresionismo ----> Expresar
    Abstracto --------> Sin forma específica pero con significado
    
    CARACTERÍSTICAS:
    - No hay gusto por la geometría
    - Individualidad, es decir, cada artista tiene su manera de pintar
    - Emociones como el odio, coraje, tristeza, etc.
    - Se pintan emociones, no objetos
    - No se usan pinces, sino otros materiales como palos, clavos, agujas, etc.
    - Lienzos enormes
    - Los accidentes son parte de la pintura, no hay errores.
    ''')
    
def artePop():
    imagen = cargarImagen("popart.jpg")
    imagen.show()
    
    imagen = cargarImagen("popart2.jpg")
    imagen.show()
    
    imagen = cargarImagen("popart3.jpg")
    imagen.show()
    
    print('''
    ARTE POP
    
    Este movimiento esde origen británico y estadounidence.
    Se originó a principio de la década de los 50's y prrincipos de 60's.
    Las obras de los artistas pop estaban caracterizados por representar
    todos los aspectos de la cultura popular.
    
    CARACTERÍSTICAS:
    - Refleja el consumismo, publicidad, etc.
    - Lleva elementos populares y los convierte en arte
    - Pretende hacer la vida cotdiana Arte
    - Muestra qué somos, qué consumimos, qué vemos... como cultura de masa
    - No busca significado profundo
    ''')
    
def minimalismo():
    imagen = cargarImagen("minimal.jpg")
    imagen.show()
    
    imagen = cargarImagen("minimal2.jpg")
    imagen.show()
    
    imagen = cargarImagen("minimal3.jpg")
    imagen.show()
    
    print('''
    MINIMALISMO
    
    El término -minimal- fue utilizado por primera vez en 1965 por el filósofo Richard
    Wolheim.
    
    El minimalismo desribe la evolución de las diversas formas de arte y diseño donde
    cualquer cosa u objeto es reducido a lo esencial y quedando solo sus características
    elementales.
    
    CARACTERÍSTICAS:
    - Abstracción: las obras operan solo en términos de color, superficie y formato
    - Producción y estandarización industriales
    - Orden
    - Geometría elemental rectilínea
    - Máxima sencillez
    - Reducción y síntesis
    ''')
    
def quizz():
    
    puntos = [0,10]
    puntaje = 0
    
    imagen = cargarImagen("quizz.jpg")
    imagen.show()
    r1 = int(input("¿Cuántas de esas obras pertenecen al minimalismo? 1, 2 o 3: "))
    if r1 == 1:
        puntaje = puntaje + puntos[1]
    else:
        if r1 == 2:
            puntaje = puntaje + puntos[0]
        else:
            if r1 == 3:
                puntaje = puntaje + puntos[0]
                        
    
    imagen = cargarImagen("quizz2.jpg")
    imagen.show()
    r1 = int(input("¿Cuántas de esas obras pertenecen al popart? 1, 2 o 3: "))
    if r1 == 1:
        puntaje = puntaje + puntos[0]
    else:
        if r1 == 2:
            puntaje = puntaje + puntos[2]
        else:
            if r1 == 3:
                puntaje = puntaje + puntos[0]
                        
    
    imagen = cargarImagen("quizz3.jpg")
    imagen.show()
    r1 = int(input("¿Cuántas de esas obras pertenecen al expresionismo abstracto? 1, 2 o 3: "))
    if r1 == 1:
        puntaje = puntaje + puntos[0]
    else:
        if r1 == 2:
            puntaje = puntaje + puntos[0]
        else:
            if r1 == 3:
                puntaje = puntaje + puntos[1]
                        
    print("Tuviste", puntaje, "de 30 puntos")
    
#------------------------------------------------------------------------------------------

def main():
    
    m = menu()
    
    
    while m != 0:
        
        if m == 1: #Definición de Arte
            definicion = arteUno()
            print(definicion)
            
        elif m == 2: #Expresionismo
            expresionismoAbstracto()
            
        elif m == 3:
            artePop()
            
        elif m == 4:
            minimalismo()
            
        elif m == 5:
            quizz()
            
        else:
            print("Ese número no es válido, ponga otro")
            
        m = menu()
            
main()