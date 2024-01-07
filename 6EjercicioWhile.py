respuesta = None

while respuesta != "1" and respuesta != "2" and respuesta != "3":
    respuesta = input("ingresa 1, 2, 3")
if respuesta == "1":
    print(1)
elif respuesta == "2":
    print(2)
elif respuesta == "3":
    print(3)
else:
    print("No existe")