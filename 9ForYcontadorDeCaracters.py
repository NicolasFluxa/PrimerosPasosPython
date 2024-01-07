
texto_usuario = input("Que texto te gustaria evaluar?")
contadorEspacio = 0
contadorComa = 0
contadorPunto = 0

for i in texto_usuario:
    if i == " ":
        contadorEspacio += 1
    elif i == ",":
        contadorComa += 1
    elif i == ".":
        contadorPunto += 1

print("Cantidad de Comas: {}, Espacios: {} y Puntos: {}".format(contadorComa, contadorEspacio, contadorPunto))