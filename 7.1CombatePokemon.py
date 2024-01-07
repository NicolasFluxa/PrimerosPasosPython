import random
import time
import os
import readchar

# Definir los datos de los Pokémon
pokemones = {
    "Pikachu": {
        "Vida Inicial": 90,
        "Bola Voltio": 9,
        "Onda Trueno": 11,
        "Recuperación": 6
    },
    "Mew": {
        "Vida Inicial": 75,
        "Megapuño": 12,
        "Coletazo": 9,
        "Recuperación": 6
    },
    "Chatot": {
        "Vida Inicial": 85,
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
VIDA_INICIAL_SQRTL = 80
vida_actual_Sqrtl = VIDA_INICIAL_SQRTL

TIEMPO_ESPERANDO = 5


# Seleccionar un Pokémon al azar
pokemon_seleccionado = random.choice(list(pokemones.keys()))

# Acceder a los datos del Pokémon seleccionado
datos_pokemon = pokemones[pokemon_seleccionado]

VIDA_INICIAL_POKEMON = datos_pokemon["Vida Inicial"]
vida_actual_pokemon = VIDA_INICIAL_POKEMON

TAMANO_VIDA = 30

print("Bienvenido al combate pokemon")
print(f"Parte atacando {pokemon_seleccionado}")
print("Debes precionar A, B o C para atacar")

while vida_actual_Sqrtl > 0 and vida_actual_pokemon > 0:
    # Crear una lista con las habilidades del Pokémon, excluyendo "vida_inicial"
    habilidades = [habilidad for habilidad in datos_pokemon.keys() if habilidad != "Vida Inicial"]

    # Seleccionar una habilidad al azar
    habilidad_seleccionada = random.choice(habilidades)

    if habilidad_seleccionada != "Recuperación":
        print(f"Te han atacado con: {habilidad_seleccionada} -", datos_pokemon[habilidad_seleccionada])
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
    print("Vida de Sqrtl  : [{}{}] ({}/{})".format(("*" * s), " " * (TAMANO_VIDA - s), vida_actual_Sqrtl, VIDA_INICIAL_SQRTL))
    p = vida_actual_pokemon * TAMANO_VIDA // VIDA_INICIAL_POKEMON
    print(f"Vida de {pokemon_seleccionado}",
          " : [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_pokemon, VIDA_INICIAL_POKEMON))

    time.sleep(TIEMPO_ESPERANDO)
    # Espera medio segundo antes de continuar
    os.system("cls")
    # Solo funciona por consola

    print("Ahora es tu turno.")
    print("¿Que ataque te gustaria hacer")
    print("[A] Placaje -10, [B] Pistola de Agua -12, [C] Recuperación \n")
    ataqueSqrtl = readchar.readchar()

    if ataqueSqrtl == "A":
        vida_actual_pokemon -= PLACAJE
    elif ataqueSqrtl == "B":
        vida_actual_pokemon -= PISTOLA_DE_AGUA
    else:
        print('Te has curado + 6 Vida')
        vida_actual_Sqrtl += RECUPERACION

    if vida_actual_Sqrtl <= 0:
        vida_actual_Sqrtl = 0
    if vida_actual_pokemon <= 0:
        vida_actual_pokemon = 0

    s = vida_actual_Sqrtl * TAMANO_VIDA // VIDA_INICIAL_SQRTL
    print("Vida de Sqrtl  : [{}{}] ({}/{})".format(("*" * s), " " * (TAMANO_VIDA - s), vida_actual_Sqrtl, VIDA_INICIAL_SQRTL))
    p = vida_actual_pokemon * TAMANO_VIDA // VIDA_INICIAL_POKEMON
    print(f"Vida de {pokemon_seleccionado}",
          " : [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_pokemon, VIDA_INICIAL_POKEMON))

    os.system("cls")
    # Solo funciona por consola

if vida_actual_pokemon <= 0:
    print("Felicidades le has ganado a la maquina")
elif vida_actual_Sqrtl <= 0:
    print(f"Ha ganado {pokemon_seleccionado}")

s = vida_actual_Sqrtl * TAMANO_VIDA // VIDA_INICIAL_SQRTL
print("Vida de Sqrtl  : [{}{}] ({}/{})".format(("*" * s), " " * (TAMANO_VIDA - s), vida_actual_Sqrtl, VIDA_INICIAL_SQRTL))
p = vida_actual_pokemon * TAMANO_VIDA // VIDA_INICIAL_POKEMON
print(f"Vida de {pokemon_seleccionado}",
      " : [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_pokemon, VIDA_INICIAL_POKEMON))
