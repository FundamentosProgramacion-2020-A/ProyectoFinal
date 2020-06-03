# Autor: Patricio León
# Proyecto final

from PIL import Image, ImageDraw


def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen


# Puntos para el valor del semestre
def valorSemestre(semestre):
    puntosS = 0
    
    if semestre >=1 and semestre <= 3:
        puntosS = 10
    elif semestre >= 4 and semestre <= 6:
        puntosS = 20
    elif semestre >= 7 and semestre <= 10:
        puntosS = 35
    else:
        print ("Teclee un semestre válido")
        
    return puntosS


# Puntos para el valor de la experiencia
def valorExperiencia(experiencia):
    puntosE = 0
    
    if experiencia >= 1 and experiencia <= 2:
        puntosE = 5
    elif experiencia >= 3 and experiencia <= 4:
        puntosE = 10
    elif experiencia >= 5 and experiencia <= 6:
        puntosE = 20
    elif experiencia >= 7 and experiencia <= 8:
        puntosE = 30
    elif experiencia >= 9 and experiencia <= 10:
        puntosE = 40
    else:
        print ("Teclee un número del 1 al 10")
        
    return puntosE
    
 
# Puntos para el valor del uso 
def valorUso(uso):
    puntosU = 0
    
    if uso == 1 :
        puntosU = 10
    elif uso == 2:
        puntosU = 20
    elif uso == 3:
        puntosU = 30
    else:
        print ("Teclee una opción del 1 al 3")
    
    return puntosU
    

# Puntos para el valor del presupuesto
def determinarPresupuesto(presupuesto):
    puntosP = 0
    
    if presupuesto == 1 :
        puntosP = 20
    elif presupuesto == 2:
        puntosP = 30
    elif presupuesto == 3:
        puntosP = 45
    else:
        print ("Teclee una opción del 1 al 3")
        
    return puntosP
        
        
def menu():
    print("¿Cómo comprar la cámara correcta?")
    print('''
        1. Acerca de
        2. Encuentra tu cámara ideal 
        0. Salir
    ''')
    opcion = int(input("Teclea tu opción: "))
    return opcion


# Suma de los puntos para determinar imagen de la cámara que será la adiquirida
def totalPuntos(puntosS, puntosE, puntosU, puntosP):
    
    puntos = puntosS + puntosE + puntosU + puntosP
    print (puntos)
    lista = ["camara1.jpg", "camara2.jpg", "camara3.jpg"]
    
    if puntos >= 45 and puntos <= 69:
        indice = lista[0]
        #print ("Esta cámara es cool")
        #print(indice)
        imagen = Image.open(indice)
        imagen.show()
    elif puntos >= 70 and puntos <= 120:
        indice = lista[1]
        #print ("Esta cámara es cool")
        #print(indice)
        imagen = Image.open(indice)
        imagen.show()
    elif puntos >= 121 and puntos <= 150:
        indice = lista[2]
        #print ("Esta cámara es cool")
        #print(indice)
        imagen = Image.open(indice)
        imagen.show()
    else:
        print ("ERROR")
    

# Suma de los puntos para determinar las especificaciones de la cámara que será la adiquirida
def datosCam(puntosS, puntosE, puntosU, puntosP):
    
    puntos = puntosS + puntosE + puntosU + puntosP
    lista = ["""Se te recomienda la cámara Nikon D5600:
                - Tiene una pantalla táctil de 3.2 pulgadas.
                - Tiene un sensor CMOS en formato DX de 24.2 MP que ofrece fotos y videos de alta calidad
                - Sistema de enfoque automático de 39 puntos adquiere el enfoque rápidamente donde lo desea
                - Amplio rango de sensibilidad ISO 100-25,600
                - Costo alrededor de $15,399 en Amazon""",\
             
             """Se te recomienda la cámara Nikon D7500:
                - Pantalla LCD inclinable de 3.2” y 922K puntos y funcionalidad táctil, Wi-Fi y Bluetooth incorporados
                - Sistema AF de 51 puntos, con 15 sensores de tipo cruz y área de AF dinámico 
                - Videos en 4K Ultra HD y 1080p full HD con sonido estéreo, control de apertura, ISO automática
                - Lente 18-140mm, compacto con zoom todo en uno en, formato DX desde gran angular (18mm) hasta teleobjetivo (140mm) 
                - Costo alrededor de $25,999 en Amazon""",\
             
             """Se te recomienda la cámara Nikon Z6:
                - Punto perfecto entre velocidad, resolución y rendimiento en condiciones de poca luz
                - tiene 24.5 megapíxeles formato FX, 12CPS, ISO 100-51,200 expansible a 204, 800, Video 4K UHD
                - Armazón compuesto de una aleación de magnesio ultrarresistente
                - Cuenta con Wi-Fi y Bluetooth 
                - Costo alrededor de $54,899 en Amazon"""]
    
    
    if puntos >= 45 and puntos <= 69:
        indice = lista[0]
        print(indice)      
    elif puntos >= 70 and puntos <= 120:
        indice = lista[1]
        print(indice)
    elif puntos >= 121 and puntos <= 150:
        print(indice)
    else:
        print ("ERROR")

# Llamar a las funciones
def main():
 
    opcion = menu()    
    
    while opcion != 0:
        if opcion == 1:
            print("Estas preguntas te ayudarán a determinar cuál cámara es adecuada para ti")
            
        elif opcion == 2:
            
            semestre = int(input("Teclea el semestre que cursas actualemnte: "))
            experiencia = int(input("Del 1 al 10, ¿Cómo calificaría su experiencia con la fotografía?: "))
            uso = int(input("¿Cuál de los siguientes usos le darías a tu cámara? 1 Personal, 2 Escolar y 3 Prfesional: "))
            presupuesto = int(input("Dentro de estos rangos, ¿dónde entra tu presupuesto? 1: 15,000 a 20,000, 2: 25,000 a 35,000, 3: 45,000 a 55,000: "))
            
            puntosS = valorSemestre(semestre)
            puntosE = valorExperiencia(experiencia)
            puntosU = valorUso(uso)
            puntosP = determinarPresupuesto(presupuesto)
            puntosFinal = totalPuntos(puntosS, puntosE, puntosU, puntosP)
            datosCam(puntosS, puntosE, puntosU, puntosP)
        
        else:
            print("Opción incorrecta, debes teclear [1, 2, 3, 4, 5]")
        
        opcion = menu()
        
    print("Termina")


main()
