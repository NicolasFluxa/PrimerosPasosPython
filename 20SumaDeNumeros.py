
# Recibimo todos los argumentos que el usuario nos quiera
# dar
def suma_de_numeros(*args):
    total = 0
    # lo que hace ese for es recorrer cada uno de los args
    # y lo suma en la variable total
    for arg in args:
        total += arg
    return total


print(suma_de_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
