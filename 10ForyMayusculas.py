
texto_usuario = input("Que texto te gustaria evaluar?")
contadorMayusculas = 0
contadorComa = 0

for i in texto_usuario:
    if i.isupper():
        contadorMayusculas += 1


print("Cantidad mayusculas: {}".format(contadorMayusculas))
