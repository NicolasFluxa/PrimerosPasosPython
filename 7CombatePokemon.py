import os
from random import randint
import time

VIDA_INICIAL_PIKACHU = 90
VIDA_INICIAL_SQRTL = 80

TAMANO_VIDA = 20

vida_actual_Pikachu = VIDA_INICIAL_PIKACHU
vida_actual_Sqrtl = VIDA_INICIAL_SQRTL

# Ataques
BOLA_VOLTIO = 9
ONDA_TRUENO = 11
PLACAJE = 10
PISTOLA_DE_AGUA = 12
BURBUJA = 9

print("Bienvenido al combate pokemon")
print("Parte atacando Pikachu")

while vida_actual_Sqrtl > 0 and vida_actual_Pikachu > 0:

    ataquePikachu = randint(BOLA_VOLTIO, ONDA_TRUENO)
    if ataquePikachu == BOLA_VOLTIO:
        print("Te atacaron con Bola Voltio -9")
        vida_actual_Sqrtl -= BOLA_VOLTIO
    else:
        print('Te atacaron con Onda Trueno -11')
        vida_actual_Sqrtl -= ONDA_TRUENO

    if vida_actual_Sqrtl <= 0:
        vida_actual_Sqrtl = 0
    if vida_actual_Pikachu <= 0:
        vida_actual_Pikachu = 0

    s = vida_actual_Sqrtl * TAMANO_VIDA // VIDA_INICIAL_SQRTL
    print("Sqrtl:   [{}{}] ({}/{})".format("*" * s, " " * (TAMANO_VIDA - s), vida_actual_Sqrtl, VIDA_INICIAL_SQRTL))
    p = vida_actual_Pikachu * TAMANO_VIDA // VIDA_INICIAL_PIKACHU
    print("Pikachu: [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_Pikachu, VIDA_INICIAL_PIKACHU))

    time.sleep(0.5)
    # Espera medio segundo antes de continuar
    os.system("cls")
    # Solo funciona por consola

    print("Ahora es tu turno.")
    print("¿Que ataque te gustaria hacer")

    ataqueSqrtl = None
    while ataqueSqrtl != "A" and ataqueSqrtl != "B" and ataqueSqrtl != "C":
        ataqueSqrtl = input("[A] Placaje -10, [B] Pistola de Agua -12, [C] Burbuja -9\n")

    if ataqueSqrtl == "A":
        vida_actual_Pikachu -= PLACAJE
    elif ataqueSqrtl == "B":
        vida_actual_Pikachu -= PISTOLA_DE_AGUA
    else:
        vida_actual_Pikachu -= BURBUJA

    if vida_actual_Sqrtl <= 0:
        vida_actual_Sqrtl = 0
    if vida_actual_Pikachu <= 0:
        vida_actual_Pikachu = 0

    os.system("cls")
    # Solo funciona por consola


if vida_actual_Pikachu <= 0:
    print("Felicidades le has ganado a la maquina")
elif vida_actual_Sqrtl <= 0:
    print("Felicidades ha ganado Pikachu")
else:
    print("Hay un error 3")

s = vida_actual_Sqrtl * TAMANO_VIDA // VIDA_INICIAL_SQRTL
print("Sqrtl  : [{}{}] ({}/{})".format(("*" * s), " " * (TAMANO_VIDA - s), vida_actual_Sqrtl, VIDA_INICIAL_SQRTL))
p = vida_actual_Pikachu * TAMANO_VIDA // VIDA_INICIAL_PIKACHU
print("Pikachu: [{}{}] ({}/{})".format("*" * p, " " * (TAMANO_VIDA - p), vida_actual_Pikachu, VIDA_INICIAL_PIKACHU))
