# Importamos las bibliotecas necesarias
import os
import random
import readchar

# Definimos constantes para las posiciones X e Y
PISICION_X = 0
POSICION_Y = 1

# Definimos la cantidad de objetos que queremos en el mapa
CANT_OBJETOS_MAPA = 5

# Definimos el mapa del juego como una cadena de texto
MAPA_JUEGO = """\
############################################
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
##                                        ##
############################################\
"""

# Definimos la posición inicial del jugador
POSICION_INICIAL = [4, 3]

# Inicializamos variables para el tamaño de la cola, la cola misma y la lista de objetos
tamano_cola = 0
cola = []
lista_de_objetos = []

# Inicializamos variables para controlar si el jugador ha perdido o se ha salido del juego
Perdiste = False
te_saliste = False

# Convertimos el mapa del juego de una cadena de texto a una lista de listas
# MAPA_JUEGO.split("\n") esto la separa en enter
# for row in Esto lo recorre
# list(row) a cada parte del row la agrega en una lista creada
# lo que nos da una lista de lista
MAPA_JUEGO = [list(row) for row in MAPA_JUEGO.split("\n")]

# Obtenemos el ancho y el alto del mapa
ANCHO_MAPA = len(MAPA_JUEGO[0])
ALTO_MAPA = len(MAPA_JUEGO)

# Mientras el jugador no haya perdido, seguimos jugando
while not Perdiste:
    # Limpiamos la consola
    os.system("cls")

    # Generamos objetos aleatorios en el mapa hasta llegar a la cantidad deseada
    while len(lista_de_objetos) < CANT_OBJETOS_MAPA:
        # Generamos una nueva posición aleatoria
        NUEVA_POSICION = [random.randint(0, ANCHO_MAPA - 1), random.randint(0, ALTO_MAPA - 1)]

        # Si la nueva posición no está ya ocupada por otro objeto, no es la posición inicial y no es una pared,
        # la añadimos a la lista de objetos
        if NUEVA_POSICION not in lista_de_objetos and NUEVA_POSICION != POSICION_INICIAL and \
                MAPA_JUEGO[NUEVA_POSICION[POSICION_Y]][NUEVA_POSICION[PISICION_X]] != "#":
            lista_de_objetos.append(NUEVA_POSICION)

    # Dibujamos el mapa
    print("+" + "-" * ANCHO_MAPA + "+")

    for cordenada_y in range(ALTO_MAPA):
        print("|", end="")

        for cordenada_x in range(ANCHO_MAPA):

            # Inicializamos el carácter a dibujar como un espacio vacío y las variables para los objetos y la cola
            # dibujados
            char_to_draw = " "
            objetos_dibujados = None
            cola_en_mapa = None

            # Comprobamos si hay algún objeto en la posición actual
            for objetos_en_mapa in lista_de_objetos:
                if objetos_en_mapa[PISICION_X] == cordenada_x and objetos_en_mapa[POSICION_Y] == cordenada_y:
                    # Si hay un objeto, cambiamos el carácter a dibujar y guardamos el objeto
                    char_to_draw = "0"
                    objetos_dibujados = objetos_en_mapa

            # Comprobamos si hay alguna pieza de la cola en la posición actual
            for piezas_de_cola in cola:
                if piezas_de_cola[PISICION_X] == cordenada_x and piezas_de_cola[POSICION_Y] == cordenada_y:
                    # Si hay una pieza de la cola, cambiamos el carácter a dibujar y guardamos la pieza de la cola
                    char_to_draw = "°"
                    cola_en_mapa = piezas_de_cola

            # Comprobamos si la posición inicial está en la posición actual
            if POSICION_INICIAL[PISICION_X] == cordenada_x and POSICION_INICIAL[POSICION_Y] == cordenada_y:
                # Si la posición inicial está en la posición actual, cambiamos el carácter a dibujar
                char_to_draw = "°"

                # Si hay un objeto en la posición actual, lo eliminamos de la lista de objetos y aumentamos el tamaño
                # de la cola
                if objetos_dibujados:
                    lista_de_objetos.remove(objetos_dibujados)
                    tamano_cola += 1

                # Si hay una pieza de la cola en la posición actual, el jugador ha perdido
                if cola_en_mapa:
                    Perdiste = True

            # Si hay una pared en la posición actual, cambiamos el carácter a dibujar
            if MAPA_JUEGO[cordenada_y][cordenada_x] == "#":
                char_to_draw = "#"

            # Dibujamos el carácter
            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * ANCHO_MAPA + "+")

    # Preguntamos al jugador hacia dónde quiere moverse
    direction = readchar.readchar()
    NUEVA_POSICION = None

    # Dependiendo de la dirección elegida, calculamos la nueva posición
    if direction == "w":
        NUEVA_POSICION = [POSICION_INICIAL[PISICION_X], (POSICION_INICIAL[POSICION_Y] - 1) % ALTO_MAPA]
    elif direction == "s":
        NUEVA_POSICION = [POSICION_INICIAL[PISICION_X], (POSICION_INICIAL[POSICION_Y] + 1) % ALTO_MAPA]
    elif direction == "a":
        NUEVA_POSICION = [(POSICION_INICIAL[PISICION_X] - 1) % ANCHO_MAPA, POSICION_INICIAL[POSICION_Y]]
    elif direction == "d":
        NUEVA_POSICION = [(POSICION_INICIAL[PISICION_X] + 1) % ANCHO_MAPA, POSICION_INICIAL[POSICION_Y]]
    elif direction == "q":
        # Si el jugador quiere salir, terminamos el juego
        te_saliste = True
        break

    # Si hay una nueva posición y no es una pared, movemos al jugador a la nueva posición
    if NUEVA_POSICION:
        if MAPA_JUEGO[NUEVA_POSICION[POSICION_Y]][NUEVA_POSICION[PISICION_X]] != "#":
            cola.insert(0, POSICION_INICIAL.copy())
            cola = cola[:tamano_cola]
            POSICION_INICIAL = NUEVA_POSICION

# Al final del juego, mostramos un mensaje dependiendo de si el jugador ha perdido o se ha salido
if Perdiste:
    print("Has Muerto!")
elif te_saliste:
    print("Por Quééééééééééééééé?")
