import random


Titulo = "Bienvenido al juego del programa"
print(Titulo + "\n" + "-" * len(Titulo) + "\n")

pistola = None

print("Has escapado de la prision del programa\nAhora es tu primera elección")

Primera = input("Tienes dos opciones; ir por la puerta [1] o Entrar a la alcantarilla[2] ")
if Primera == "1":
    print("Tu eleccion te a llevado directo a un guardia, tienes que volver a elergir")
    primera1 = input("Te haces el dormido [1] o Corres del Gardia [2]")
    if primera1 == "1":
        print("No fue la mejor opcion te han atrapado y te devolvieron a la prision")
        print("Fin del Juego")
    else:
        print("Como has elegido correr sigues en tu huida ")
        print("Ahora estas en un lugar oscuro y ves un reflejo en el suelo al final del pasillo")
        primera2 = input("Corres devuelta para ver si el guardia se fue [1] o Vas al agujero iluminado [2]")
        if primera2 == "1":
            print("No fue la mejor opcion te han atrapado y te devolvieron a la prision")
            print("Fin del Juego")
        else:
            print("Como has elegido ir al agujero abres la escotilla y caes a la alcantarilla")
            print("Lo primero con lo que te encuentras en una pistola en el suelo")
            primera3 = input("Tomas el arma [1] o  no [2]")
            if primera3 == "1":
                pistola = True
            else:
                pistola = False

elif Primera == "2":
    print("Como has elegido ir entrar a la alcantarilla")
    print("Lo primero con lo que te encuentras en una pistola en el suelo")
    segunda = input("Tomas el arma [1] o  no [2]")
    if segunda == "1":
        pistola = True
    else:
        pistola = False

print("Sigues por la alcantarilla y te encuentras con una rata matematica la cual te dice\n"
      "que para seguir debes resolver el siguiente problema matematico\n"
      "Debes multiplicar 13 por un numero random entre 1 a 10")
resultado = int(input("Ingrese el resultado de 13 * un numero de 1 a 10"))
if resultado == 13 * random.randint(1,10):
    print("La rata odio a los sabelotodos estas muerto")

else:
    print("la rata odia a los sabelotodo y tu no lo eres, sigues en el juego")
    print("sigue tu camino por la alcantarilla hasta la salida la cual esta muy lejos de la prision\n"
          "llegas hasta una calle en donde le haces señales a un camionero\n"
          "el camionero para y te logras subir al camion\n"
          "despues de unas horas andando el camionero para en medio de la carretera y se lanza hacia ti\n"
          "Como es una persona gorda no puedes moverte por que no tienes la fuerza pero te acuerdas del arma")
    if pistola:
        print("como tomaste el arma ahora te puedes defender y le disparas muchos disparos en el cuerpo al camioner\n"
              "le robas el camion y sigues con tu huida a un mundo feliz")
        print("Felicidades has logrado huir puedes seguir con tu vida delictual")
    else:
        print("como no has elejido tomar el arma, el camionero logra su objetivo y luego de una larga noche\n"
              "decide matarte")
        print("Fin del juego")
