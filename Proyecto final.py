# Mariana Ponce Gonzàlez
# Proyecto final
# Se revisò el viernes 5 en una asesoria especial 

from PIL import Image

def imprimirNombre():
    print("Mariana Ponce Gonzàlez")
    print("Carrera LAD")
    print("\n")
    
def menu1():
    print('''¿Què deseas hacer?
         1. Ver tu informaciòn
         2. Iniciar la apliaciòn
         0. Salir
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def menu():
    #Opciones
    print('''
         Aplicaciòn (Considera tu nivel): ¿Què proyecto
         quieres hacer?
         1. Una animaciòn en 2D
         2. Editar un audio
         3. Modelar en 3D
         4. Dibujar y editar fotos
         5. Tengo dudas de mi semestre y los temas 
         0. Cambie de opiniòn, quiero salirme 
         ¿Què deseas hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def menu2D():
    #Opciones
    print('''
         Opciòn 1. Si desesas hacer una animaciòn 2D
         te recomiendo Photoshop ¿De què tienes dudas?
         1. ¿Cómo empiezo?
         2. ¿Cómo usar la lìnea de tiempo?
         3. ¿Cómo usar el papel cebolla?
         4. ¿Cómo guardar la animaciòn?
         0. Estoy satisfecho
         ¿Què deseas hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def imagen2D1(archivo):
    img = Image.open(archivo)
    return img

def menuaudio():
    #Opciones
    print('''
         Opciòn 2. Si desesas editar un audio te recomiendo 
         Audition ¿De què tienes dudas?
         1. ¿Cómo puedo jugar con la fuerza con la que suena en audio?
         2. ¿Cómo acomodo un video para editar el audio ?
         3. ¿Cómo guardo mis resultados?
         0. Estoy satisfecho, regresame al menù principal
         ¿Què deseas hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def menu3D():
    #Opciones
    print('''
         Opciòn 3. Si desesas empezar a modelar en 3D
         te recomiendo Maya ¿De què tienes dudas?
         1. ¿Cuáles son las herramientas más simples para trabajar?
         2. ¿Cuáles son las herramientas más simples para modelar?
         3. ¿Cómo puedo hacer el render?
         0. Estoy satisfecho, regresame al menù principal
         ¿Què deseas hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def sem():
    valores = []
    numero = int(input("De los cuatro temas ¿Cuàntos quieres ver? (eligelos del 1 al 4 sin repetir) pon 0 si ya acabaste: "))
    while numero != 0:
        valores.append(numero)
        numero = int(input("Sigue: "))
                
    a = [1,2,3, 4]
    b = [1]
    c = [2]
    d = [3]
    e = [4]
    a1 = [1,2]
    a2 = [1,3]
    a3 = [1,4]
    b1 = [2,4]
    b2 = [2,3]
    c1 = [3,4]
    valores.sort()
    if valores==a:
        print("Si manejas todos esos temas, estaras prepadado hasta el quinto semestre")
    elif valores==b or valores==c or valores==d or valores==e:
        print("Si manejas uno de estos temas, te ayudara a pasar el primer semestre")
    elif valores==a1 or valores==a1 or valores==a3 or valores==b1 or valores==b2 or valores==c1:
        print("Si manejas todos esos temas, estaras prepadado hasta el segundo semestre")
    else:
        print("Si manejas todos esos temas, estaras prepadado hasta el tercer semestre")

def menueditdibu():
    #Opciones
    print('''
         Opciòn 4. Si desesas dibujar y editar fotos
         te recomiendo Photoshop ¿De què tienes dudas?
         1. ¿Cuáles son las herramientas bàsicas para dibujar?
         2. ¿Cuáles son las herramientas bàsicas para editar una foto?
         3. ¿Cómo guardar lo que he trabajado?
         0. Estoy satisfecho, regresame al menù principal
         ¿Què deseas hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def graficas():
    #Opciones
    print('''
         Aplicaciòn: ¿Què quieres saber
         de tu nivel?
         1. ¿Cuàl debe de ser mi nivel segùn mi semestres?
         2. Quiero saber cuales son los temas màs fàciles y cuales los mas dìficiles
         3. Tengo duda de los temas y mi semestre 
         0. Cambie de opiniòn, quiero salirme 
         ¿Què deseas hacer?
    ''')
    opcion = int(input("Teclea tu opciòn: "))
    return opcion

def main():
    
    #Datos de proyecto
    opcion = menu1()
    while opcion !=0:
        if opcion ==1:
            imprimirNombre()
            
        #Inicia la apliaciòn
        elif opcion ==2:
            opcion = menu()
            while opcion != 0:
                if opcion == 1:
                    # Una animaciòn en 2D
                    opcion = menu2D()
                    while opcion!= 0:
                        #¿Cómo empiezo?
                        if opcion == 1:
                            imagen = imagen2D1("a.jpg")
                            imagen.show()
                        elif opcion == 2:
                        #¿Cómo usar la linea de tiempo?
                            imagen = imagen2D1("b.jpg")
                            imagen.show()
                        elif opcion == 3:
                            #¿Cómo usar el papel cebolla?
                            imagen = imagen2D1("c.jpg")
                            imagen.show()
                        elif opcion == 4:
                            #¿Cómo guardar la animaciòn?
                            imagen = imagen2D1("d.jpg")
                            imagen.show()
                        opcion = menu2D()       
                    
                elif opcion == 2:
                    # Editar un audio
                    opcion = menuaudio()
                    while opcion!= 0:
                        #¿Cómo puedo jugar con la fuerza como sueña el audio?
                        if opcion == 1:
                            imagen = imagen2D1("e.jpg")
                            imagen.show()
                        elif opcion == 2:
                        #¿Cómo acomodo un video para editar el audio ?
                            imagen = imagen2D1("f.jpg")
                            imagen.show()
                        elif opcion == 3:
                            #¿Cómo guardo mis resultados?
                            imagen = imagen2D1("g.jpg")
                            imagen.show()
                        opcion = menuaudio()
                        
                elif opcion == 3:
                    #Modelar en 3D
                    opcion = menu3D()
                    while opcion!= 0:
                        #¿Cuáles son las herramientas más simples para trabajar?
                        if opcion == 1:
                            imagen = imagen2D1("h.jpg")
                            imagen.show()
                        elif opcion == 2:
                        #¿Cuáles son las herramientas más simples para modelar?
                            imagen = imagen2D1("i.jpg")
                            imagen.show()
                        elif opcion == 3:
                            #¿Cómo puedo hacer el render?
                            imagen = imagen2D1("j.jpg")
                            imagen.show()
                        opcion = menu3D()
                        
                elif opcion == 4:
                    opcion = menueditdibu()
                    while opcion!= 0:
                        #¿Cuáles son las herramientas basicas para dibujar?
                        if opcion == 1:
                            imagen = imagen2D1("k.jpg")
                            imagen.show()
                        elif opcion == 2:
                        #¿Cuáles son las herramientas basicas para dibujar?
                            imagen = imagen2D1("l.jpg")
                            imagen.show()
                        elif opcion == 3:
                        #¿Cómo guardar lo que he trabajado?
                            imagen = imagen2D1("m.jpg")
                            imagen.show()
                        opcion = menueditdibu()
                        
                elif opcion == 5:
                    opcion = graficas()
                    while opcion!= 0:
                        if opcion == 1:
                            #¿Cuàl debe de ser mi nivel segùn mi semestres?
                            # Tabla 
                            imagen = imagen2D1("tabla.jpg")
                            imagen.show()
                        elif opcion == 2:
                        #Quiero saber cuales son los temas màs fàciles y cuales los mas dìficiles
                            #Gráfica
                            imagen = imagen2D1("graf.jpg")
                            imagen.show()
                        elif opcion == 3:
                        #Tengo duda de los temas y mi semestre
                        #Lista 
                            sem()
                        opcion = graficas()
                        
        opcion = menu1()
        print("Salir")
    
main()