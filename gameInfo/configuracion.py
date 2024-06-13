import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
W = 800
H = 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Configuración de Juego")
#ícono de la ventana
icono = pygame.image.load("Imagenes/Bombas/1.png")
pygame.display.set_icon(icono)

# Colores
Blanco = (255, 255, 255)
Negro = (0, 0, 0)

# Función para mostrar texto en pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Función para cargar música
def cargar_musica():
    pygame.mixer.music.load("Sound/Bomberman music.mp3")
    pygame.mixer.music.play(-1)  # -1 hace que la música se repita indefinidamente

# Función para detener la música
def detener_musica():
    pygame.mixer.music.stop()

# Función principal
def configuracion():
    # Fuentes
    font = pygame.font.Font(None, 36)

    # Estado de la música (habilitada o deshabilitada)
    musica_habilitada = True

    def dibujarConfiguracion():
        fondo = pygame.image.load("Imagenes/Menu de configuración fondo/Fondo.JPG")
        fondo = pygame.transform.scale(fondo, (W, H))
        # Dibujar la imagen de fondo en la pantalla
        screen.blit(fondo, (0, 0))
        draw_text("Configuración de Juego", font, Negro, W // 2, 50)

        Bomber = pygame.image.load("Imagenes/Menu de configuración fondo/Music Bomberman.png")
        BomberScale = pygame.transform.scale(Bomber,(200,200))
        screen.blit(BomberScale,(500,200))

        # Dibujar botones de música
        if musica_habilitada:
            draw_text("Música: Deshabilitada", font, Negro, W // 2, 200)
        else:
            draw_text("Música: Habilitada", font, Negro, W // 2, 200)

        # Dibujar botón de volver
        draw_text("Volver", font, Negro, W // 2, 400)

        # Actualizar la pantalla
        pygame.display.update()

    dibujarConfiguracion()  # Dibujar pantalla inicial

    # Bucle para manejar eventos
    ejecuta = True
    while ejecuta:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 350 <= mouse_pos[0] <= 450 and 180 <= mouse_pos[1] <= 220:
                if musica_habilitada:
                    detener_musica()
                    musica_habilitada = False
                else:
                    cargar_musica()
                    musica_habilitada = True
                dibujarConfiguracion()  # Redibujar pantalla con cambios
            elif 350 <= mouse_pos[0] <= 450 and 380 <= mouse_pos[1] <= 420:
                return  # Volver al menú principal

# Ejecutar la configuración
configuracion()