#Primero aparece una ventana donde se selecciona la skin y se pone el nombre
import pygame

# Inicialización de Pygame
pygame.init()

# Pantalla - Ventana (Proporciones)
W, H = 650, 650
PANTALLA = pygame.display.set_mode((W,H))

#Título
pygame.display.set_caption("¡Vintage Bomberman! WOW")

#ícono de la ventana
icono = pygame.image.load("Imagenes/Bombas/1.png")
pygame.display.set_icon(icono)

#Sector de paleta de colores
gris = (146, 143, 136)
grisOscuro = (118, 109, 94)
negro = (0,0,0)
verde = (0, 171, 21)
blanco = (255,255,255)

# Variable para almacenar el nombre del jugador este se modifica en la función manejar evento
nombre_jugador = ""

#Nivel inicial
nivel = 1

# Variable para almacenar la skin seleccionada (inicialmente ninguna)
skin_seleccionada = None

#Dibujar logo
imagen_logo = pygame.image.load("Imagenes/Logo/logo.png")
imagen_logo = pygame.transform.scale(imagen_logo, (400, 100))


#----------------------(Inicio)Cargar imagenes para los botones skins------------------------------

imagen_skin1 = pygame.image.load("Imagenes/Player/Down/Down1.png")
imagen_skin1 = pygame.transform.scale(imagen_skin1, (100, 100))

imagen_skin2 = pygame.image.load("Imagenes/Player2/Down/1.png")
imagen_skin2 = pygame.transform.scale(imagen_skin2, (100, 100))

imagen_skin3 = pygame.image.load("Imagenes/Player3/quieto.png")
imagen_skin3 = pygame.transform.scale(imagen_skin3, (100, 100))

#----------------------(End)Cargar imagenes para los botones skins------------------------------

# Función para renderizar texto en la pantalla
def renderizar_texto(texto, longitud, x, y, color):
    font = pygame.font.Font(None, longitud)
    superficie_texto = font.render(texto, True, color)
    PANTALLA.blit(superficie_texto, (x, y))

# Función para dibujar un botón
def dibujar_boton(texto, x, y, ancho, alto, color_activo, color_inactivo):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + alto > mouse[1] > y:
        pygame.draw.rect(PANTALLA, color_activo, (x, y, ancho, alto))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(PANTALLA, color_inactivo, (x, y, ancho, alto))

    renderizar_texto(texto, 20, x + ancho / 2 - len(texto) * 3, y + alto / 2 - 10, negro)

    return False

# Función para guardar el nombre del jugador en un
#  archivo de texto #Aprendí esto en una consulta con el profe Leonardo
def guardar_texto(nombre_jugador):
    #la "a" es de append. , es para que agregue nombres uno tras otro y no borre o sobre escriba
    with open("nombres.txt", "a") as archivo:
        archivo.write(nombre_jugador + "\n")

# Bucle para la ventana inicial de ingreso de nombre
# Función recursiva para la ventana inicial de ingreso de nombre y selección de skin
def manejar_eventoMenu(ventana_activa=True):
    global nombre_jugador
    global skin_seleccionada

    #Mientras ventana_activa sea True, se mantiene pasandole eventos a la función principal.
    while ventana_activa:
        event = pygame.event.poll()  # Para hacer que los eventos vengan en cola
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        #Si hay un evento de tipo tecla precionada
        elif event.type == pygame.KEYDOWN:
            #y además es la tecla borrar, entonces elimine hacía atrás un caracter
            if event.key == pygame.K_BACKSPACE:
                nombre_jugador = nombre_jugador[:-1]
                #Si no cualquier otra cosa significan teclas para agregar a la variable nombre.
            else:
                nombre_jugador += event.unicode

        # Color de la pantalla antes del juego
        PANTALLA.fill(negro)

        #Dibujar logo
        PANTALLA.blit(imagen_logo,(125,100))

        # Renderizar texto para ingresar el nombre
        renderizar_texto("Por favor, escribe tu nombre:", 36, 100, 300, blanco)
        renderizar_texto(nombre_jugador, 36, 100, 350, blanco)

        renderizar_texto("Seleccona una skin a tu gusto: ",35,100,500,blanco)
        # Dibujar botón de inicio
        if dibujar_boton("Iniciar juego", 250, 400, 150, 50, verde, blanco):
            #Cuando el jugador le da al botón iniciar juego, esta ventana se cierra pero guarda su nombre en un archivo de texto(Aprendí de esto con una consulta del profe Leonardo)
            guardar_texto(nombre_jugador)
            ventana_activa = False
            #Si la persona le da a iniciar juego, entonces la ventana se pone en False, lo que finaliza el bucle de esta ventana y la cierra
            #para poder continuar con el juego(Solo si está activa: if ventana_activa: "manejar_evento(ventana_activa)")

        # Dibujar botones para seleccionar skin
        if dibujar_boton("Skin 1", 125, 530, 100, 100, verde if skin_seleccionada == 1 else blanco, verde if skin_seleccionada == 1 else blanco):
            skin_seleccionada = 1
        if dibujar_boton("Skin 2", 275, 530, 100, 100, verde if skin_seleccionada == 2 else blanco, verde if skin_seleccionada == 2 else blanco):
            skin_seleccionada = 2
        if dibujar_boton("Skin 3", 425, 530, 100, 100, verde if skin_seleccionada == 3 else blanco, verde if skin_seleccionada == 3 else blanco):
            skin_seleccionada = 3

        #Dibujar skins sobre los botones:
        PANTALLA.blit(imagen_skin1,(125,530))
        PANTALLA.blit(imagen_skin2,(275,530))
        PANTALLA.blit(imagen_skin3,(425,530))
        # Si la persona no seleccionó ninguna skin, por defecto se le asigna la 1
        if skin_seleccionada is None:
            skin_seleccionada = 1

        # Actualizar la pantalla
        pygame.display.update()

# Llamada inicial a la función recursiva
manejar_eventoMenu()

#---------------------------------------------JUEGO BOMBERMAN--------------------------------------#

# Pantalla - Ventana (Proporciones)
PANTALLA = pygame.display.set_mode((W,H))


#Fuentes de texto para mensajes:
fuente = pygame.font.Font(None, 36)  # Fuente y tamaño del texto

#Imagenes para los bloques destructibles
muro = pygame.image.load("Imagenes/terrain/block.png")
muro_INTERNOS_scale = pygame.transform.scale(muro, (50, 50))  # Ajustar tamaño de la imagen al rectángulo

#Imagenes para los bloques destructibles
muro_destructible = pygame.image.load("Imagenes/terrain/box.png")
muro_destructible_scale = pygame.transform.scale(muro_destructible,(50,50)) # Ajustar tamaño de la imagen al rectángulo

#Imagen para los puntos
puntosImagen = pygame.image.load("Imagenes/Points/PointsImage.png")
puntosImagen_scale = pygame.transform.scale(puntosImagen,(50,50))

#------------------------------------------Creación de los puntos en juego(Inicio)-----------------------------------------------------#
# Lista de posiciones de los puntos y su respectivo nivel
listaPosicionesPuntos = [
    # Antes de Línea 1
    (500, 50),
    (550, 50),
    #Linea 1
    (100,100),
    #Entre 1 y 2
    (200,150),
    #Linea 2
    (400,200),
    #Linea entre 2 y 3
    (0,250),
    (150,250),
    (350,250),
    (500,250),
    #Linea 4
    (100,400),
    #Debajo linea 4
    (150,450),

]

listaPosicionesPuntosNivel2 = [
    #Antes de linea 1
    (50,50),
    (500,50),
    #Linea 1
    (100,100),
    #Linea entre 1 y 2
    (50,150),
    (600,150),
    #linea entre 2 y 3
    (150,250),
    (400,250),
    #Entre linea 3 y 4
    (150,250),
    #Despues de linea 4
    (200,450),
    (350,450),
]

listaPosicionesPuntosNivel3 = [
    #Ante de linea 1
    (500,50),
    (50,50),
    (350,50),
    #Linea entre 1 y 2
    (50,150),
    (100,150),
    (200,150),
    (600,150),
    #Entre 2 y 3
    (0,250),
    (350,250),
    #Linea entre 3 y 4
    (50,350),
    #Linea 4
    (0,400),
    (200,400),
    (600,400),
    #Despues de linea 4
    (300,450),
]

#---------------Puntos primer Nivel(Inicio)-----------------------
# Creamos una función que dibuja en pantalla la imágenes de los puntos
def dibujarPuntosPantalla(PosicionesPuntosenLista):
    if not PosicionesPuntosenLista:
        return #Si no hay puntos en la lista, retorne nada.
    
    x, y = PosicionesPuntosenLista[0] #Extraemos las coordenadas del punto a analizar, (x,y) en la lista.
    PANTALLA.blit(puntosImagen_scale, (x, y)) #Dibujamos
    dibujarPuntosPantalla(PosicionesPuntosenLista[1:])#Llamada recursiva analizando todos los componentes.

#Nota: Anteriormente se hicieron 2 funciones que por separado hacian la deteccion y otra eliminaba pero surgieron varios
# bugs, se decidió hacer una función fucionada para evitar errores y organizar de mejor manera el código.
def detectar_colision_y_eliminar_puntos(px, py, listapuntos, puntos, rango_colision=40):
    if not listapuntos:
        return [], puntos  # Si no quedan puntos en la lista, retorna la lista vacía y los puntos acumulados

    puntos_x, puntos_y = listapuntos[0] #Extraemos las coords del punto a analizar.
    centro_puntos_x = puntos_x + 20 #Ajustamos cual es el centro de, por decirlo así, el bloque del punto en X
    centro_puntos_y = puntos_y + 20# Lo mismo pero en Y

    if abs(px - centro_puntos_x) <= rango_colision and abs(py - centro_puntos_y) <= rango_colision:
        # Si el jugador colisiona con el punto, se suma un punto al contador y se elimina el punto de la lista
        print("Se sumó un punto")
        puntos += 1
        return listapuntos[1:], puntos
    else:
        # Si no hay colisión, se mantiene el punto en la lista
        nuevos_puntos, puntos_actualizados = detectar_colision_y_eliminar_puntos(px, py, listapuntos[1:], puntos)
        return [listapuntos[0]] + nuevos_puntos, puntos_actualizados

#-----0------0----Puntos primer Nivel(end)------0------0-----------

#---------------Puntos Segundo Nivel(Inicio)-------------------
def dibujarPuntosPantallaNivel2(posicionesPuntosNivel2):
    if not posicionesPuntosNivel2:
        return #Si no hay puntos en la lista, retorne nada.
    
    x, y = posicionesPuntosNivel2[0] #Extraemos las coordenadas del punto a analizar, (x,y) en la lista.
    PANTALLA.blit(puntosImagen_scale, (x, y)) #Dibujamos
    dibujarPuntosPantallaNivel2(posicionesPuntosNivel2[1:])#Llamada recursiva analizando todos los componentes.

def detectar_colision_y_eliminar_puntosNivel2(px, py, listapuntos, puntos, rango_colision=40):
    if not listapuntos:
        return [], puntos  # Si no quedan puntos en la lista, retorna la lista vacía y los puntos acumulados

    puntos_x, puntos_y = listapuntos[0] #Extraemos las coords del punto a analizar.
    centro_puntos_x = puntos_x + 20 #Ajustamos cual es el centro de, por decirlo así, el bloque del punto en X
    centro_puntos_y = puntos_y + 20# Lo mismo pero en Y

    if abs(px - centro_puntos_x) <= rango_colision and abs(py - centro_puntos_y) <= rango_colision:
        # Si el jugador colisiona con el punto, se suma un punto al contador y se elimina el punto de la lista
        print("Se sumó un punto")
        puntos += 1
        return listapuntos[1:], puntos
    else:
        # Si no hay colisión, se mantiene el punto en la lista
        nuevos_puntos, puntos_actualizados = detectar_colision_y_eliminar_puntosNivel2(px, py, listapuntos[1:], puntos)
        return [listapuntos[0]] + nuevos_puntos, puntos_actualizados
#-----0------0----Puntos Segundo Nivel(End)------0----------0-------
#---------------Tercer y último nivel(inicio)-------------------
def dibujarPuntosPantallaNivel3(posicionesPuntosNivel3):
    if not posicionesPuntosNivel3:
        return #Si no hay puntos en la lista, retorne nada.
    
    x, y = posicionesPuntosNivel3[0] #Extraemos las coordenadas del punto a analizar, (x,y) en la lista.
    PANTALLA.blit(puntosImagen_scale, (x, y)) #Dibujamos
    dibujarPuntosPantallaNivel3(posicionesPuntosNivel3[1:])#Llamada recursiva analizando todos los componentes.

def detectar_colision_y_eliminar_puntosNivel2(px, py, listapuntos, puntos, rango_colision=40):
    if not listapuntos:
        return [], puntos  # Si no quedan puntos en la lista, retorna la lista vacía y los puntos acumulados

    puntos_x, puntos_y = listapuntos[0] #Extraemos las coords del punto a analizar.
    centro_puntos_x = puntos_x + 20 #Ajustamos cual es el centro de, por decirlo así, el bloque del punto en X
    centro_puntos_y = puntos_y + 20# Lo mismo pero en Y

    if abs(px - centro_puntos_x) <= rango_colision and abs(py - centro_puntos_y) <= rango_colision:
        # Si el jugador colisiona con el punto, se suma un punto al contador y se elimina el punto de la lista
        print("Se sumó un punto")
        puntos += 1
        return listapuntos[1:], puntos
    else:
        # Si no hay colisión, se mantiene el punto en la lista
        nuevos_puntos, puntos_actualizados = detectar_colision_y_eliminar_puntosNivel2(px, py, listapuntos[1:], puntos)
        return [listapuntos[0]] + nuevos_puntos, puntos_actualizados
#----0--------0---Tercer y último nivel(End)-----0------------0-----


#Función para almacenar los puntos en un txt para que así la ventana de mejores puntajes pueda leer
#el último puntaje que ganó el jugador.
def agregar_puntos_a_txt(puntos):
    with open("puntajes.txt", "a") as archivo: #La "a" es de .append
        archivo.write(str(puntos) + "\n")

# Función para dibujar el contador de bombas disponibles en la pantalla
def dibujar_contador_puntos():
    font = pygame.font.Font(None, 30)
    texto = font.render("" + str(puntos), True, blanco)
    PANTALLA.blit(texto, (80, 573))

#------------------------------------------Creación de los puntos en juego(End)-----------------------------------------------------#


#------------------------------------------Creación de los bordes exteriores(Inicio)---------------------------------------------------#

#Se creó una función recursiva que pone una imagen de forma recursiva hacía la derecha hasta que ya no caben, esto se hace haciendo la imagen un poco más grande, calculando cuantas veces cabe en la pantalla y luego se usa ese parámetro
#para que sea el limite de la función recursiva.
    #Función auxiliar #1
def draw_muros_superiores_aux(muro_imagen, cantidad_muros, posicion_x=0):#La posición_x, ponemos 0 para que empieze desde la izquierda del todo poniendo bloques
    if cantidad_muros <= 0:
        return  # Caso base: No quedan muros por dibujar ya que se llegó al final calculado

    # Dibujar un muro en el borde superior
    PANTALLA.blit(muro_imagen, (posicion_x, 0))

    # Calcular la posición x del siguiente muro
    nueva_posicion_x = posicion_x + muro_imagen.get_width()  #Se le va sumando su ancho para que no quede una encima de la otra o separadas.

    # Llamar recursivamente a la función para dibujar el siguiente muro
    draw_muros_superiores_aux(muro_imagen, cantidad_muros - 1, nueva_posicion_x)

#Se tuvo que crear una función a parte solo para los muros inferiores ya que haciendolo todo solo con una principal y una auxiliar resultó en muchos más bugs
    #Función auxiliar #2
def draw_muros_inferiores_aux(muro_imagen, cantidad_muros, posicion_x=0):
    if cantidad_muros <= 0:
        return  # Caso base: No quedan muros por dibujar

    # Dibujar un muro en el borde inferior
    PANTALLA.blit(muro_imagen, (posicion_x, 500))

    # Calcular la posición x del siguiente muro
    nueva_posicion_x = posicion_x + muro_imagen.get_width()  # Avanzar una anchura de muro

    # Llamar recursivamente a la función para dibujar el siguiente muro
    draw_muros_inferiores_aux(muro_imagen, cantidad_muros - 1, nueva_posicion_x)

#Función pricipal
def draw_bordes_y_temporizador(): 
    pygame.draw.rect(PANTALLA, grisOscuro, (0, 550, 800, 90))  # Borde inferior
    pygame.draw.rect(PANTALLA, gris, (12, 560, 623, 90))  # Área de juego
    pygame.draw.rect(PANTALLA, grisOscuro, (0, 640, 800, 90))  # Borde inferior

    # Cargar la imagen del muro y ajustar su tamaño
    muro_imagen = pygame.image.load("Imagenes/terrain/block.png")
    muro_imagen = pygame.transform.scale(muro_imagen, (93, 50))  # Ajustar tamaño del muro

    # Definir la cantidad de muros consecutivos a dibujar en los bordes superior e inferior
    cantidad_muros_superiores = 7
    cantidad_muros_inferiores = 7

    # Dibujar varios muros consecutivos a lo largo del borde superior de forma recursiva
    draw_muros_superiores_aux(muro_imagen, cantidad_muros_superiores)

    # Dibujar varios muros consecutivos a lo largo del borde inferior de forma recursiva
    draw_muros_inferiores_aux(muro_imagen, cantidad_muros_inferiores)

#Sector Función recursiva encargada de darle imagen a los bloques internos(donde el jugador chocará jugando)colocados:
def draw_bloques_internos(posiciones):
    if not posiciones:
        return  # Caso base: la lista de posiciones está vacía
    # Dibujar el bloque en la primera posición de la lista
    x, y = posiciones[0]
    PANTALLA.blit(muro_INTERNOS_scale,(x,y))
    # Llamar recursivamente a la función con la lista restante de posiciones de bloques
    draw_bloques_internos(posiciones[1:])


#Sector Función recursiva encargada de darle imagen a los bloques destructibles:
def draw_bloques_destructibles(posiciones,posiciones2,posiciones3):
    if nivel == 1:
        if not posiciones:
            return #Caso base: La lista de bloques por pintar está vacia
        #Se dibuja el bloque en la primera posición de la lista
        x,y = posiciones[0]
        PANTALLA.blit(muro_destructible_scale,(x,y))
        #Se llama recursivamente a la función con lo que queda por dibujar en la lista, eliminando el de atrás.
        draw_bloques_destructibles(posiciones[1:],posiciones2,posiciones3)
    if nivel == 2:
        if not posiciones2:
            return #Caso base: La lista de bloques por pintar está vacia
        #Se dibuja el bloque en la primera posición de la lista
        x,y = posiciones2[0]
        PANTALLA.blit(muro_destructible_scale,(x,y))
        #Se llama recursivamente a la función con lo que queda por dibujar en la lista, eliminando el de atrás.
        draw_bloques_destructibles(posiciones,posiciones2[1:],posiciones3)
    if nivel == 3:
        if not posiciones3:
            return
        x,y = posiciones3[0]
        PANTALLA.blit(muro_destructible_scale,(x,y))
        draw_bloques_destructibles(posiciones,posiciones2,posiciones3[1:])
#---------------------------------------------------Creación de los bordes exteriores(end)---------------------------------------------------#

#----------------------------Creación de la llave y la puerta para saltar a otros niveles(Inicio)---------------------------------#

#---------------(Inicio)Nivel 1-----------------------#
#Donde aparece la puerta
puerta_x = 0
puerta_y = 450

# Cargar la imagen de la llave, scalarla y rodearla con un rectángulo(Esto último se hace en la función que la dibuja)
#Donde aparece la llave
llave_img = pygame.image.load("imagenes/Key/Key.png")
llave_img = pygame.transform.scale(llave_img, (40, 40))
llave_rect = llave_img.get_rect()
llave_rect.x = 450
llave_rect.y = 50

# Cargar la imagen de la puerta, scalarla y rodearla con un rectángulo(Igual, se hace en la función)..
puerta_img = pygame.image.load("imagenes/Door/door sprite.png")
puerta_img = pygame.transform.scale(puerta_img,(50,50))
puerta_rect = puerta_img.get_rect(topleft=(puerta_x, puerta_y))

# Por defecto, ya que está escondida en un bloque
llave_recogidaNivel1 = False

# La puerta se mantiene cerrada hasta que el jugador se acerca con la llave en el inventario
puerta_abiertaNivel1 = False

# Variable para mantener registro de si ya se ha detectado una colisión, se mantiene en False, porque si no cerraria la función
#apenas se iniciara el bucle.
colision_detectada_PuertaNivel1 = False

# Función encargada de verificar la colisión con la puerta y la llave
def detectar_colisionLlavePuertaNivel1(px, py):
    global llave_recogidaNivel1, nivel, ejecuta, colision_detectada_PuertaNivel1
    # Verificar si ya se ha detectado una colisión si es así, cierra la función para que se deje de dibujar la puerta
    if colision_detectada_PuertaNivel1:
        return #Retorna nada.
    # Verificar si el jugador está completamente dentro de los límites de la llave
    if not llave_recogidaNivel1 and llave_rect.collidepoint(px, py):
        llave_recogidaNivel1 = True
        print("¡Has recogido la llave!")

    # Detectar colisión con la puerta
    if puerta_rect.colliderect(pygame.Rect(px, py, 35, 35)):
        if llave_recogidaNivel1:
            nivel += 1
            print("¡Has abierto la puerta del nivel 1! Ahora estás en el nivel 2")
            colision_detectada_PuertaNivel1 = True  # Marcar que se ha detectado una colisión
            
            #Mostrar mensaje de pasaste a otro nivel
            #Marco negro
            pygame.draw.rect(PANTALLA, negro, (50, 50, 540, 500), 5)
            Fondo_Gris = pygame.Surface((540, 490), pygame.SRCALPHA)  # Superficie transparente Largo, Ancho
            Fondo_Gris.fill((80, 64, 64, 128))  # Color grisáceo transparente
            PANTALLA.blit(Fondo_Gris, (50, 50)) #Donde aparece X y Y

            #Texto de pasaste a otro nivel:
            font = pygame.font.SysFont("Arial", 48)
            game_over_text = font.render("¡Nivel 2 alcanzado!", True, negro,blanco)
            text_rect = game_over_text.get_rect(center=(W // 2, H // 2)) #Situar el texto en el centro
            PANTALLA.blit(game_over_text, text_rect) #Dibujar el texto con las especificaciones
            pygame.display.update()  # Actualizar la pantalla para mostrar el mensaje
            pygame.time.delay(2000)
            return

#Cambiar la posición de la llave y la puerta
def renderizar_elementosNivel1():
    global puerta_abiertaNivel1

    # Renderizar la llave si no ha sido recogida
    if not llave_recogidaNivel1:
        # Dibujar el rectángulo donde se colocará la llave #Aquí estaba el error(estaba poniendo llave.x en lugar de llave_rect.x)
        #la idea es que una vez se recoja la llave, este rectangulo la tape
        pygame.draw.rect(PANTALLA, verde, (llave_rect.x, llave_rect.y,45,45))
        PANTALLA.blit(llave_img, llave_rect)

    #Si la llave fué recogida, entonces dibujela en el inventario
    elif llave_recogidaNivel1:
        PANTALLA.blit(llave_img, (150, 590))

    # Renderizar la puerta dependiendo de si está abierta o cerrada

#---------------(End)Nivel 1-----------------------#

#---------------(Inicio)Nivel 2-----------------------#

#Donde aparece la puerta
puerta_x2 = 300
puerta_y2 = 400

# Cargar la imagen de la llave, scalarla y rodearla con un rectángulo(Esto último se hace en la función que la dibuja
llave2_img = pygame.image.load("imagenes/Key/key2Definitiva.png")
llave2_img = pygame.transform.scale(llave2_img, (30, 45))
llave2_rect = llave2_img.get_rect()
llave2_rect.x = 0
llave2_rect.y = 50

# Cargar la imagen de la puerta, scalarla y rodearla con un rectángulo(Igual, se hace en la función).
#Donde aparece la llave
puerta2_img = pygame.image.load("imagenes/Door/door sprite.png")
puerta2_img = pygame.transform.scale(puerta2_img,(50,50))
puerta2_rect = puerta2_img.get_rect(topleft=(puerta_x2, puerta_y2))

# Por defecto, ya que está escondida en un bloque
llave_recogidaNivel2 = False

# La puerta se mantiene cerrada hasta que el jugador se acerca con la llave en el inventario
puerta_abiertaNivel2 = False

# Variable para mantener registro de si ya se ha detectado una colisión, se mantiene en False, porque si no cerraria la función
#apenas se iniciara el bucle.
colision_detectada_PuertaNivel2 = False

# Función encargada de verificar la colisión con la puerta y la llave
def detectar_colisionPuertaNivel2(px, py):
    global llave_recogidaNivel2, nivel, ejecuta, colision_detectada_PuertaNivel2

    # Verificar si ya se ha detectado una colisión si es así, cierra la función para que se deje de dibujar la puerta
    if colision_detectada_PuertaNivel2:
        return
    # Verificar si el jugador está completamente dentro de los límites de la llave
    if not llave_recogidaNivel2 and llave2_rect.collidepoint(px, py):
        llave_recogidaNivel2 = True
        print("¡Has recogido la llave Nivel 2!")

    # Detectar colisión con la puerta niel 2
    if puerta2_rect.colliderect(pygame.Rect(px, py, 35, 35)):
        if llave_recogidaNivel2:
            nivel += 1
            print("¡Has abierto la puerta del Nivel2! Ahora estás en el nivel 3")
            colision_detectada_PuertaNivel2 = True  # Marcar que se ha detectado una colisión

            #Mostrar mensaje de pasaste a otro nivel
            #Marco negro
            pygame.draw.rect(PANTALLA, negro, (50, 50, 540, 500), 5)
            Fondo_Gris = pygame.Surface((540, 490), pygame.SRCALPHA)  # Superficie transparente Largo, Ancho
            Fondo_Gris.fill((80, 64, 64, 128))  # Color grisáceo transparente
            PANTALLA.blit(Fondo_Gris, (50, 50)) #Donde aparece X y Y

            #Texto de pasaste a otro nivel:
            font = pygame.font.SysFont("Arial", 48)
            game_over_text = font.render("¡Nivel 3 alcanzado!", True, negro,blanco)
            text_rect = game_over_text.get_rect(center=(W // 2, H // 2)) #Situar el texto en el centro
            PANTALLA.blit(game_over_text, text_rect) #Dibujar el texto con las especificaciones
            pygame.display.update()  # Actualizar la pantalla para mostrar el mensaje
            pygame.time.delay(2000)
            return
            return

#Cambiar la posición de la llave y la puerta
def renderizar_elementosPuertaNivel2():
    global puerta_abiertaNivel2

    # Renderizar la llave si no ha sido recogida
    if not llave_recogidaNivel2:
        #Rectangulo que rodea la llave para el nivel 2, la idea es que una vez se recoja la llave, este rectangulo la tape.
        pygame.draw.rect(PANTALLA, verde, (llave2_rect.x, llave2_rect.y,45,45))
        PANTALLA.blit(llave2_img, llave2_rect)
    #Si la llave fué recogida, entonces dibujela en el inventario
    elif llave_recogidaNivel2:
        PANTALLA.blit(llave2_img, (150, 590))

#---------------(End)Nivel 2-----------------------#

#---------------(Inicio)Nivel 3---------------------#

#Donde aparece la puerta
puerta3_x = 600
puerta3_y = 50

#Cargar la imagen de la llave, scalarla y rodearla con un rectángulo(Esto último se hace en la función que la dibuja.
#Donde aparece la llave.
llave3_img = pygame.image.load("imagenes/Key/key3.png")
llave3_img = pygame.transform.scale(llave3_img, (30, 45))
llave3_rect = llave2_img.get_rect()
llave3_rect.x = 250
llave3_rect.y = 50

# Cargar la imagen de la puerta, scalarla y rodearla con un rectángulo(Igual, se hace en la función).
puerta3_img = pygame.image.load("imagenes/Door/door sprite.png")
puerta3_img = pygame.transform.scale(puerta3_img,(50,50))
puerta3_rect = puerta3_img.get_rect(topleft=(puerta3_x, puerta3_y))

# Por defecto, ya que está escondida en un bloque
llave_recogidaNivel3 = False

# La puerta se mantiene cerrada hasta que el jugador se acerca con la llave en el inventario
puerta_abiertaNivel3 = False

# Variable para mantener registro de si ya se ha detectado una colisión, se mantiene en False, porque si no cerraria la función
#apenas se iniciara el bucle.
colision_detectada_PuertaNivel3 = False

# Función encargada de verificar la colisión con la puerta y la llave
def detectar_colisionPuertaNivel3(px, py):
    global llave_recogidaNivel3, nivel, ejecuta, colision_detectada_PuertaNivel3

    # Verificar si ya se ha detectado una colisión si es así, cierra la función para que se deje de dibujar la puerta
    if colision_detectada_PuertaNivel3:
        return
    # Verificar si el jugador está completamente dentro de los límites de la llave
    if not llave_recogidaNivel3 and llave3_rect.collidepoint(px, py):
        llave_recogidaNivel3 = True
        print("¡Has recogido la llave Nivel 3!")

    # Detectar colisión con la puerta niel 2
    if puerta3_rect.colliderect(pygame.Rect(px, py, 35, 35)):
        if llave_recogidaNivel3:
            nivel += 1
            print("¡Has abierto la puerta del Nivel2! Ahora estás en el nivel 3")
            colision_detectada_PuertaNivel3 = True  # Marcar que se ha detectado una colisión
            return

#Cambiar la posición de la llave y la puerta
def renderizar_elementosPuertaNivel3():
    global puerta_abiertaNivel3

    # Renderizar la llave si no ha sido recogida
    if not llave_recogidaNivel3:
        #Rectangulo que rodea la llave para el nivel 2, la idea es que una vez se recoja la llave, este rectangulo la tape.
        pygame.draw.rect(PANTALLA, verde, (llave3_rect.x, llave3_rect.y,45,45))
        PANTALLA.blit(llave3_img, llave3_rect)
    #Si la llave fué recogida, entonces dibujela en el inventario
    elif llave_recogidaNivel3:
        PANTALLA.blit(llave3_img, (150, 590))

#---------------(End)Nivel 3------------------------#

#----------------------------Creación de la llave y la puerta para saltar a otros niveles(end)---------------------------------#

#----------------0--------------0-------------0-----------(Inicio)bomba y los rangos de explosion------------------0------------------0-------------------0---

#Lista de posiciones de los muros DESTRUCTIBLES(Si se puede, destruir pero no pasar por encima):
muros_destructibles_posiciones = [
    #Antes de linea #1:
    (0,50),
    (250,50),
    #linea #1
    (450,50),
    (0, 100),
    (0, 150),
    
    (150,150),
    (200,250),
    (250,250),
    (250,150),
    #Linea 3
    (500,300),
    #Debajo de Linea 3
    (400,350),
    (250,350),
    (200,350),
    (400,100),
    (400,150),
    
]

muros_destructibles_posicionesNivel2 = [
    #Antes de linea #1:
    (0,50),
    (250,50),
    #linea #1
    (450,50),
    (0, 100),
    (0, 150),
    
    (150,150),
    (200,250),
    (250,250),
    (250,150),
    #Linea 3
    (500,300),
    #Debajo de Linea 3
    (400,350),
    (250,350),
    (200,350),
    (400,100),
    (400,150),
    
]

muros_destructibles_posicionesNivel3 = [
    #Antes de linea #1:
    (0,50),
    (250,50),
    #linea #1
    (450,50),
    (0, 100),
    (0, 150),
    
    (150,150),
    (200,250),
    (250,250),
    (250,150),
    #Linea 3
    (500,300),
    #Debajo de Linea 3
    (400,350),
    (250,350),
    (200,350),
    (400,100),
    (400,150),
    
]

#Lista de posiciones de los muros indestructibles(No se puede destruir ni pasar por encima)
muros_Indestructibles_posiciones = [ 
    #Encima de linea 1
    (200,50),
    (400,50),
    #Linea 1   
    (50, 100),
    (150, 100),
    (250, 100),
    (350, 100),
    (450, 100),
    (550, 100),
    #Linea 2
    (50, 200),
    (150, 200),
    (250, 200),
    (350, 200),
    (450, 200),
    (550, 200),
    (500,200),
    #Encima de linea 3
    (350,150),
    #Linea 3
    (50, 300),
    (150,300),
    (250,300),
    (300,300),
    (350,300),
    (450,300),
    (550,300),
    (600,300),
    #Debajo linea 3
    (300,350),
    #Encima de linea 4
    (100,350),
    #Linea 4
    (50, 400),
    (150, 400),
    (250, 400),
    (350, 400),
    (450, 400),
    (550, 400),

    #Linea debajo de 4
    (50,450),
    (500,450),
]

#CANTIDAD máxima de bombas Nivel 1:
bombas_disponibles = 25
bombas_disponiblesNivel2 = 20
bombas_disponiblesNivel3 = 24

# Función para dibujar el contador de bombas disponibles en la pantalla
def dibujar_contador_bombas():
    if nivel == 1:
        font = pygame.font.Font(None, 30)
        texto = font.render("Bombas disponibles: " + str(bombas_disponibles), True, negro)
        PANTALLA.blit(texto, (350, 580))
    
    if nivel == 2:
        font = pygame.font.Font(None, 30)
        texto = font.render("Bombas disponibles: " + str(bombas_disponiblesNivel2), True, negro)
        PANTALLA.blit(texto, (350, 580))
    
    if nivel == 3:
        font = pygame.font.Font(None, 30)
        texto = font.render("Bombas disponibles: " + str(bombas_disponiblesNivel3), True, negro)
        PANTALLA.blit(texto, (350, 580))

#Tiempo de vida de la bomba, antes, durante y después de explotar.(Tiempo que tiene para estar en el campo de juego antes de explotar)
def bomb_exploded(bomb):
    current_time = pygame.time.get_ticks()
    return current_time - bomb["Tiempo que dura la bomba en juego"] >= 3000

#Función auxiliar/recursiva de explosion bomba (Rango de explosión y demás)
def detectar_colision_bomba_bloque(bomba_x, bomba_y, bloques, rango_colision=40):
    if not bloques:
        return bloques  # Caso base: si no hay bloques, devuelve la lista original
        
    # Extraer las coordenadas del primer bloque de la lista
    bloque_x, bloque_y = bloques[0]
    
    # Calcular el centro del bloque
    centro_bloque_x = bloque_x + 20  # Ajustar según el tamaño de los bloques
    centro_bloque_y = bloque_y + 20  # Ajustar según el tamaño de los bloques
    
    # Verificar si la bomba está dentro del rango de colisión del bloque
    #El \ se utiliza para ignorar el centro de linea y continuar lyendo incluso una linea abajo.
    if (abs(centro_bloque_x - bomba_x) <= rango_colision and abs(centro_bloque_y - bomba_y) <= rango_colision) \
    or (abs(centro_bloque_x - bomba_x) <= rango_colision and abs(centro_bloque_y - (bomba_y + 40)) <= rango_colision) \
    or (abs(centro_bloque_x - bomba_x) <= rango_colision and abs(centro_bloque_y - (bomba_y - 40)) <= rango_colision) \
    or (abs(centro_bloque_x - (bomba_x + 40)) <= rango_colision and abs(centro_bloque_y - bomba_y) <= rango_colision) \
    or (abs(centro_bloque_x - (bomba_x - 40)) <= rango_colision and abs(centro_bloque_y - bomba_y) <= rango_colision):
        # Si la bomba está dentro del rango de colisión, eliminar el bloque de la lista
        return bloques[1:]
    else:
        # Si la bomba no está dentro del rango de colisión, mantener el bloque en la lista
        return [bloques[0]] + detectar_colision_bomba_bloque(bomba_x, bomba_y, bloques[1:], rango_colision)


#------------Estas variables se ponen encima de la función ya que sino, no las toma en cuenta---
#Vida del personaje Se define acá para poder pasarla a la función explosion_bomba
vida_personaje = 100
#Variable puntos(Va almacenando los puntos trás cada colision y la función dibujadora se encarga de enseñarla en pantalla) 
#Además define el valor incial de los puntos.
puntos = 0

#Vida del duende morado:
vida_DuendeMorado = 50
#Variable del duende verde 
vida_DuendeVerde = 50
#Vida del duende verde Vertical
vida_DuendeVerdeVertical = 50
# Variable para controlar si el duende morado está vivo o muerto
duende_morado_vivo = True
duende_verde_vivo = True
duende_verdeVertical_vivo = True
#-----------------------------------------------------------------------------------------------

#Función principal de detectar_colision_bomba_bloque, actualiza los bloques cada que una bomba explota
def explosion_bomba(bombs, indice=0): 
    global muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3,vida_personaje,vida_DuendeMorado,duende_morado_vivo,vida_DuendeVerde,duende_verde_vivo,duende_verdeVertical_vivo, vida_DuendeVerdeVertical #Se define la lista de muros de forma global para que esta fución pueda leerla
    if indice >= len(bombs):
        return  # Caso base: todas las bombas han explotado

    #Extrae las coords de las bombas almacenadas en la lista bombs, es decir cuando se le dió espacio, guardó las coordenadas de donde quedó.
    #Esto se ve en la función principal del bucle del juego "manejar evento()"
    bomb = bombs[indice]
    bomb_x, bomb_y = bomb["x"], bomb["y"]
    
    # Verificar si la bomba ha explotado con los ticks del juego, a lo Minecraft.
    if bomb_exploded(bomb):

        if abs(px - bomb_x) <= 40 and abs(py - bomb_y) <= 40:
            # Si el personaje está en el rango de la explosión, reducir su vida.
            vida_personaje -= 5
            print("¡La bomba ha explotado y has perdido 5 puntos de vida!")

        #Si una bomba explota a la par del duende morado, le baja vida, cuando llega a 0, muere(se frena la función de 
        # dibujado, y desaparece)
        if (duende_morado_x1 - bomb_x) <= 40 and abs(duende_morado_y1 - bomb_y) <= 40  and nivel == 3:
            # Si el personaje está en el rango del duende, reducir su vida
            vida_DuendeMorado -= 10
            print("Poner sonido de muerte del duende")
            if vida_DuendeMorado <= 0:
                duende_morado_vivo = False
        
        if (duendeVerde_x1 - bomb_x) <= 40 and abs(duendeVerde_y1 - bomb_y) <= 40 and nivel == 2:
            # Si el personaje está en el rango del duende, reducir su vida
            vida_DuendeVerde -= 10
            print("Poner sonido de muerte del duende")
            if vida_DuendeVerde <= 0:
                vida_DuendeVerde = False
        
        if (duendeVerdeVertical_x1 - bomb_x) <= 40 and abs(duendeVerdeVertical_y1 - bomb_y) <= 40  and nivel == 3:
            # Si el personaje está en el rango del duende, reducir su vida
            vida_DuendeVerdeVertical -= 10
            print("Poner sonido de muerte del duende")
            if vida_DuendeVerdeVertical <= 0:
                vida_DuendeVerdeVertical = False

        # Actualizar la lista de bloques destructibles tras cada explosion, limita los argumentos dependiendo el nivel para quue la 
        # función de detección no se bugue al recibir 3 listas al mismo tiempo.
        muros_destructibles_posiciones = detectar_colision_bomba_bloque(bomb_x, bomb_y, muros_destructibles_posiciones)
        if nivel == 2:
            muros_destructibles_posicionesNivel2 = detectar_colision_bomba_bloque(bomb_x, bomb_y, muros_destructibles_posicionesNivel2)
        if nivel == 3:
            muros_destructibles_posicionesNivel3 = detectar_colision_bomba_bloque(bomb_x, bomb_y, muros_destructibles_posicionesNivel3)
    
    # Llamada recursiva para movernos hacia la siguiente bomba en la lista
    explosion_bomba(bombs, indice + 1)


#----------------0--------------0-------------0-----------(End)bomba y los rangos de explosion------------------0------------------0-------------------0---

#---------------------------------------------------Cargando imagenes de bombas Y sector Lógica de explosiones(incio)---------------------------------------------------------------#

#Se cambió el tamaño de algunas imagenes para que la explosión se vea más grande que la bomba
bomb_images = [
    pygame.transform.scale(pygame.image.load("Imagenes/Bombas/1.png"), (25, 25)),
    pygame.transform.scale(pygame.image.load("Imagenes/Bombas/2.png"), (25, 25)),
    pygame.transform.scale(pygame.image.load("Imagenes/Bombas/3.png"), (25, 25)),
    pygame.transform.scale(pygame.image.load("Imagenes/Bombas/4.png"), (80, 80)),
    pygame.transform.scale(pygame.image.load("Imagenes/Bombas/5.png"), (65, 65)),
    pygame.transform.scale(pygame.image.load("Imagenes/Bombas/6.png"), (35, 35)),
]

# Lista para almacenar las bombas colocadas
bombs = []

#Animación de la bomba cuando explota: 
def animacion_bombas(bombs, indice=0):
    if indice >= len(bombs):
        return  # Caso base: todas las bombas han explotado
    
    bomb = bombs[indice]
    bomb_image = bomb_images[bomb["Indice de la imagen(posición en la lista)"]] #Es decir, que imagen se va a poner de las 6 que hay en la lista
    PANTALLA.blit(bomb_image, (bomb["x"], bomb["y"]+20)) #Ajustamos que aparezca un poco más abajo, ya que aparecía encima de los bloques

    current_time = pygame.time.get_ticks()
    if current_time - bomb["Tiempo que dura la bomba en juego"] >= 3000:
        bomb["Indice de la imagen(posición en la lista)"] += 1
        if bomb["Indice de la imagen(posición en la lista)"] >= len(bomb_images):
            # Si la bomba ha alcanzado la última imagen, eliminarla de la lista de bombas almacenadas
            bombs.pop(indice)
            # Llamada recursiva sin incrementar el índice, ya que se ha eliminado una bomba
            animacion_bombas(bombs, indice)
    else:
        # Llamada recursiva para manejar la siguiente bomba en la lista
        animacion_bombas(bombs, indice + 1)

#---------------------------------------------------Cargando imagenes de bombas Y sector Lógica de explosiones(end)---------------------------------------------------------------#

#------------------------------------------------------------Movimiento de personaje(Incio)-----------------------------------------------#
#Diccionario de skins, cuando el jugador selecciona uno de los botones la skin actual se toma de acá
skins = {
    1: {
        "quieto": [
            pygame.image.load("Imagenes/Player/Quieto/quieto.png")
            ],
        "up": [
            pygame.image.load("Imagenes/Player/Up/Up1.png"),
            pygame.image.load("Imagenes/Player/Up/Up2.png"),
            pygame.image.load("Imagenes/Player/Up/Up3.png"),
            pygame.image.load("Imagenes/Player/Up/Up4.png"),
            pygame.image.load("Imagenes/Player/Up/Up5.png"),
            pygame.image.load("Imagenes/Player/Up/Up6.png"),
            pygame.image.load("Imagenes/Player/Up/Up7.png"),
        ],
        "down": [
            pygame.image.load("Imagenes/Player/Down/Down1.png"),
            pygame.image.load("Imagenes/Player/Down/Down2.png"),
            pygame.image.load("Imagenes/Player/Down/Down3.png"),
            pygame.image.load("Imagenes/Player/Down/Down4.png"),
            pygame.image.load("Imagenes/Player/Down/Down5.png"),
            pygame.image.load("Imagenes/Player/Down/Down6.png"),
            pygame.image.load("Imagenes/Player/Down/Down7.png"),
        ],
        "right": [
            pygame.image.load("Imagenes/Player/right/right1.png"),
            pygame.image.load("Imagenes/Player/right/right2.png"),
            pygame.image.load("Imagenes/Player/right/right3.png"),
            pygame.image.load("Imagenes/Player/right/right4.png"),
            pygame.image.load("Imagenes/Player/right/right5.png"),
            pygame.image.load("Imagenes/Player/right/right6.png"),
            pygame.image.load("Imagenes/Player/right/right7.png"),
            
        ],
        "left": [
            pygame.image.load("Imagenes/Player/Left/left1.png"),
            pygame.image.load("Imagenes/Player/Left/left2.png"),
            pygame.image.load("Imagenes/Player/Left/left3.png"),
            pygame.image.load("Imagenes/Player/Left/left4.png"),
            pygame.image.load("Imagenes/Player/Left/left5.png"),
            pygame.image.load("Imagenes/Player/Left/left6.png"),
            pygame.image.load("Imagenes/Player/Left/left7.png"),
            
        ],
    },
    2: {
        "quieto" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Quieto/Quieto.png"), (40,40))
            ],
        "up": [
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Up/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Up/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Up/3.png"), (40,40)),
        ],
        "down" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Down/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Down/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Down/3.png"), (40,40)),
        ],
        "right" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Right/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Right/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Right/3.png"), (40,40)),
        ],
        "left" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Left/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Left/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player2/Left/3.png"), (40,40)),
        ]
    },
    3: {
        "quieto" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/quieto.png"), (40,40))
            ],
        "up": [
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/3.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/4.png"), (40,40)),
        ],
        "down" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/3.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/4.png"), (40,40)),
        ],
        "right" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/3.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Derecha/4.png"), (40,40)),
        ],
        "left" : [
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/1.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/2.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/3.png"), (40,40)),
            pygame.transform.scale(pygame.image.load("Imagenes/Player3/Izquierda/4.png"), (40,40))
        ]
    }
}

# Velocidad a la que se mueve el personaje
velocidad = 11

#------------------ Movimiento de los enemigos(Skins)"Inicio" ---------------#
# Variable del movimiento enemigo duende morado (Quieto)
quietoDuendeMorado = pygame.image.load("Imagenes/Enemigos/DuendeMorado/Quieto/Quieto.png")
# Camina hacía arriba
CaminaHaciaArribaDuendeMorado = [pygame.image.load("Imagenes/Enemigos/DuendeMorado/Up/1.png"),
                                pygame.image.load("Imagenes/Enemigos/DuendeMorado/Up/2.png"),
                                pygame.image.load("Imagenes/Enemigos/DuendeMorado/Up/3.png")]
# Camina hacía abajo
CaminaHaciaAbajoDuendeMorado = [pygame.image.load("Imagenes/Enemigos/DuendeMorado/Down/1.png"),
                                pygame.image.load("Imagenes/Enemigos/DuendeMorado/Down/2.png"),
                                pygame.image.load("Imagenes/Enemigos/DuendeMorado/Down/3.png")]


#-----------------para el duende 2-----------------
# Variable del movimiento enemigo duende morado (Quieto)
quietoDuendeVerde = pygame.image.load("Imagenes/Enemigos/DuendeVerde/Quieto/Quieto.png")
# Camina hacía arriba
CaminaHaciaderechaDuendeVerde  = [pygame.image.load("Imagenes/Enemigos/DuendeVerde/Right/1.png"),
                                pygame.image.load("Imagenes/Enemigos/DuendeVerde/Right/2.png"),
                                pygame.image.load("Imagenes/Enemigos/DuendeVerde/Right/3.png"),
                                ]
# Camina hacía abajo
CaminaHaciaizquerdaDuendeVerde = [  pygame.image.load("Imagenes/Enemigos/DuendeVerde/Left/1.png"),
                                    pygame.image.load("Imagenes/Enemigos/DuendeVerde/Left/2.png"),
                                    pygame.image.load("Imagenes/Enemigos/DuendeVerde/Left/3.png"),
                                ]

CaminaHaciaArribaDuendeVerde = [
        pygame.image.load("Imagenes/Enemigos/DuendeVerde/Up/1.png"),
        pygame.image.load("Imagenes/Enemigos/DuendeVerde/Up/2.png"),
        pygame.image.load("Imagenes/Enemigos/DuendeVerde/Up/3.png"),
]

CaminaHaciaAbajoDuendeVerde = [ 
        pygame.image.load("Imagenes/Enemigos/DuendeVerde/Abajo/1.png"),
        pygame.image.load("Imagenes/Enemigos/DuendeVerde/Abajo/2.png"),
        pygame.image.load("Imagenes/Enemigos/DuendeVerde/Abajo/3.png"),
]

# Velocidad a la que se mueve el enemigo Verde
velocidadDuendeVerde = 2
# Velocidad a la que se mueve el enemigo Morado
velocidadDuendeMorado = 2
# Velocidad a la que se mueve el enemigo Verde Vertical
velocidadDuendeVerde_Vertical = 2

#-----------------para el duende 2-----------------

# Coordenadas iniciales del enemigo duende morado
duende_morado_x1 = 300
duende_morado_y1 = 280

duendeVerde_x1 = 100
duendeVerde_y1 = 450

# Índice de la imagen actual para la animación del duende
indice_animacion_duende_morado = 0

# Índice de la imagen actual para la animación del duende
indice_animacion_duende_Verde = 0

# Variable para controlar el movimiento inicial del duende morado
duende_morado_movimiento = "arriba"  # Movimiento inicial del duende morado

duende_verde_movimiento = "derecha"

# Función para actualizar la posición del duende morado según el ciclo de movimiento predefinido
def actualizar_posicion_duende_morado():
    global duende_morado_x1, duende_morado_y1, vida_personaje, vida_DuendeMorado, duende_morado_movimiento

    # Verificar si estamos en el nivel 2 para agregar duendes morados
    if vida_DuendeMorado > 0:
        # Actualizar la posición del duende morado según su dirección de movimiento y velocidad
        if duende_morado_movimiento == "abajo":
            duende_morado_y1 += velocidadDuendeMorado
        elif duende_morado_movimiento == "arriba":
            duende_morado_y1 -= velocidadDuendeMorado
        # Cambiar la dirección del duende morado cuando alcanza ciertos límites
        if duende_morado_y1 >= 280:
            duende_morado_movimiento = "arriba"
        elif duende_morado_y1 <= 50:
            duende_morado_movimiento = "abajo"
        
        if abs(px - duende_morado_x1) <= 40 and abs(py - duende_morado_y1) <= 40:
            # Si el personaje está en el rango del duende, reducir su vida
            vida_personaje -= 2
            print("¡Duende!")
    else:
        vida_DuendeMorado = False

# Función para dibujar todos los duendes morados en sus posiciones actuales
def dibujar_duende_morado():
    global duende_morado_x1,duende_morado_y1, indice_animacion_duende_morado 

    # Verificar si estamos en el nivel 2 para dibujar duendes morados
    # Obtener la imagen correspondiente al movimiento actual del duende morado
    imagen = None
    if duende_morado_movimiento == "arriba":
        imagen = CaminaHaciaArribaDuendeMorado[indice_animacion_duende_morado]
    elif duende_morado_movimiento == "abajo":
        imagen = CaminaHaciaAbajoDuendeMorado[indice_animacion_duende_morado]
    # Escalamos la imagen del duende
    imagen_redimensionada = pygame.transform.scale(imagen, (40, 40))
    # Dibujar al duende morado en su posición actual
    PANTALLA.blit(imagen_redimensionada, (duende_morado_x1, duende_morado_y1))
    # Incrementar el índice de la animación para la próxima imagen
    indice_animacion_duende_morado = (indice_animacion_duende_morado + 1) % len(CaminaHaciaArribaDuendeMorado)

##------------------ Movimiento de los enemigo #2(Skins)"End" ---------------#

def actualizar_posicion_duende_Verde():
    global duendeVerde_x1, duendeVerde_y1, vida_personaje, vida_DuendeVerde, duende_verde_movimiento
    # Verificar si estamos en el nivel 2 para agregar duende
    if vida_DuendeVerde > 0:
            # Actualizar la posición del duende morado según su dirección de movimiento y velocidad
        if duende_verde_movimiento == "derecha":
            duendeVerde_x1 += velocidadDuendeVerde
            # Cambiar la dirección del duende morado cuando alcanza ciertos límites
            if duendeVerde_x1 >= 400:
                duende_verde_movimiento = "izquierda"
        elif duende_verde_movimiento == "izquierda":
            duendeVerde_x1 -= velocidadDuendeVerde
            # Cambiar la dirección del duende morado cuando alcanza ciertos límites
            if duendeVerde_x1 <= 100:  # Define tus propios límites horizontales
                duende_verde_movimiento = "derecha"
        if abs(px - duendeVerde_x1) <= 40 and abs(py - duendeVerde_y1) <= 40:
            # Si el personaje está en el rango del duende, reducir su vida
            vida_personaje -= 2
            print("¡Duende!")
    else:
        vida_DuendeVerde = False

# Función para dibujar todos los duendes morados en sus posiciones actuales
def dibujar_duende_Verde():
    global duendeVerde_x1, duendeVerde_y1, indice_animacion_duende_Verde
        # Verificar si estamos en el nivel 2 para dibujar duendes morados
        # Obtener la imagen correspondiente al movimiento actual del duende morado
    imagen = None
    if duende_verde_movimiento == "derecha":
        imagen = CaminaHaciaderechaDuendeVerde[indice_animacion_duende_Verde]
    elif duende_verde_movimiento == "izquierda":
        imagen = CaminaHaciaizquerdaDuendeVerde[indice_animacion_duende_Verde]
    # Escalamos la imagen del duende
    imagen_redimensionada = pygame.transform.scale(imagen, (40, 40))
    # Dibujar al duende morado en su posición actual
    PANTALLA.blit(imagen_redimensionada, (duendeVerde_x1, duendeVerde_y1))
    # Incrementar el índice de la animación para la próxima imagen
    indice_animacion_duende_Verde = (indice_animacion_duende_Verde + 1) % len(CaminaHaciaderechaDuendeVerde)    


#------------------ Movimiento del enemigo #2(Skins)"End" ---------------#
#------------------ Movimeinto del enemigo #3(Inicio)(Duende verde repetido pero con movimiento hacia arriba)---------------------------#
# Coordenadas iniciales del enemigo duende morado
duendeVerdeVertical_x1 = 600
duendeVerdeVertical_y1 = 280

# Índice de la imagen actual para la animación del duende
indice_animacion_duende_VerdeVertical = 0
duende_verdeVertical_movimiento = "Arriba"

def actualizar_posicion_duende_VerdeVertical():
    global duendeVerdeVertical_x1, duendeVerdeVertical_y1, vida_personaje, vida_DuendeVerdeVertical, duende_verdeVertical_movimiento

    # Verificar si estamos en el nivel 2 para agregar duendes morados
    if vida_DuendeVerdeVertical > 0:
        # Actualizar la posición del duende morado según su dirección de movimiento y velocidad
        if duende_verdeVertical_movimiento == "abajo":
            duendeVerdeVertical_y1 += velocidadDuendeVerde_Vertical
        elif duende_verdeVertical_movimiento == "arriba":
            duendeVerdeVertical_y1 -= velocidadDuendeVerde_Vertical
        # Cambiar la dirección del duende morado cuando alcanza ciertos límites
        if duendeVerdeVertical_y1 >= 260:
            duende_verdeVertical_movimiento = "arriba"
        elif duendeVerdeVertical_y1 <= 100:
            duende_verdeVertical_movimiento = "abajo"
        
        if abs(px - duendeVerdeVertical_x1) <= 40 and abs(py - duendeVerdeVertical_y1) <= 40:
            # Si el personaje está en el rango del duende, reducir su vida
            vida_personaje -= 2
            print("¡Duende!")
    else:
        vida_DuendeVerdeVertical = False

def dibujar_duende_VerdeVertical():
    global duendeVerdeVertical_x1, duendeVerdeVertical_y1, indice_animacion_duende_VerdeVertical

    imagenVertical = None
    if duende_verdeVertical_movimiento == "arriba":
        imagenVertical = CaminaHaciaArribaDuendeVerde[indice_animacion_duende_VerdeVertical]
    elif duende_verdeVertical_movimiento == "abajo":
        imagenVertical = CaminaHaciaAbajoDuendeVerde[indice_animacion_duende_VerdeVertical]
    
    imagen_redimensionadaVertical = pygame.transform.scale(imagenVertical,(40,40))
    PANTALLA.blit(imagen_redimensionadaVertical,(duendeVerdeVertical_x1,duendeVerdeVertical_y1))

    indice_animacion_duende_VerdeVertical = (indice_animacion_duende_VerdeVertical + 1) % len(CaminaHaciaArribaDuendeVerde)
    

#------------------ Movimeinto del enemigo #3(End)(Duende verde repetido pero con movimiento hacia arriba)---------------------------#
#------------------ Movimiento de los enemigos(Skins)"End" ---------------#

#------------------ Función de Movimiento del personaje y Refrescar de los elementos"Inicio" ---------------#
# Variables de dirección para que no se vaya el personaje solo
arriba = False
abajo = False
derecha = False
izquierda = False

#Variables en cero para empezar a contar e ir cambiando la imagen del jugador:
cuentaPasosUP = 0
cuentaPasosDown = 0
cuentaPasosLeft = 0
cuentaPasosRight = 0

#Lógica de la animación del personaje, va eliminando las imagenes hasta que llega a la final y vuelve a repetir
def MovimientopersonajeJugable():
    global cuentaPasosDown, cuentaPasosLeft, cuentaPasosRight, cuentaPasosUP
    # Lo que hace es ir aumentando el índice de la imagen asociado al movimiento, al aumentar el índice este va cambiando las imágenes.

    #La Skin es basicamente que numero"LLave" del diccionario se seleccionó.
    skin = skins[skin_seleccionada]

    # Verificar límites de los contadores de pasos y reiniciar cuando se llegó al final de la lista(Para dar animación a la skin actual)
    if cuentaPasosUP + 1 >= len(skin["up"]):
        cuentaPasosUP = 0
    
    if cuentaPasosDown + 1 >= len(skin["down"]):
        cuentaPasosDown = 0
    
    if cuentaPasosLeft + 1 >= len(skin["left"]):
        cuentaPasosLeft = 0
    
    if cuentaPasosRight + 1 >= len(skin["right"]):
        cuentaPasosRight = 0
    
    # Dibujar el personaje dependiendo de la dirección del movimiento y el número(llave) del diccionario
    if abajo:
        PANTALLA.blit(skin["down"][cuentaPasosDown], (px, py))
        cuentaPasosDown += 1
    elif arriba:
        PANTALLA.blit(skin["up"][cuentaPasosUP], (px, py))
        cuentaPasosUP += 1
    elif derecha:
        PANTALLA.blit(skin["right"][cuentaPasosRight], (px, py))
        cuentaPasosRight += 1
    elif izquierda:
        PANTALLA.blit(skin["left"][cuentaPasosLeft], (px, py))
        cuentaPasosLeft += 1
    else:
        # Si el personaje no se mueve, mostrar la imagen de "quieto"
        PANTALLA.blit(skin["quieto"][0], (px, py))
    

    #Actualizar la ventana a cada rato para que se refresque el movimiento(cada vez que se llama a RefreshPlayer)
    #Se podría poner directamente en el bucle del juego, pero acá hace 2x1 cuando se llama esta función al bucle del juego
    pygame.display.update()
#------------------ Función de Movimiento del personaje y Refrescar de los elementos"End" ---------------#


#------------------------------------------RECURSIVIDAD(Bucle del juego)"Inicio"------------------------------------------#

#Creamos una función recursiva que controle las coliciones, toma las coordenadas X y Y además la lista de coodenadas de los bloques, 
def check_collision(x, y, muros_Indestructibles_posiciones, muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3):
    if not muros_Indestructibles_posiciones and not muros_destructibles_posiciones and not muros_destructibles_posicionesNivel2 and not muros_destructibles_posicionesNivel3:
        # Si no quedan muros ni bloques destructibles por verificar, retornar False
        return False

    if muros_Indestructibles_posiciones:
        # Verificar colisión con muros
        muro_x, muro_y = muros_Indestructibles_posiciones[0]
        if x < muro_x + 46 and x + 32 > muro_x and y + 45 > muro_y and y < muro_y + 20:
            return True
    
    if muros_destructibles_posiciones: #Se agregó esta parte cuando se incluyeron los bloques que si se pueden destruir
        # Verificar colisión con bloques destructibles
        muro_x, muro_y = muros_destructibles_posiciones[0]
        if x < muro_x + 46 and x + 32 > muro_x and y + 45 > muro_y and y < muro_y + 20:
            return True
    
    if nivel == 2:
        if muros_destructibles_posicionesNivel2: #Se agregó esta parte cuando se incluyeron los bloques que si se pueden destruir
            # Verificar colisión con bloques destructibles
            muro_x, muro_y = muros_destructibles_posicionesNivel2[0]
            if x < muro_x + 46 and x + 32 > muro_x and y + 45 > muro_y and y < muro_y + 20:
                return True
    
    if nivel == 3:
        if muros_destructibles_posicionesNivel3: #Se agregó esta parte cuando se incluyeron los bloques que si se pueden destruir
            # Verificar colisión con bloques destructibles
            muro_x, muro_y = muros_destructibles_posicionesNivel3[0]
            if x < muro_x + 46 and x + 32 > muro_x and y + 45 > muro_y and y < muro_y + 20:
                return True

    # Llamada recursiva para comprobar la colisión con el resto de muros y bloques destructibles
    return check_collision(x, y, muros_Indestructibles_posiciones[1:], muros_destructibles_posiciones[1:],muros_destructibles_posicionesNivel2[1:],muros_destructibles_posicionesNivel3[1:])

#------------------------------(Start)(Función que dibuja la Pantalla Final)---------------------------


#------------------------------(End)(Función que dibuja la Pantalla Final)---------------------------

# Variable global para controlar la ejecución del juego True = Se mantiene, False = Se cierra
ejecuta = True #----> Básicamente lo que mantiene encendida esta máquina, como la primera combustión de un carro, que mantiene encendido su motor hasta que se apaga.
def manejar_evento():
    global ejecuta,bombas_disponibles,bombas_disponiblesNivel2,bombas_disponiblesNivel3,llave_recogidaNivel1

    # Manejar un solo evento
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        ejecuta = False  # Cuando se cierra la ventana desde la X
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Colocar una bomba en la posición actual del jugador y guardar las coords para que luego la bomba tenga donde plantarse y
            # luego comparar esas coords con los bloques.
            if nivel == 1: #Estos condicionales están conectados indirectamente con el contador de bombas, ya que el mismo muestra
                            #cuentas bombas quedan disponibles en pantalla segun el nivel.
                #Variable #1 de bombas
                if bombas_disponibles > 0:
                    nueva_bomba = {"x": px, "y": py, "Indice de la imagen(posición en la lista)": 0, "Tiempo que dura la bomba en juego": pygame.time.get_ticks()}
                    bombs.append(nueva_bomba)
                    bombas_disponibles = bombas_disponibles -1
                else:
                    mensaje = fuente.render("Ya no hay bombas disponibles", True, negro, blanco)
                    PANTALLA.blit(mensaje, (W // 2 - mensaje.get_width() // 2, H // 2 - mensaje.get_height() // 2))
                    pygame.display.update()  # Actualizar la pantalla para mostrar el mensaje
                    pygame.time.delay(1200)  # Esperar 1.5 segundos antes de borrar el mensaje
                    PANTALLA.fill(verde)  # Volver a llenar la pantalla para borrar el mensaje
            
            if nivel == 2:
                #Variable #2 de bombas
                if bombas_disponiblesNivel2 > 0:
                    nueva_bomba = {"x": px, "y": py, "Indice de la imagen(posición en la lista)": 0, "Tiempo que dura la bomba en juego": pygame.time.get_ticks()}
                    bombs.append(nueva_bomba)
                    bombas_disponiblesNivel2 = bombas_disponiblesNivel2 -1
                else:
                    mensaje = fuente.render("Ya no hay bombas disponibles", True, negro, blanco)
                    PANTALLA.blit(mensaje, (W // 2 - mensaje.get_width() // 2, H // 2 - mensaje.get_height() // 2))
                    pygame.display.update()  # Actualizar la pantalla para mostrar el mensaje
                    pygame.time.delay(1200)  # Esperar 1.5 segundos antes de borrar el mensaje
                    PANTALLA.fill(verde)  # Volver a llenar la pantalla para borrar el mensaje
            
            if nivel == 3:
                #Variable #3 de bombas
                if bombas_disponiblesNivel3 > 0:
                    nueva_bomba = {"x": px, "y": py, "Indice de la imagen(posición en la lista)": 0, "Tiempo que dura la bomba en juego": pygame.time.get_ticks()}
                    bombs.append(nueva_bomba)
                    bombas_disponiblesNivel3 = bombas_disponiblesNivel3 -1
                else:
                    mensaje = fuente.render("Ya no hay bombas disponibles", True, negro, blanco)
                    PANTALLA.blit(mensaje, (W // 2 - mensaje.get_width() // 2, H // 2 - mensaje.get_height() // 2))
                    pygame.display.update()  # Actualizar la pantalla para mostrar el mensaje
                    pygame.time.delay(1200)  # Esperar 1.5 segundos antes de borrar el mensaje
                    PANTALLA.fill(verde)  # Volver a llenar la pantalla para borrar el mensaje

# Cronómetro
inicio_tiempo = pygame.time.get_ticks()  # Obtener el tiempo inicial
# Variable para controlar si la puntuación ya se agregó al archivo
puntuacion_agregada = False

#Bucle principal
def bucle_principal():
    #Se definen las variables de forma global para poder utilizarlas en el resto de la función
    global ejecuta, px, py, abajo, arriba, izquierda, derecha, muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3,duende_verde_vivo,listaPosicionesPuntos, puntos,listaPosicionesPuntosNivel2,listaPosicionesPuntosNivel3,puntuacion_agregada

    # Variable de posicionamiento(Donde spawmnea el personaje)
    px = 550
    py = 450

    while ejecuta:  # Bucle principal mientras ejecuta sea True "Ventana de juego"    

        # Verificar si la vida ha llegado a 0 o menos
        if vida_personaje <= 0:
            # Detener el bucle principal para salir del juego
            
            #Llamamos a la función que pasa los puntos al txt apenas finaliza el juego, para que así se actualice el bloc de notas
            if not puntuacion_agregada:
                # Llamar a la función para agregar puntos al archivo de puntajes
                agregar_puntos_a_txt(puntos)
                # Establecer la bandera como True para indicar que la puntuación ha sido agregada
                puntuacion_agregada = True

            # Mostrar mensaje de "Game Over"
            font = pygame.font.SysFont("Arial", 48)
            game_over_text = font.render("Game Over! You died", True, negro,blanco)
            text_rect = game_over_text.get_rect(center=(W // 2, H // 2))
            PANTALLA.blit(game_over_text, text_rect)
            pygame.display.update()

            # Pequeña pausa antes de salir del juego
            pygame.time.delay(2000)  # Pausa de 2 segundos (2000 milisegundos)

        
            # Salir del bucle principal
            return
        
        # Se llama recursivamente la función principal, es decir, mientras manejar_evento() sea True, osea, se ejecute la ventana, 
        #esta permitirá que bucle_principal siga existiendo, de ser False, la llamada recursiva no se realiza y se cierra la ventana 
        #ya que no tiene que más devolver.
        manejar_evento()
        
        # Pintar Fondo desde la paleta de colores en el inicio del código
        PANTALLA.fill(verde)

        #Dibujar la función que tiene los bordes y temporizador(y demás...)
        draw_bordes_y_temporizador()
        dibujar_contador_bombas()

        #Como lo que se llama primero se dibuja primero, llamamos primero la llave(y la puerta) para que los bloques
        #tapen la llave
        if nivel == 1:
            PANTALLA.blit(puerta_img, puerta_rect)
            detectar_colisionLlavePuertaNivel1(px,py)    
            renderizar_elementosNivel1()
        
        if nivel == 2:
            PANTALLA.blit(puerta2_img, puerta2_rect)
            detectar_colisionPuertaNivel2(px, py)
            renderizar_elementosPuertaNivel2()
        
        if nivel == 3:
            PANTALLA.blit(puerta3_img, puerta3_rect)
            detectar_colisionPuertaNivel3(px, py)
            renderizar_elementosPuertaNivel3()

        #Se llama despues de manejar_evento y antes de RefreshPlayer para que los bloques se pongan en cada llamada recursiva antes 
        #de que se actualice la pantalla.
        draw_bloques_internos(muros_Indestructibles_posiciones)

        #Se llama despues de manejar evento y antes de RefreshPlayer para llamar los bloques destructibles:
        draw_bloques_destructibles(muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3)


        #---------------------------------------------(Teclas)Movimiento y detección de coliciones"Inicio"---------------------------------------------#
        #Las teclas cuando se precionan mueve el personaje, de otra manera tendría que estarse precionando a cada rato, por eso mejor
        #manterlas precionadas.
        keys = pygame.key.get_pressed()
        # Tecla W - Movimiento hacia arriba
        if keys[pygame.K_a] and px > velocidad and not check_collision(px - velocidad, py, muros_Indestructibles_posiciones, muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3):
            px -= velocidad
            izquierda = True
            derecha = False
            arriba = False
            abajo = False
        elif keys[pygame.K_d] and px < W - 32 - velocidad and not check_collision(px + velocidad, py, muros_Indestructibles_posiciones, muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3):
            px += velocidad
            derecha = True
            izquierda = False
            arriba = False
            abajo = False
        elif keys[pygame.K_w] and py-30 > velocidad and not check_collision(px, py - velocidad, muros_Indestructibles_posiciones, muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3):
            py -= velocidad
            arriba = True
            abajo = False
            derecha = False
            izquierda = False
        elif keys[pygame.K_s] and py < 571 - 114 and not check_collision(px, py + velocidad, muros_Indestructibles_posiciones, muros_destructibles_posiciones,muros_destructibles_posicionesNivel2,muros_destructibles_posicionesNivel3):
            py += velocidad
            abajo = True
            arriba = False
            derecha = False
            izquierda = False
        else: #Si no se preciona nada, todo en Falso para que el personaje no se mueva solo
            arriba = False
            abajo = False
            derecha = False
            izquierda = False

        #---------------------------------------------(Teclas)Movimiento"End"---------------------------------------------#
        
        #-----------------Sistema de puntos(LLamadas y demás)(Inicio)--------------------------------
        
        PuntosDashboard = pygame.image.load("Imagenes/Points/PointsDashboardImage.png")
        PuntosDashboardAScale = pygame.transform.scale(PuntosDashboard,(135,60))
        PANTALLA.blit(PuntosDashboardAScale,(10,550))
        dibujar_contador_puntos()

        #En este sector dibujamos la vida en pantalla y además una decoración(marco)
        vidaDashboard = pygame.image.load("Imagenes/Health/Health Image.png")
        vidaImagen_scale = pygame.transform.scale(vidaDashboard,(135,45))
        PANTALLA.blit(vidaImagen_scale,(13,600))
        fuente = pygame.font.SysFont("Arial", 21)
        texto_vida = fuente.render(f"{vida_personaje}", True, blanco)
        PANTALLA.blit(texto_vida, (73, 610))

        if nivel == 1:
            font = pygame.font.SysFont("Arial", 28)
            texto = font.render("¡Nivel 1 de 3!", True, negro)
            text_rect = texto.get_rect(center=(250, 620)) #Situar el texto en el centro
            PANTALLA.blit(texto, text_rect)
        if nivel == 2:
            font = pygame.font.SysFont("Arial", 28)
            texto = font.render("¡Nivel 2 de 3!", True, negro)
            text_rect = texto.get_rect(center=(250, 620)) #Situar el texto en el centro
            PANTALLA.blit(texto, text_rect)
        if nivel == 3:
            font = pygame.font.SysFont("Arial", 28)
            texto = font.render("¡Nivel 3 de 3!", True, negro)
            text_rect = texto.get_rect(center=(250, 620)) #Situar el texto en el centro
            PANTALLA.blit(texto, text_rect)
        
        #Posición donde aparece
        posicion_nombre = (215, 560)
        # Fuente y tamaño de la fuente para el nombre del jugador
        font_nombre = pygame.font.SysFont("Arial", 28)
        # Renderizar el nombre del jugador
        texto_nombre = font_nombre.render(nombre_jugador, True, negro)  # nombre_jugador es la variable que contiene el nombre
        #Le damos un rectángulo
        rect_nombre = texto_nombre.get_rect()
        rect_nombre.topleft = posicion_nombre

        # Dibuja el nombre del jugador en la pantalla
        PANTALLA.blit(texto_nombre, rect_nombre)

        #Nota: El orden de llamada aquí es muy importante ya que primero verificamos coliciones y luego se actualice la lista de puntos
        # Se llama a la función que dibuja los puntos por pantalla:
        #Dibujamos las funciones de los puntos segun sea el nivel, esto se realiza bajo el mismo principio que se usó
        #para dibujar los enemigos según el nvel,
        if nivel == 1:
            listaPosicionesPuntos, puntos = detectar_colision_y_eliminar_puntos(px, py, listaPosicionesPuntos, puntos)
            #Usamos el igualado de variables(arriba), para actualizar las variables listaPosicionesPuntos y puntos con los valores 
            #devueltos por la función detectar_colision_y_eliminar_puntos.

            dibujarPuntosPantalla(listaPosicionesPuntos) #Dibujamos los puntos en pantalla
        
        if nivel == 2:#Mismo que el nivel 1, pero se utiliza la lista de puntos del nivel 2
            listaPosicionesPuntosNivel2, puntos = detectar_colision_y_eliminar_puntosNivel2(px, py, listaPosicionesPuntosNivel2, puntos)
            dibujarPuntosPantalla(listaPosicionesPuntosNivel2) #Dibujamos los puntos en pantalla

        if nivel == 3:#Mismo que los condicionales anteiores pero con la lista de puntos nivel 3.
            listaPosicionesPuntosNivel3, puntos = detectar_colision_y_eliminar_puntosNivel2(px, py, listaPosicionesPuntosNivel3, puntos)
            dibujarPuntosPantalla(listaPosicionesPuntosNivel3) #Dibujamos los puntos en pantalla
        #-----------------Sistema de puntos(LLamadas y demás)(End)--------------------------------

        #Encargada de cambiar la animación de la bomba cuando su tiempo de vida llega a ser mayor igual a 3 segundos.
        animacion_bombas(bombs)

        #Encargada de actualizar la lista de bloques trás cada explosión
        explosion_bomba(bombs)

        #----------------------Chronometro par el tiempo de partida(Inicio)----------------------------
        # Obtener el tiempo actual
        tiempo_actual = pygame.time.get_ticks()

        # Calcular la diferencia de tiempo
        tiempo_transcurrido = tiempo_actual - inicio_tiempo

        # Convertir el tiempo a segundos
        segundos = tiempo_transcurrido // 1000

        #Siempre y cuando el duende morado tenga vida mayor a 0, se seguirá dibujando en patanlla, si no, pues se
        #para la función.
        # Dibujar al duende morado si está vivo y si estamos en el nivel 1
        if duende_morado_vivo and nivel == 3:
            actualizar_posicion_duende_morado()
            dibujar_duende_morado()

        # Dibujar al duende verde si está vivo y estamos en el nivel 2
        if duende_verde_vivo and nivel == 2: #Con esto reutilizamos la función de dibujar duende verde
            actualizar_posicion_duende_Verde()
            dibujar_duende_Verde()
        
        if duende_verdeVertical_vivo and nivel == 3:
            actualizar_posicion_duende_VerdeVertical()
            dibujar_duende_VerdeVertical()
        
        # Mostrar el tiempo en la pantalla
        font = pygame.font.SysFont("Arial", 22)
        # Renderizar el texto del cronómetro
        chronometro = font.render("Tiempo transcurrido: {} segundos".format(segundos), True, negro)
        # Dibujar el texto del cronómetro en la pantalla
        PANTALLA.blit(chronometro, (350, 610))
        #----------------------Chronometro par el tiempo de partida(End)-------------------------

        if nivel == 4:
            #Llamamos a la función que pasa los puntos al txt apenas finaliza el juego, para que así se actualice el bloc de notas
            if not puntuacion_agregada:
                # Llamar a la función para agregar puntos al archivo de puntajes
                agregar_puntos_a_txt(puntos)
                # Establecer la bandera como True para indicar que la puntuación ha sido agregada
                puntuacion_agregada = True
                # Salir del bucle principal

            #Mostrar mensaje de "Felicidades, ganaste" Fin
            #Marco negro del final
            pygame.draw.rect(PANTALLA, negro, (50, 50, 540, 500), 5)
            Fondo_Gris = pygame.Surface((540, 490), pygame.SRCALPHA)  # Superficie transparente Largo, Ancho
            Fondo_Gris.fill((80, 64, 64, 128))  # Color grisáceo transparente
            PANTALLA.blit(Fondo_Gris, (50, 50)) #Donde aparece X y Y

            #Texto de ganaste:
            font = pygame.font.SysFont("Arial", 48)
            game_over_text = font.render("¡Felicidades ganaste!", True, negro,blanco)
            text_rect = game_over_text.get_rect(center=(W // 2, H // 2)) #Situar el texto en el centro
            PANTALLA.blit(game_over_text, text_rect) #Dibujar el texto con las especificaciones

            #Imagenes que acompañan el mensaje final.
            BombermanFinal = pygame.image.load("Imagenes/Imagenes de la pantalla Felicidades Ganaste/BombermanDefinitivo.png")
            BombermanFinal = pygame.transform.scale(BombermanFinal,(190,215))#Imagen de bomberman al final
            bombaExplosionDecoracion = pygame.image.load("Imagenes/Bombas/4.png")  
            bombaExplosionDecoracion = pygame.transform.scale(bombaExplosionDecoracion,(100,100))

            bombaImagen = pygame.image.load("Imagenes/Bombas/1.png")
            bombaImagen = pygame.transform.scale(bombaImagen,(55,55))

            #Dibujar por pantalla
            PANTALLA.blit(bombaExplosionDecoracion,(285,400))
            PANTALLA.blit(bombaImagen,(300,420))
            PANTALLA.blit(BombermanFinal,(390,320))
            pygame.display.update()

            # Pequeña pausa antes de salir del juego
            pygame.time.delay(2000)  # Pausa de 2 segundos (2000 milisegundos)

            
            
            return 
        
        # Pequeña pausa para evitar el desbordamiento de la pila de llamadas
        pygame.time.delay(20)
        
        #Refresca la pantalla
        MovimientopersonajeJugable()

    # Salida del juego, se ejecuta después de que el bucle principal haya finalizado. 
    #Se encarga de cerrar Pygame y liberar los recursos utilizados por el juego.
    pygame.quit()

#------------------------------------------RECURSIVIDAD(Bucle del juego)"End"------------------------------------------#

#Comienza la ejecución del programa. Esta llamada inicia el bucle principal del juego, Como el sistema de arranque de un carro.
bucle_principal()
