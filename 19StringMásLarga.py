
def string_mas_larga(*args):
    # crea una lista para agregar el tamaño de cada STR
    lista_de_cantidad = []
    for arg in args:
        # recorre todos los argumentos obteniendo el largo de cada un
        # y ese valor lo agrega en la lista
        lista_de_cantidad.append(len(arg))

    return lista_de_cantidad


print(string_mas_larga("hola", "como", "estas"))