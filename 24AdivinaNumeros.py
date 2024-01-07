from random import randint


def adivinaNumero(numero):
    valor = randint(1, 100)
    while numero != valor:
        print("intentalo denuevo")
        numero = int(input(" "))
    print("Has acertado")


adivinaNumero(numero=int(input("Dime un numero entre 1 y 100 \n")))
