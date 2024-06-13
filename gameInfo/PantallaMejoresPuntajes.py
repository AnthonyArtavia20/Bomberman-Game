import pygame
pygame.init()

#Establecemos las proporciones de la ventana y algunas características
PANTALLA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nombres y Puntajes")

#ícono de la ventana
icono = pygame.image.load("Imagenes/Bombas/1.png")
pygame.display.set_icon(icono)

#Paleta de colores
blanco = (255,255,255)
Negro = (0, 0, 0)

font_texto = pygame.font.Font(None, 24)
font_titulo = pygame.font.Font(None,30)

#Al final descubrí que pygame no tiene sorporte nativo para mover las imagenes de los gifs, pero me gustó la imagen
#entonces lo dejo así.
gif = pygame.image.load("Imagenes/Imagenes mejores puntajes/BombermanGif.gif")
gifScalado = pygame.transform.scale(gif,(135,205))

# Función para leer nombres desde archivo de texto
def leer_nombres(txtConLosNombres):
    #El contenido de la primera linea que lee se almacena en reglon
    reglon = txtConLosNombres.readline()
    if not reglon: #Caso base, si no hay reglón, entonces llegamos al final
        return [] #Ponemos un vacio para que no afecte al resto
    return [reglon] + leer_nombres(txtConLosNombres)

# Función para leer puntajes desde archivo de texto
def leer_puntajes(txtConPuntuaciones):
    #El contenido de la primera linea que lee se almacena en reglon
    reglon = txtConPuntuaciones.readline()
    if not reglon: #Caso base, si no hay reglón, entonces llegamos al final
        return [] #Igual, ponemos un vacio para no afectar a la salida
    return [int(reglon)] + leer_puntajes(txtConPuntuaciones)

def mostrar_mejores_puntajes(PANTALLA, fuenteParaTexto, lista_combinada, indice=0): #Definir el indice como 0 y como argumento al mismo tiempo lo vimos en clase
                                                    #muy útil para no tener que ingresar otro valor, es decir no nos preocupamos por poner otro valor
    if indice >= min(5, len(lista_combinada)): #Así limitamos la especificación de "Que sean los mejores 5 promedios" haciendo que si lee más de 5
                                            #entonces la función simplemente sale de la ejecución y no devuelve nada explícitamente.
        return#Si la lista tiene menos de cinco elementos, simplemente usará la longitud de la lista como límite.
    
    # Ordenamos la lista combinada por puntaje de mayor a menor
    lista_combinada.sort(key=lambda x: x[1], reverse=True)#El argumento de lambda define que el ordenamiento se hará basado en el segundo elemento de cada tupla(los puntajes)
    #reverse true es para que se de manera descendente
    
    nombre, puntaje = lista_combinada[indice]
    text_surface = fuenteParaTexto.render(f"{nombre}. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . :  {puntaje}", True, blanco)
    PANTALLA.blit(text_surface, (250, 150 + indice * 25)) 

    mostrar_mejores_puntajes(PANTALLA, fuenteParaTexto, lista_combinada, indice + 1)

# Función para mostrar texto en pantalla(Reutilizable)
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    PANTALLA.blit(text_surface, text_rect)

# Función para dibujar los botones en la pantalla de información del creador
def dibujar_botones():
    VolverAlMenu = pygame.Rect(350, 300, 90, 40)
    pygame.draw.rect(PANTALLA, blanco, VolverAlMenu)
    draw_text("Menu", font_texto, Negro, 370, 310)


ejecuta = True
def bucle_principal():
    global ejecuta
    if ejecuta == False:
        pygame.quit()
        return
    
    PANTALLA.fill(Negro)

    # Fuente o fuentes a usar
    fuenteParaTexto = pygame.font.Font(None, 24)
    draw_text("¡Mejores puntajes!", font_titulo, blanco, 310, 100)

    # Leer los nombres
    with open('nombres.txt', 'r') as txtConLosNombres:
        nombres = leer_nombres(txtConLosNombres)

    # Leer los puntajes
    with open('puntajes.txt', 'r') as txtConPuntuaciones:
        puntajes = leer_puntajes(txtConPuntuaciones)

    # Combinar nombres y puntajes en una lista de tuplas
    lista_combinada = list(zip(nombres, puntajes))

    mostrar_mejores_puntajes(PANTALLA, fuenteParaTexto, lista_combinada)
    dibujar_botones()

    while ejecuta:
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            ejecuta = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 350 <= mouse_pos[0] <= 440 and 300 <= mouse_pos[1] <= 340:
                print("Mensaje para probar la funcionalidad del botón volver")
                return

        # Dibujar la imagen GIF en la pantalla
        PANTALLA.blit(gifScalado, (100, 100))
        pygame.display.update()

    pygame.quit()

bucle_principal()