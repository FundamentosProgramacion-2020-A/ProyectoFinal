# Mariana Mejía Béjar, A01374862
# Proyecto final


from PIL import Image, ImageOps
from random import randint


# Define el menú que le muestra al usuario las opciones a elegir de aquelo que puede realizar el programa
def menu():
    print("Bienvenido! Seleccione lo que quiere hacer: ")
    print("1. Iniciar la aplicación")
    print("2. Tips para grabar en la CDMX")
    print("3. Obtener info")
    print("4. Encuentra un lugar random")
    print("0. Salir de la aplicación")
    opcion = int(input("¿Qué desea hacer?: "))
    print(" ") 
    return opcion


def obtenerInfo(): #Función que le muestra al usuario mi información y la del programa.
    print(" ")
    print("Mi nombre es Mariana Mejía Béjar, tengo 21 años y estudio Comunicación y Medios Digitales.")
    print(" ")
    print("Esta aplicación pretender dar ideas para locaciones de filmación en la CDMX.")
    print(" ")
    

def obtenerTips(): #Función que habla acerca de las recomendaciones para grabar en la CDMX.
    print(" ")
    print("¡Grabar en CDMX es una gran idea!")
    print("Esta ciudad cuenta con una amplia variedad de locaciones de todo tipo.")
    print("Es una ciudad capaz de combinar el bullicio de la ciudad con la tranquilidad de la naturaleza.")
    print(" ")
    print("¡Grabar en la CDMX es una gran forma de promover el turismo en ella y de impulsar")
    print("su economía! Así que, si estás considerando en grabar en esta ciudad, aquí hay unos")
    print("tips para que tengas la mejor experiencia posible:")
    print(" ")
    print("1.- Obtener permisos: Si bien es cierto que no todos los lugares de la CDMX requieren de un")
    print("permiso para que te permitan grabar ahí, muchas locaciones sí los exigen. Así que siempre ponte")
    print("en contacto con los encargados del lugar para resolver todas estas cuestiones antes de que vayas")
    print("a grabar. Te ahorrará mucho tiempo, problemas e incluso encuentros con la ley.")
    print(" ")
    print("2.- ¡Ten cuidado con el tráfico!: La CDMX es un lugar mágico y magnético... y todos lo sabemos,")
    print("es por eso que al parecer todos siempre quieren estar en sus calles causando mucho tráfico.")
    print("De hecho, la CDMX está en el Top 5 de las ciudades con más tráfico del mundo, de acuerdo con")
    print("la investigación del año pasado de la empresa INRIX Research.")
    print("Es por eso que la recomendación es que midas muy bien tus tiempos y siempre contemples")
    print("el tráfico pesado de esta ciudad.")
    print(" ")
    print("3.- Siempre checa el clima: El clima en la Ciudad de México se ha vuelto muy impredecible e incierto.")
    print("De acuerdo con el sitio 'Hello DF' en la mayor parte del territorio de la ciudad (87%) se encuentra un")
    print("clima templado subhúmedo, en el siguiente 7% hay un clima seco y semiseco y en el 6% restante se presenta")
    print("un clima templado húmedo.")
    print("La temperatura media anual es 16ºC. En el mes de marzo se presenta la mayor temperatura: 25ªC")
    print("y en el mes de enero se presenta la temperatura más baja: 5ªC.")
    print("Lo ideal es constantemente checar el clima para que este no se interponga en tu grabación.")
    print(" ")
    print(" ")
   

#Función que le mostrará al usuario una imagen aleatoria, a partir de una lista con las puntuaciones posibles, mismas que son las que permiten que se abran las imágenes 
def generarAleatoria(): 
    opciones = 0
    lugares = [1130, 1010, 1090, 2090, 2050, 3010, 3050, 3090, 3130, 4130, 4010, 2050, 3050, 3090, 3130, 4130,
                4010, 4050, 4090, 5130, 5050, 5010, 5090, 6130, 6010, 6050, 6090, 7130, 7050, 7010, 7090, 10090,
                10050, 30130, 30050, 30010, 30090, 50130, 50090, 50010, 50050, 60130, 60050, 60010, 60090, 70130,
                70050, 70010, 70090, 20010, 20090, 20050, 20010, 40130, 40050, 40010, 40090, 2130]
    
    opciones = randint(0,53) #Define el rango
    randomTotal = lugares[opciones]
    contarTotal(randomTotal)


# Función que le muestra al usuario las áreas disponibles a la vez que encadena a la función de interior/exterior. De acuerdo a la elección del usuario comienza a guardar su puntuación.
def elegirArea(): 
    
    contarArea = 0
    contarInterior = 0
    contarExterior = 0
    area = 0
    ie = 0

    while area < 1 or area > 4: #Si area es 1, 2, 3, 4, entonces se sale del while. Si es cualqiier otro # se volverá a mostrar el menú nuevamente.
        print(" ")
        print("Elige una de las siguientes áreas:")
        print("1. Norte CDMX")
        print("2. Sur CDMX")
        print("3. Oriente CDMX")
        print("4. Poniente CDMX")
        print(" ")
    
        area = int(input("¿En qué área le gustaría filmar?: "))
        if area == 1:
            contarArea = 0 + 10
        if area == 2:
            contarArea = 0 + 50
        elif area == 3:
            contarArea = 0 + 90
        elif area == 4:
            contarArea = 0 + 130
    
    while ie < 1 or ie > 2: #Si ie es 1 ó 2 entonces se sale del while
        ie = eligirInteriorExterior() #Si es cualquier otro número se quedará en esta función hasta que se teclee uno correcto.

        if ie == 1:
            contarInterior = interior()
            
        elif ie == 2:
            contarExterior = exterior()
            
        else:
            print(" ")
            print("Favor de teclear un número válido")
            print(" ")
        

    total = contarArea + contarInterior + contarExterior

    contarTotal(total)
    
    
def interior(): #Función que le muestra al usuario las opciones de interiores. De acuerdo a la elección del usuario comienza a guardar su puntuación.
    
    contarInterior = 0
    tipoIn = 0

    while tipoIn < 1 or tipoIn > 7:  #Si tipoIn es 1, 2, 3, 4, 5, 6, 7 entonces se sale del while. Si es cualquier otro # se volverá a mostrar el menú nuevamente.
        print(" ")
        print("Opciones de Interior: ")
        print("1. cabaña") 
        print("2. restaurante")
        print("3. hotel") 
        print("4. plaza comercial")
        print("5. museo") 
        print("6. biblioteca") 
        print("7. teatro")
        print(" ")
    
        tipoIn = int(input("Teclee su elección: "))
        print(" ")
        
        if tipoIn == 1:
            contarInterior = 0 + 10000
        elif tipoIn == 2:
            contarInterior = 0 + 20000
        elif tipoIn == 3:
            contarInterior = 0 + 30000
        elif tipoIn == 4:
            contarInterior = 0 + 40000
        elif tipoIn == 5:
            contarInterior = 0 + 50000
        elif tipoIn == 6:
            contarInterior = 0 + 60000
        elif tipoIn == 7:
            contarInterior = 0 + 70000
        else:
            print("Favor de teclear un número válido")
        
    return contarInterior
     
     
def exterior(): #Función que le muestra al usuario las opciones de exteriores. De acuerdo a la elección del usuario comienza a guardar su puntuación.
    
    contarExterior = 0
    tipoEx = 0
    
    while tipoEx < 1 or tipoEx > 7: #Si tipoEx es 1, 2, 3, 4, 5, 6, 7 entonces se sale del while. Si es cualquier otro # se volverá a mostrar el menú nuevamente.
        print(" ")
        print("Opciones de Exterior: ")
        print(" ")
        print("1. bosque")
        print("2. parque de diversiones/temático") 
        print("3. plaza cívica")
        print("4. parques")
        print("5. rancho")
        print("6. panteón")
        print("7. mercado")
        print(" ")
        tipoEx = int(input("Teclee su elección: "))
        print(" ")
        if tipoEx == 1:
            contarExterior = 0 + 1000 
        elif tipoEx == 2:
            contarExterior = 0 + 2000
        elif tipoEx == 3:
            contarExterior = 0 + 3000
        elif tipoEx == 4:
            contarExterior = 0 + 4000
        elif tipoEx == 5:
            contarExterior = 0 + 5000
        elif tipoEx == 6:
            contarExterior = 0 + 6000
        elif tipoEx == 7:
            contarExterior = 0 + 7000
        else:
            print("Favor de teclear número válido")
    
    return contarExterior
    
    
def eligirInteriorExterior(): #Función que le muestra al usuario las opciones de exteriores e interiores.
    print("1. Interior")
    print("2. Exterior")
    print(" ")
    ie = int(input("¿Quiere un interior o exterior?: "))
    
    return ie


#Función que hace una sumatoria de todos los puntajes y dependiendo del total, le regresa al usuario la imagen correspondiente.
def contarTotal(total):
    
    respuesta = ""
    disponible = True # Si hay una imagen disponible entonces es True
    
    imagenes = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png",
                "11.png", "12.png", "13.png", "14.png", "15.png", "16.png", "17.png", "18.png", "19.png", "20.png",
                "21.png", "22.png", "23.png", "24.png", "25.png", "26.png", "27.png", "28.png", "29.png", "30.png",
                "31.png", "32.png", "33.png", "34.png", "35.png", "36.png", "37.png", "38.png", "39.png", "40.png",
                "41.png", "42.png", "43.png", "44.png", "45.png", "46.png", "47.png", "48.png", "49.png", "50.png",
                "51.png", "52.png", "53.png"]
    
    if total == 1130:
        respuesta = imagenes[0]
        
    elif total == 1010:
        respuesta = imagenes[1]
    
    elif total == 1090:
        respuesta = imagenes[2]
    
    elif total == 1050:
        respuesta = imagenes[3]
    
    elif total == 2090:
        respuesta = imagenes[4]
    
    elif total == 2050:
        respuesta = imagenes[5]
    
    elif total == 3010:
        respuesta = imagenes[6]
    
    elif total == 3050:
        respuesta = imagenes[7]
    
    elif total == 3090:
        respuesta = imagenes[8]
    
    elif total == 3130:
        respuesta = imagenes[9]
        
    elif total == 4130:
        respuesta = imagenes[10]
    
    elif total == 4010:
        respuesta = imagenes[11]
    
    elif total == 2050:
        respuesta = imagenes[6]
    
    elif total == 3050:
        respuesta = imagenes[7]
    
    elif total == 3090:
        respuesta = imagenes[8]
    
    elif total == 3130:
        respuesta = imagenes[9]
        
    elif total == 4130:
        respuesta = imagenes[10]
    
    elif total == 4010:
        respuesta = imagenes[11]
    
    elif total == 4050:
        respuesta = imagenes[12]
    
    elif total == 4090:
        respuesta = imagenes[13]
    
    elif total == 5130:
        respuesta = imagenes[14]
    
    elif total == 5050:
        respuesta = imagenes[15]
        
    elif total == 5010:
        respuesta = imagenes[16]
        
    elif total == 5090:
        respuesta = imagenes[17]
        
    elif total == 6130:
        respuesta = imagenes[18]
        
    elif total == 6010:
        respuesta = imagenes[19]
        
    elif total == 6050:
        respuesta = imagenes[20]
        
    elif total == 6090:
        respuesta = imagenes[21]
        
    elif total == 7130:
        respuesta = imagenes[22]
        
    elif total == 7050:
        respuesta = imagenes[23]
        
    elif total == 7010:
        respuesta = imagenes[24]
        
    elif total == 7090:
        respuesta = imagenes[25]
        
    elif total == 10090:
        respuesta = imagenes[26]
        
    elif total == 10050:
        respuesta = imagenes[27]
        
    elif total == 30130:
        respuesta = imagenes[28]
        
    elif total == 30050:
        respuesta = imagenes[29]
        
    elif total == 30010:
        respuesta = imagenes[30]
        
    elif total == 30090:
        respuesta = imagenes[31]
        
    elif total == 50130:
        respuesta = imagenes[32]
        
    elif total == 50090:
        respuesta = imagenes[33]

    elif total == 50010:
        respuesta = imagenes[34]
        
    elif total == 50050:
        respuesta = imagenes[35]
        
    elif total == 60130:
        respuesta = imagenes[36]
        
    elif total == 60050:
        respuesta = imagenes[37]
        
    elif total == 60010:
        respuesta = imagenes[38]
        
    elif total == 60090:
        respuesta = imagenes[39]
        
    elif total == 70130:
        respuesta = imagenes[40]
        
    elif total == 70050:
        respuesta = imagenes[41]
        
    elif total == 70010:
        respuesta = imagenes[42]
        
    elif total == 70090:
        respuesta = imagenes[43]
        
    elif total == 20130:
        respuesta = imagenes[44]
        
    elif total == 20090:
        respuesta = imagenes[45]
        
    elif total == 20050:
        respuesta = imagenes[46]
        
    elif total == 20010:
        respuesta = imagenes[47]
        
    elif total == 40130:
        respuesta = imagenes[48]
        
    elif total == 40050:
        respuesta = imagenes[49]
        
    elif total == 40010:
        respuesta = imagenes[50]
        
    elif total == 40090:
        respuesta = imagenes[51]
        
    elif total == 2130:
        respuesta = imagenes[52]
        
    else:
       print("No se encontraron resultados para esa área")
       print(" ")
       disponible = False #No hay imágenes disponibles

    if disponible:
        img = Image.open(respuesta)
        img.show()
        

def main(): # Define la función principal
    opcion = 10
    
    while opcion !=0 :
        opcion = menu()
        if opcion == 1:
            elegirArea()
            
        elif opcion == 2:
            obtenerTips()
            
        elif opcion == 3:
            obtenerInfo()
        
        elif opcion == 4:
            generarAleatoria()
            
        else:
            print(" ")
            print("Favor de teclear un número válido")
            print(" ")
        
    print(" ")
    print("¡Gracias por hacer uso de esta aplicación! Esperamos haberle ayudado")
    print(" ")
    

main()
