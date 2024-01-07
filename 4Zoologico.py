print('Bienvenido al Zoologico\nResponda las siguientes preguntas: ')

while True:
    edad = int(input('¿Cual es tu edad?'))

    carnet = input('Tienes algun tipo de carnet\nFamilia numerosa [F],'
                   'Estudiante [E], Pensionado[P], No tiene [N]')

    if edad <= 10:
        print('gratis')
    elif 25 <= edad <= 35:
        if carnet == "E":
            print("Tienes 20% de descuento.")
        else:
            print("No tiene descuento")
    elif 35 < edad <= 64:
        if carnet == "F":
            print("Tiene 5% de descuento por integrante de la familia")
        else:
            print("No tiene descuento")
    elif edad >= 65:
        if carnet == "P":
            print("Tiene 25% de descuento")
        else:
            print("Tiene un 15% de descuento")

    else:
        print("algo malo")

