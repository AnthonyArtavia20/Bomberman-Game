import pygame

# Inicializar pygame
pygame.init()

# Definir dimensiones de la pantalla de inicio
W, H = 800, 600

#Nombre de la ventana
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption("Menú Principal")

#ícono de la ventana
icono = pygame.image.load("Imagenes/Bombas/1.png")
pygame.display.set_icon(icono)

#Pantalla Información del creador
def informacion():
    import PantallaInformación
    PantallaInformación.mostrar_informacion_creador()

#Pantalla Configuración
def configuracion():
    import configuracion
    configuracion.configuracion()

#Iniciar juego
def iniciar_juego_bomberman():
    import Bomberman
    Bomberman.bucle_principal()

#Importamos el menú de mejores promedios:
def mejores_promedios_menu():
    import PantallaMejoresPuntajes
    PantallaMejoresPuntajes.bucle_principal()

# Paleta de colores para el fondo
Blanco = (255, 255, 255)
Negro = (0, 0, 0)


# Fuente de letra a usar
font = pygame.font.Font(None, 36)

# Creamos una función para dibujar texto en pantalla(Se le dan sus caracteristicas como argumentos).
def dibujarTexto(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#Manejamos los posibles eventos que se pueden dar en esta ventana
def manejar_eventos(buttons):
    #Obtenemos la posición exacta del mouse(x,y), devuelve un a tupla con esos valores.
    mouse_posicion = pygame.mouse.get_pos()
    #Obtener el siguiente evento de la cola de eventos de Pygame.
    #Para manejar eventos uno por uno, devuelve un objeto de evento que tiene información del evento más reciente.
    evento = pygame.event.poll()
    #Si el evento fue de cerrar la pestaña, cierra y finaliza todo.
    if evento.type == pygame.QUIT:
        pygame.quit()
        #Verifica si el tipo de evento fue de tipo click, si así lo fue llama la función Botones_funciones(botones,mouse_Pos)
        #Esto con el fin de interactuar con el menú.
    if evento.type == pygame.MOUSEBUTTONDOWN:
        Botones_Funciones(buttons, mouse_posicion)

#Función para los botones, que harán si son  precionados.
def Botones_Funciones(buttons, mouse_pos, indice=0):
    #Si el indice es menor a la cantidad de elementos en la lista de numeros entonces: 
    if indice < len(buttons):
        #Definimos variables que serán el indice actual sobre el cual se está.
        boton, accion = buttons[indice] 
        #Verificamos que el cursor del mouse está sobre el botón actual, Si es así, se ejecuta la acción asociada al botón(action()), es decir se ejecuta cuando se le da click.
        if boton.collidepoint(mouse_pos):
            accion()
            #Si el cursor del mouse no está sobre el botón actual, se llama recursivamente a la función "Botones_Funciones" con el siguiente indice, esto para pasar al siguiente botón
            #en la lista y repetir el proceso
        else:
            Botones_Funciones(buttons, mouse_pos, indice + 1)


#Boton salir del menú:
def salir_del_menu():
    pygame.display.update()
    pygame.quit()


def bucle_principal():

    ejecute = True
    while ejecute:

        #------------------------------Sector de imagenes decorativas(inicio)-----------------------
        # Cargar la imagen de fondo y escalarla a las dimensiones de la ventana
        fondo = pygame.image.load("Imagenes/Para el menu/Fondo.png")
        fondo = pygame.transform.scale(fondo, (W, H))
        # Dibujar la imagen de fondo en la pantalla
        PANTALLA.blit(fondo, (0, 0))

        titulodelFondo = pygame.image.load("Imagenes/Para el menu/Titulo editado.jpg")
        PANTALLA.blit(titulodelFondo,(100,50))

        bomberDerecho = pygame.image.load("Imagenes/Para el menu/BomberDerecho.png")
        bomberDerechoScale= pygame.transform.scale(bomberDerecho,(150,200))
        PANTALLA.blit(bomberDerechoScale,(600,290))

        bomberIzquierdo = pygame.image.load("Imagenes/Para el menu/bomberIzquierdo.png")
        bomberIzquierdoScale = pygame.transform.scale(bomberIzquierdo,(150,200))
        PANTALLA.blit(bomberIzquierdoScale,(80,290))
        
        #------------------------------Sector de imagenes decorativas(End)-----------------------

        # Creamos las variables de los rectángulos para poner texto en ellos luego
        button_1 = pygame.Rect(275, 200, 250, 50)
        button_2 = pygame.Rect(275, 300, 250, 50)
        button_3 = pygame.Rect(275, 400, 250, 50)
        button_4 = pygame.Rect(275, 500, 250, 50)
        button_5 = pygame.Rect(100, 500, 160, 50)

        # Utilizamos la función para dibujar los rectángulos con las especificaciones anteriormente dadas
        pygame.draw.rect(PANTALLA, Negro, button_1)
        pygame.draw.rect(PANTALLA, Negro, button_2)
        pygame.draw.rect(PANTALLA, Negro, button_3)
        pygame.draw.rect(PANTALLA, Negro, button_4)
        pygame.draw.rect(PANTALLA, Negro, button_5)

        #Se me ocurrió la idea de que los botones tengan la apariencia de las cajas destructibles
        BoxBoton = pygame.image.load("Imagenes/terrain/box.png")
        BoxBotonScale = pygame.transform.scale(BoxBoton,(250,50))
        BoxBotonScale2 = pygame.transform.scale(BoxBoton,(160,50))

        PANTALLA.blit(BoxBotonScale,(275,200))
        PANTALLA.blit(BoxBotonScale,(275,300))
        PANTALLA.blit(BoxBotonScale,(275,400))
        PANTALLA.blit(BoxBotonScale,(275,500))
        PANTALLA.blit(BoxBotonScale2,(100,500))

        # Utilizamos la función para dibujar texto creada al inicio
        dibujarTexto("Iniciar Juego", font, Blanco, PANTALLA, 325, 210)
        dibujarTexto("Configuración", font, Blanco, PANTALLA, 325, 310)
        dibujarTexto("Mejores puntajes", font, Blanco, PANTALLA, 300, 410)
        dibujarTexto("Salir", font, Blanco, PANTALLA, 370, 510)
        dibujarTexto("Información", font, Blanco, PANTALLA, 110, 510)

        # Lista con los botones y sus funciones (Lo que harán cuando sean presionados)
        buttons = [
            (button_1, lambda: iniciar_juego_bomberman()),
            (button_2, lambda: configuracion()),
            (button_3, lambda: mejores_promedios_menu()),
            (button_4, lambda: salir_del_menu()),
            (button_5, lambda: informacion()),
        ]

        # Si en manejar_eventos(buttons) se toma la decisión de cerrar el juego, entonces este bucle principal while cesará
        manejar_eventos(buttons)

        # Actualizamos la pantalla
        pygame.display.update()

# Ejecutar el menú principal
bucle_principal()