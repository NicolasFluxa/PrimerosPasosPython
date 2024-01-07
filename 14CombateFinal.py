# Importamos las bibliotecas necesarias
import os
import random
import readchar
import time

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


# Definir los datos de los Pokémon
pokemones = {
    "Pikachu": {
        "Vida Inicial": 30,
        "Bola Voltio": 9,
        "Onda Trueno": 11,
        "Recuperación": 6
    },
    "Mew": {
        "Vida Inicial": 35,
        "Megapuño": 12,
        "Coletazo": 9,
        "Recuperación": 6
    },
    "Chatot": {
        "Vida Inicial": 35,
        "Ataque Furia": 11,
        "Picotazon": 8,
        "Recuperación": 6
    }
}

# Ataques SQRTL
RECUPERACION = 6
PLACAJE = 10
PISTOLA_DE_AGUA = 12
BURBUJA = 9
# Vida SQRTL
VIDA_INICIAL_SQRTL = 40
vida_actual_Sqrtl = VIDA_INICIAL_SQRTL

TIEMPO_ESPERANDO = 2

TAMANO_VIDA = 30


# Mientras el jugador no haya perdido, seguimos jugando
while not te_saliste:
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

            # Comprobamos si hay algún objeto en la posición actual
            for objetos_en_mapa in lista_de_objetos:
                if objetos_en_mapa[PISICION_X] == cordenada_x and objetos_en_mapa[POSICION_Y] == cordenada_y:
                    # Si hay un objeto, cambiamos el carácter a dibujar y guardamos el objeto
                    char_to_draw = "0"
                    objetos_dibujados = objetos_en_mapa

            # Comprobamos si la posición inicial está en la posición actual
            if POSICION_INICIAL[PISICION_X] == cordenada_x and POSICION_INICIAL[POSICION_Y] == cordenada_y:
                # Si la posición inicial está en la posición actual, cambiamos el carácter a dibujar
                char_to_draw = "°"

                # Si hay un objeto en la posición actual, lo eliminamos de la lista de objetos y aumentamos el tamaño
                # de la cola
                if objetos_dibujados:
                    lista_de_objetos.remove(objetos_dibujados)

                    # Seleccionar un Pokémon al azar
                    pokemon_seleccionado = random.choice(list(pokemones.keys()))

                    # Acceder a los datos del Pokémon seleccionado
                    datos_pokemon = pokemones[pokemon_seleccionado]

                    VIDA_INICIAL_POKEMON = datos_pokemon["Vida Inicial"]
                    vida_actual_pokemon = VIDA_INICIAL_POKEMON

                    os.system("cls")
                    # Solo funciona por consola

                    print("Bienvenido al combate pokemon")
                    print(f"Parte atacando {pokemon_seleccionado}")
                    print("Debes precionar A, B o C para atacar y Q Para salir")

                    while vida_actual_Sqrtl > 0 and vida_actual_pokemon > 0:
                        # Crear una lista con las habilidades del Pokémon, excluyendo "vida_inicial"
                        habilidades = [habilidad for habilidad in datos_pokemon.keys() if habilidad != "Vida Inicial"]

                        # Seleccionar una habilidad al azar
                        habilidad_seleccionada = random.choice(habilidades)

                        if habilidad_seleccionada != "Recuperación":
                            print(f"Te han atacado con: {habilidad_seleccionada} -",
                                  datos_pokemon[habilidad_seleccionada])
                            vida_actual_Sqrtl -= datos_pokemon[habilidad_seleccionada]
                        else:
                            print("Recuperación de vida + 6")
                            vida_actual_pokemon += datos_pokemon[habilidad_seleccionada]

                        if vida_actual_Sqrtl <= 0:
                            vida_actual_Sqrtl = 0
                            break
                        if vida_actual_pokemon <= 0:
                            vida_actual_pokemon = 0
                            break

                        s = vida_actual_Sqrtl * TAMANO_VIDA // VIDA_INICIAL_SQRTL
                        print("Vida de Sqrtl  : [{}{}] ({}/{})".format(("*" * s), " " * (TAMANO_VIDA - s),
                                                                       vida_actual_Sqrtl, VIDA_INICIAL_SQRTL))
                        p = vida_actual_pokemon * TAMANO_VIDA // VIDA_INICIAL_POKEMON
                        print(f"Vida de {pokemon_seleccionado}",
                              " : [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_pokemon,
                                                         VIDA_INICIAL_POKEMON))

                        time.sleep(TIEMPO_ESPERANDO)
                        # Espera medio segundo antes de continuar

                        print("Ahora es tu turno.")
                        print("¿Que ataque te gustaria hacer")
                        print("[A] Placaje -10, [B] Pistola de Agua -12, [C] Recuperación, [Q] Para salir\n")
                        ataqueSqrtl = readchar.readchar()

                        if ataqueSqrtl == "A":
                            vida_actual_pokemon -= PLACAJE
                        elif ataqueSqrtl == "B":
                            vida_actual_pokemon -= PISTOLA_DE_AGUA
                        elif ataqueSqrtl == "Q":
                            te_saliste = True
                            break
                        else:
                            print('Te has curado + 6 Vida')
                            vida_actual_Sqrtl += RECUPERACION

                        if vida_actual_Sqrtl <= 0:
                            vida_actual_Sqrtl = 0
                        if vida_actual_pokemon <= 0:
                            vida_actual_pokemon = 0

                        os.system("cls")
                        # Solo funciona por consola

                    if vida_actual_pokemon <= 0:
                        print("Felicidades le has ganado a la maquina")
                    elif vida_actual_Sqrtl <= 0:
                        print(f"Ha ganado {pokemon_seleccionado}")
                        Perdiste = True

                    s = vida_actual_Sqrtl * TAMANO_VIDA // VIDA_INICIAL_SQRTL
                    print(
                        "Vida de Sqrtl  : [{}{}] ({}/{})".format(("*" * s), " " * (TAMANO_VIDA - s), vida_actual_Sqrtl,
                                                                 VIDA_INICIAL_SQRTL))
                    p = vida_actual_pokemon * TAMANO_VIDA // VIDA_INICIAL_POKEMON
                    print(f"Vida de {pokemon_seleccionado}",
                          " : [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_pokemon,
                                                     VIDA_INICIAL_POKEMON))

                    vida_actual_Sqrtl = VIDA_INICIAL_SQRTL

                    os.system("cls")

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
    if direction == "W":
        NUEVA_POSICION = [POSICION_INICIAL[PISICION_X], (POSICION_INICIAL[POSICION_Y] - 1) % ALTO_MAPA]
    elif direction == "S":
        NUEVA_POSICION = [POSICION_INICIAL[PISICION_X], (POSICION_INICIAL[POSICION_Y] + 1) % ALTO_MAPA]
    elif direction == "A":
        NUEVA_POSICION = [(POSICION_INICIAL[PISICION_X] - 1) % ANCHO_MAPA, POSICION_INICIAL[POSICION_Y]]
    elif direction == "D":
        NUEVA_POSICION = [(POSICION_INICIAL[PISICION_X] + 1) % ANCHO_MAPA, POSICION_INICIAL[POSICION_Y]]
    elif direction == "Q":
        # Si el jugador quiere salir, terminamos el juego
        te_saliste = True
        break

    # Si hay una nueva posición y no es una pared, movemos al jugador a la nueva posición
    if NUEVA_POSICION:
        if MAPA_JUEGO[NUEVA_POSICION[POSICION_Y]][NUEVA_POSICION[PISICION_X]] != "#":
            POSICION_INICIAL = NUEVA_POSICION

# Al final del juego, mostramos un mensaje dependiendo de si el jugador ha perdido o se ha salido
if te_saliste:
    print("Por Quééééééééééééééé?")
elif Perdiste:
    print("Has Muerto!")

