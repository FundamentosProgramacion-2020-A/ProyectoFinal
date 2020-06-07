#Autor José Manuel Rivera Sosapavón
#Proyecto Final

from PIL import Image


def menu():
    print ("1. ¿Qué area de comunicación es la ideal para ti?")
    print ("2.Acerca de")
    print ("0.Salir")
    menu = int(input("Teclea tu opción: "))
    
    return menu

def preguntarPrimero():
    print ("Pregunta 01 ------------") 
    print ("Dentro de una producción que es lo que más te gusta hacer")
    print ("1. Producción")
    print ("2. Actuación")
    print ("3. Guion o carpeta de preproducción")
    print ("4. Audio o Iluminación o Montaje")
    print ("5. Dirección")
    print ("6. Edición")
    print ("7. Fotografía")
    r1 = int(input("Teclea el numero de tu respuesta: "))
    
    return r1

def preguntarSegundo(archivo):
    print("Pregunta 02 -------------")
    imagen = Image.open(archivo)
    return imagen
 
def preguntarTercero():
    print ("Pregunta 03 -------------")
    print ("Del 1 al 10 que tan capaz te sientes de ser un lider")
    
    for i in range (1,11,):
        if  i ==  1:
            print("%d. Soy un seguidor." % (i))
        elif i == 2:
            print (" %d. Soy seguidor, pero me interesa el proceso creativo."% (i))
        elif i == 3:
            print ("%d. Soy creativo pero no externo mis ideas con los demas."% (i))
        elif i == 4:
            print ("%d. Soy parte del proceso creativo del proyecto, pero no participo mucho."% (i))
        elif i == 5: 
            print ("%d. Puedo ayudar en tomar algunas decisiones." % (i))
        elif i == 6:
            print ("%d. Ayudo en la toma de decisiones pero solo me enfoco en mi trabajo."% (i))
        elif i == 7:
            print ("%d. Soy parte de la toma de decisiones y busco ayudar a los que estan directamente debajo de mi."% (i))
        elif i == 8:
            print ("%d. Soy parte de las cabezas del trabajo pero necesito ayuda de alguien arriba de mi."% (i))
        elif i == 9:
            print ("%d. Soy uno de los lideres del proyecto pero necesito a alguien que me ayude a tomar las deciciones importantes." % (i))
        elif i == 10:
            print ("%d. Soy un buen lider, tomo las decisones que sean mejor para mi equipo y los ayudo a hacerlos crecer." % (i))   
            r3 = int(input("Teclea el numero de tu respuesta: "))
    
    return r3

def preguntarCuarto(archivo):
     print ("Pregunta 04 -------------")
     print ("¿Cual de estos colores es tu favorito?")
     imagen = Image.open(archivo)
     return imagen
    
def preguntarQuinto():
    print ("Pregunta 05 -------------")
    print ("¿Que tipo de cine es el que más te gusta?")
    lista = ["1. Acción", "2. Comedia","3. Cine de arte", "4. Extranjero", "5. Drama",
             "6. Scifi", "7. Animación","8. Musical","9. Historias Reales", "10. Romantico"]
    print(lista)
    ans = int(input("Teclea el numero de tu respuesta: "))
    return ans

def preguntarSexto():
    print ("Pregunta 06 -------------")
    print ("¿De los siguientes, cual es tu director preferido?")
    for linea in open("preguntaseis.txt", encoding="UTF-8"):
        cadena = linea.rstrip()
        if linea.startswith ("#") ==True:
            lista = linea.split()
            lista = linea.rstrip()
            print(lista)
        
    r6 = int(input("Teclea el numero de tu respuesta: "))
    return r6
             
def serDirector(archivo):
    imagen = Image.open(archivo)
    return imagen

def main():
    rmenu = menu()
    while rmenu !=0:
         if rmenu  == 1:
            pr1 = preguntarPrimero ()
            while pr1 !=0:
                if pr1 <=7:
                    imagen = preguntarSegundo("pregunta 2.png")
                    imagen.show()
                    pr2 = int(input("Con base a la imagen, tecle su respuesta: "))
                    
                    while pr2 !=0:
                        if pr2 <=4:
                            pr3 = preguntarTercero()
                            
                            while pr3 !=0:
                                    if pr3 <=10:
                                        imagen = preguntarCuarto("pregunta4.png")
                                        imagen.show()
                                        pr4 = int(input("Con base a la imagen, tecle su respuesta: "))
                                        while pr4 !=0:
                                            if pr4 <=5:
                                                pr5 = preguntarQuinto()
                                                while pr5 !=0:
                                                    if pr5 <=10:
                                                        pr6 = preguntarSexto()
                                                        while pr6 !=0:
                                                            if pr6 <=10:
                                                                suma = pr1+pr2+pr3+pr4+pr5+pr6
                                                                print ("TENEMOS TU RESULTADO, TÚ...")
                                                                if suma >= 6 and suma <= 13:
                                                                    print ("ERES DIRECTOR: Eres un lider y estas centrado en hacer una obra maestra.")
                                                                elif suma > 13 and suma <= 20:
                                                                    print ("ERES PRODUCTOR: Creas y buscas conseguir lo que quieres sin importar que. ")
                                                                elif suma > 20 and suma <= 27:
                                                                    print ("Eres DIRECTOR DE FOTOGRAFÍA: Tienes un ojo unico y eres un ser lleno de ideas")
                                                                elif suma > 27 and suma <= 34:
                                                                    print ("Eres DIRECTOR DE EDICIÓN: Siempre eres precavido y eres muy paciente con tu trabajo.")
                                                                elif suma > 34 and suma <=40:
                                                                    print ("Eres DIRECTOR DE AMBIENTACIÓN: Tu creas un ambiente unico de trabajo y haces que todo tenga armonía")
                                                                elif suma > 40 and suma <= 46:
                                                                    print ("Eres TALENTO: El popular, guap@ y todos quieren ser como tu.")
                                                                print ("************************")
                                                                resultado = print ("Gracias por tomar esta encuesta, vuelve pronto.")
                                                                print ("************************")
                                                                print ("************************")
                                                                finish = int(input("Presiona play para regresar al menu principal."))
                                                               
        
         elif rmenu ==2:
            print ("Acerca de este proyecto:")
            print ("Soy José Manuel Rivera, estudiante de cuarto semestre de LCMD")
            print ("Muchos a lo largo de la carrera nos ponemos a pensar que hacer")
            print ("con nuestro futuro, hay tantas opciones que hay algunos que no sabemos.")
            print ("Esta encuesta tiene como misión el ayudar a los jovenes")
            print ("estudiantes de LCMD para que sepan a que area de su carrera")
            print ("es el que más se asocia con su manera de trabajar y de pensar.")
            print ("Gracias por visitarnos, vuelve pronto.")
            print ("************************")
            print ("************************")
            
            rmenu = menu()
            break
    
            
    
        
    print ("Gracias por visitarnos, vuelve pronto.")
    
main()