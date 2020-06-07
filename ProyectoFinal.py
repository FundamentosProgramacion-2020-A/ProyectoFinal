#Kathia Alejandra Cervantes López
#Proyecto final

from PIL import ImageDraw, Image


#Menú que se mostrará al usuario
def menu ():
    print ('''
        1. Fotografía publicitaria
        2. Fotografía de moda
        3. Fotografía retrato
        4. Fotografía artística
        5. Fotografía de paisajes
        6. Acerca de Kathia's Work
        0. Salir 
    ''')
    paquete = int(input("Teclea el paquete que te interesa: "))
    return paquete


#Función para que se muestre la imgen 
def mostrarFotografia (archivo):
    imagen = Image.open(archivo)
    return imagen
   

def calcularPrecio(fotografias):  
    lista = ["$0 ", "$16,000", "$32,000","$48,000", "$64,000", "$80,000", "$96,000", "$112,000", "$128,000", "$144,000", "$160,000"]
    precio = lista[fotografias]
    return precio


def main ():
    print ("Bienvenido a 'Kathia's Work', nos especializamos\
 en tomar fotografías, elige el paquete que estás buscando.\nRecuerda\
 teclear únicamente del 0 al 6 según el paquete que quieras.")

    elegir = menu ()

    #FOTOGRAFÍA PUBLICITARIA
    if elegir == 1:
        
        #Se muestra la foto publicitaria
        imagen = mostrarFotografia("Publicitaria.jpg")
        imagen.show()
        
        #Aviso de que sólo se puede tomar estas fotografías en interiores
        print ("\nEstas fotografías únicamente las tomamos en estudios de fotografía (interiores)")
        
        #Luces cálidas o frías
        tipoLuz = input("\n¿Quiere luces cálidas o frias? (Únicamente teclee 'c' para cálidas o 'f' para frías: ")
        #Condición
        if tipoLuz == "c":
            print ("Estas son las luces cálidas")
            imagen = mostrarFotografia("luzCalida.jpg")
            imagen.show()
        else:
            if tipoLuz == "f":
                print ("Estas son las luces frías")
                imagen = mostrarFotografia("luzFria.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear 'c' o 'f' y vuelvalo a intentar")
                
        #Tipo de luces
        print ("\nEn caso de querer luces cálidas y frías, te recomendamos elegir luces led.")
        luces = input("¿Quieres luces led o de tungsteno?(Únicamente pon 'l' o 't'): ")
        #Condición
        if luces == "l":
            print ("Estas son las luces led")
            imagen = mostrarFotografia("led.jpg")
            imagen.show()
        else:
            if luces == "t":
                print ("Estas son las luces de tungsteno")
                imagen = mostrarFotografia("tungsteno.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear 'l' o 't' y vuelvalo a intentar")
        
        #Cantidad de fotografías y precio
        print ("\nEl número máximo de fotografías que entregamos es 10")
        cantidad = int(input("¿Cuántas fotografías necesitas? "))
        precioXCantidad = calcularPrecio (cantidad)
        print ("El precio es:", precioXCantidad)
        
        #Información del usuario para contectarlo y aclarar agendar cita
        número = int(input("\nTeclea tu número telefónico para contactarte y aclarar más detalles: "))
        print ("Gracias, nosotros te contactaremos en breve")
    
    
    #FOTOGRAFÍA DE MODA
    elif elegir == 2:
        
        #Fotografía muestra
        imagen = mostrarFotografia("Moda.jpg")
        imagen.show()
        
        #Para saber si es en exterior o condición
        espacio = input("\n¿Quiere las fotografías en exterior o interior?(Asegurese de poner únicamente 'e' para exterior o 'i' para interior): ")
        #Condición
        if espacio == "e":
            print ("Es problable que se aporveche la luz del día sin usar luces. En caso de necesitar: ")
        else:
            if espacio == "i":
                print ("Es necesario usar luces")
            else:
                print ("ERROR, asegurese de escribir 'interior' o 'exterior' y vuelvelo a intentar")
        
        #Luces cálidas o frías
        tipoLuz = input("\n¿Quiere luces cálidas o frias? (Únicamente teclee 'c' para cálidas o 'f' para frías: ")
        #Condición
        if tipoLuz == "c":
            print ("Estas son las luces cálidas")
            imagen = mostrarFotografia("luzCalida.jpg")
            imagen.show()
        else:
            if tipoLuz == "f":
                print ("Estas son las luces frías")
                imagen = mostrarFotografia("luzFria.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear 'f' o 'c' y vuelvalo a intentar")
                
        #Tipo de luces
        print ("\nEn caso de querer luces cálidas y frías, te recomendamos elegir luces led.")
        luces = input("¿Quieres luces led o de tungsteno?(Únicamente pon 'l' o 't'): ")
        #Condición
        if luces == "l":
            print ("Estas son las luces led")
            imagen = mostrarFotografia("led.jpg")
            imagen.show()
        else:
            if luces == "t":
                print ("Estas son las luces de tungsteno")
                imagen = mostrarFotografia("tungsteno.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear 'c' o 'f' y vuelvalo a intentar")
                
        #Cantidad de fotografías y precio        
        print ("\nEl número máximo de fotografías que entregamos es 10")
        cantidad = int(input("¿Cuántas fotografías necesitas? "))
        precioXCantidad = calcularPrecio (cantidad)
        print ("El precio es:", precioXCantidad)
        
        #Información del usuario para contectarlo y aclarar agendar cita
        número = int(input("\nTeclea tu número telefónico para contactarte y aclarar más detalles: "))
        print ("Gracias, nosotros te contactaremos en breve")
      
    #Fotografía retrato
    elif elegir == 3:
        
        #Fotografía muestra
        imagen = mostrarFotografia("Retrato.jpg")
        imagen.show()
        
        #Para saber si es en exterior o condición
        espacio = input("\n¿Quiere las fotografías en exterior o interior?(Asegurese de poner únicamente 'e' para exterior o 'i' para interior): ")
        #Condición
        if espacio == "e":
            print ("Es problable que se aporveche la luz del día sin usar luces. En caso de necesitar: ")
        else:
            if espacio == "i":
                print ("Es necesario usar luces")
            else:
                print ("ERROR, asegurese de escribir 'interior' o 'exterior' y vuelvelo a intentar")
        
        #Luces cálidas o frías
        tipoLuz = input("\n¿Quiere luces cálidas o frias? (Únicamente teclee 'c' para cálidas o 'f' para frías: ")
        #Condición
        if tipoLuz == "c":
            print ("Estas son las luces cálidas")
            imagen = mostrarFotografia("luzCalida.jpg")
            imagen.show()
        else:
            if tipoLuz == "f":
                print ("Estas son las luces frías")
                imagen = mostrarFotografia("luzFria.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear únicamente 'c' o 'f' y vuelvelo a intentar")
                
        #Tipo de luces
        print ("\nEn caso de querer luces cálidas y frías, te recomendamos elegir luces led.")
        luces = input("¿Quieres luces led o de tungsteno?(Únicamente pon 'l' o 't'): ")
        #Condición
        if luces == "l":
            print ("Estas son las luces led")
            imagen = mostrarFotografia("led.jpg")
            imagen.show()
        else:
            if luces == "t":
                print ("Estas son las luces de tungsteno")
                imagen = mostrarFotografia("tungsteno.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear 'l' o 't' y vuelvalo a intentar")
                
       
        #Cantidad de fotografías y precio        
        print ("\nEl número máximo de fotografías que entregamos es 10")
        cantidad = int(input("¿Cuántas fotografías necesitas? "))
        precioXCantidad = calcularPrecio (cantidad)
        print ("El precio es:", precioXCantidad)
        
        #Información del usuario para contectarlo y aclarar agendar cita
        número = int(input("\nTeclea tu número telefónico para contactarte y aclarar más detalles: "))
        print ("Gracias, nosotros te contactaremos en breve")
        
    #Fotografía artística    
    elif elegir == 4:
        
        #Fotografía muestra
        imagen = mostrarFotografia("Artistica.jpg")
        imagen.show()
        
       #Para saber si es en exterior o condición
        espacio = input("\n¿Quiere las fotografías en exterior o interior?(Asegurese de poner únicamente 'e' para exterior o 'i' para interior): ")
        #Condición
        if espacio == "e":
            print ("Es problable que se aporveche la luz del día sin usar luces. En caso de necesitar: ")
        else:
            if espacio == "i":
                print ("Es necesario usar luces")
            else:
                print ("ERROR, asegurese de escribir 'interior' o 'exterior' y vuelvelo a intentar")
        
        #Luces cálidas o frías
        tipoLuz = input("\n¿Quiere luces cálidas o frias? (Únicamente teclee 'c' para cálidas o 'f' para frías: ")
        #Condición
        if tipoLuz == "c":
            print ("Estas son las luces cálidas")
            imagen = mostrarFotografia("luzCalida.jpg")
            imagen.show()
        else:
            if tipoLuz == "f":
                print ("Estas son las luces frías")
                imagen = mostrarFotografia("luzFria.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear únicamente 'c' o 'f' y vuelvelo a intentar")
                
        #Tipo de luces
        print ("\nEn caso de querer luces cálidas y frías, te recomendamos elegir luces led.")
        luces = input("¿Quieres luces led o de tungsteno?(Únicamente pon 'l' o 't'): ")
        #Condición
        if luces == "l":
            print ("Estas son las luces led")
            imagen = mostrarFotografia("led.jpg")
            imagen.show()
        else:
            if luces == "t":
                print ("Estas son las luces de tungsteno")
                imagen = mostrarFotografia("tungsteno.jpg")
                imagen.show()
            else:
                print ("ERROR, asegurese de teclear 'l' o 't' y vuelvalo a intentar")
                
        #Cantidad de fotografías y precio        
        print ("\nEl número máximo de fotografías que entregamos es 10")
        cantidad = int(input("¿Cuántas fotografías necesitas? "))
        precioXCantidad = calcularPrecio (cantidad)
        print ("El precio es:", precioXCantidad)
        
        #Información del usuario para contectarlo y aclarar agendar cita
        número = int(input("\nTeclea tu número telefónico para contactarte y aclarar más detalles: "))
        print ("Gracias, nosotros te contactaremos en breve")
        
    #Fotografía de paisaje   
    elif elegir == 5:
        #Fotografía muestra
        imagen = mostrarFotografia("Paisaje.jpg")
        imagen.show()
        
        #Aviso de que sólo se puede tomar estas fotografías en exteriores
        print ("\nEstas fotografías únicamente las tomamos en exteriores, por lo cual no se necesitaran luces.")
        
        hora = input("\n¿A qué hora se prefiere que se tomen las fotografías? (Únicamente tecle 'd' para día, 't' para tarde o 'n' para noche) ")
        if hora == "d":
            print ("Nuestro horario de día es de 05:00 a 11:00")
        else:
            if hora == "t":
                print ("Nuestro horario de tarde es de 12:00 a 18:00")
            else:
                if hora == "n":
                    print ("Nuestro horario de noche es de 19:00 a 02:00am")
                else:
                    print ("Asegurate de teclear 'd', 't' o 'n' y vuelvelo a intentar")
        
        print("\nNo es necesario que esté presente en toda la sesión")
                
        #Cantidad de fotografías y precio        
        print ("\nEl número máximo de fotografías que entregamos es 10")
        cantidad = int(input("¿Cuántas fotografías necesitas? "))
        precioXCantidad = calcularPrecio (cantidad)
        print ("El precio es:", precioXCantidad)
        
        #Información del usuario para contectarlo y aclarar agendar cita
        número = int(input("\nTeclea tu número telefónico para contactarte y aclarar más detalles: "))
        print ("Gracias, nosotros te contactaremos en breve")
        
    elif elegir == 6:
        print ("¡Hola!\nKathia's Work, es una empresa especializada \
en hacer fotografías publicitarias, de moda, retrato, artísticas y de paisajes. \
Nos gusta que nuestros clientes queden satisfechos con nuestro trabajo, \
es por eso que hicimos este programa el cual recolecta la información \
tecleada por el usuario y esta se va a nuestra base de datos para poder realizar la \
idea que el cliente tiene en mente.\nPuede teclear lo que necesita mediante ese medio \
o contactarnos por las siguientes plataformas:\nTeléfono: 55 84 30 42 08\n\
Correo electrónico: kathiacervantescea@gmail.com\nFacebook: Kathia's Work\n\
Gracias por su preferencia")
    elif elegir == 0:
        print ("¡Gracias por tu visita!")
    else:
        print ("Opción incorrecta, vuelvalo a intentar y asegurese que está tecleando un número entre 0 - 6")

            
main ()
            