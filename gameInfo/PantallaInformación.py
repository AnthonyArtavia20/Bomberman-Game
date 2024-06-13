import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
PANTALLA_ANCHO= 800
PANTALLA_ALTO = 600
PANTALLA = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
pygame.display.set_caption("Información del Creador")

#ícono de la ventana
icono = pygame.image.load("Imagenes/Bombas/1.png")
pygame.display.set_icon(icono)

# Colores
Blanco = (255, 255, 255)
Negro = (0, 0, 0)

#Fuentes a usar
font_titulo = pygame.font.Font(None, 48)
font_texto = pygame.font.Font(None, 24)

# Color grisáceo con transparencia ajustable
GrisTransparente = (128, 128, 128, 128)  # Ajusta el último valor (alfa) para cambiar la transparencia

# Cargar imagen de fondo
imagen_fondo = pygame.image.load("Imagenes/Info creador/Fondo.jpeg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (PANTALLA_ANCHO, PANTALLA_ALTO))  # Ajustar tamaño de la imagen

# Cargar imagen del creador
foto = pygame.image.load("Imagenes/Info creador/Creador.png")
foto = pygame.transform.scale(foto, (200, 200))  # Ajustar tamaño de la foto

#Cargamos la imagen de las teclas a usar
fotoMovimiento = pygame.image.load("Imagenes/Info creador/Movimiento.png")
fotoMovimiento = pygame.transform.scale(fotoMovimiento, (80, 50))  # Ajustar tamaño de la foto

#Cargamos la imagen de la tecla espacio para las bombas
fotoBombasEspacio = pygame.image.load("Imagenes/Info creador/Bombas.JPG")
fotoBombasEspacio = pygame.transform.scale(fotoBombasEspacio, (90, 50))  # Ajustar tamaño de la foto

#Cargamos una imagen de las bombas para decoración
fotoBombasDefondo = pygame.image.load("Imagenes/Bombas/1.png")
fotoBombasDefondo = pygame.transform.scale(fotoBombasDefondo, (50, 50))  # Ajustar tamaño de la foto

# Función para mostrar texto en pantalla(Reutilizable)
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    PANTALLA.blit(text_surface, text_rect)

# Función para dibujar los botones en la pantalla de información del creador
def dibujar_botones():
    pygame.draw.rect(PANTALLA, Negro, (675, 25, 110, 60), 5)  
    VolverAlMenu = pygame.Rect(680, 30, 100, 50)
    pygame.draw.rect(PANTALLA, Blanco, VolverAlMenu)
    draw_text("Menu", font_titulo, Negro, 685, 40)

# Función principal
ejecuta = True #-------> Básicamente lo que enciende esta pantalla
def mostrar_informacion_creador():
    global font_texto, font_titulo
    # Bucle principal
    while ejecuta:        

        # Dibujar imagen de fondo
        PANTALLA.blit(imagen_fondo, (0, 0))

        # Dibujar rectángulo transparente en el área del marco de información
        Fondo_Gris = pygame.Surface((500, 500), pygame.SRCALPHA)  # Superficie transparente
        Fondo_Gris.fill((128, 128, 128, 128))  # Color grisáceo transparente
        PANTALLA.blit(Fondo_Gris, (50, 50))

        # Dibujar rectángulo transparente en el área del marco de autor
        Fondo_Gris = pygame.Surface((250, 290), pygame.SRCALPHA)  # Superficie transparente
        Fondo_Gris.fill((64, 64, 64, 128))  # Color grisáceo transparente
        PANTALLA.blit(Fondo_Gris, (300, 260))

        # Dibujar marco de información
        pygame.draw.rect(PANTALLA, Negro, (50, 50, 500, 500), 5)  
        # Marco para la foto
        pygame.draw.rect(PANTALLA,Negro,(300,260, 250,290),5)
        # Marco para la info de controles
        pygame.draw.rect(PANTALLA,Negro,(70,290, 200,240),5)

        # Dibujar texto de información
        draw_text("ACERCA DE", font_titulo, Negro, 70, 60)
        draw_text("Anthony Artavia", font_texto, Negro, 310, 470)
        draw_text("305510324", font_texto, Negro, 310, 500)
        draw_text("Instituto Técnológico de Costa Rica", font_texto, Negro, 70, 150)
        draw_text("Taller de programación", font_texto, Negro, 70, 170)
        draw_text("Profesor: Leonardo Araya", font_texto, Negro, 70, 190)
        draw_text("Vintage Bomberman V.1.0", font_texto, Negro, 70, 210)
        draw_text("Costa Rica", font_texto, Negro, 70, 230)
        draw_text("Ingeniería en Computadores", font_texto, Negro, 70, 260)
        draw_text("Controles", font_texto, Negro, 80, 300)
        draw_text("Movimiento:", font_texto, Negro, 80, 335)
        draw_text("Colocar Bombas:", font_texto, Negro, 80, 450)

        #Dibujar foto de las teclas
        PANTALLA.blit(fotoMovimiento,(90,360))
        # Dibujar foto del creador
        PANTALLA.blit(foto, (327, 270))
        #Dibujar tecla espacio
        PANTALLA.blit(fotoBombasEspacio, (80, 470))
        #Dibujar bombas de decoración
        PANTALLA.blit(fotoBombasDefondo,(450,200))
        
        #Dibujamos la función que diuja botones, en este caso solo el de volver, pero se puede dibujar más solo llamandolos acá
        dibujar_botones()

        #Si se preciona la X de la ventana, cerramos la pantalla
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()

            #Lógica para hacer click en el botón y devuelva al menú principal
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 675 <= mouse_pos[0] <= 785 and 25 <= mouse_pos[1] <= 85:  # Verificar si se hizo clic en el botón de volver al menú principal
                return  # Salir de la función y volver al menú principal
        
        # Actualizar pantalla
        pygame.display.update()

# Ejecutar la ventana de información del creador
mostrar_informacion_creador()