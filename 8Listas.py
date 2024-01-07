Lista_del_supermercado = []

qParaSalir = None

while qParaSalir != "Q":
    qParaSalir = str(input("Que te gustaria agregar a la lista del supermercado"))
    if qParaSalir != "Q":
        consulta = input("Seguro que quiere agregar " + qParaSalir)
        if consulta == "S":
            if qParaSalir not in Lista_del_supermercado:
                Lista_del_supermercado.append(qParaSalir)
                print("Se ha agregado " + qParaSalir)
            else:
                print(qParaSalir + " ya existe en la lista de supermercado")
        else:
            print("Entonces no se guarda " + qParaSalir)
    else:
        break

print("La lista del supermercado es ", Lista_del_supermercado)
