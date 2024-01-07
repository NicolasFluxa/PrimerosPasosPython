valorUsuario = int(input("Ingrese un Numero entre 1 y 9"))

for i in range(1, 11):
    print(valorUsuario, " * ", i, " = {}".format(valorUsuario * i))

    if (valorUsuario * i) % 2 == 0:
        print(valorUsuario, " * ", i, " = {}".format(valorUsuario * i))
