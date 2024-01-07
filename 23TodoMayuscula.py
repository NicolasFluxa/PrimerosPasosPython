import string


def mayusculas():
    # Creo las listas en donde estaran las minusculas y mayusculas.
    lista_mayu = list(string.ascii_uppercase)
    lista_minu = list(string.ascii_lowercase)

    lista_resuelto = []

    # La str entregada por el usuario se transforma de inmediato en una lista
    lista_entrada = list(input("Ingrese una palabra: "))
    # es un For que recorre cada una de las letras dentro de la lista
    for i in lista_entrada:
        # si una de esas letras esta en la lista minuscula
        if i in lista_minu:
            # ya que ambas listas son iguales toma el valor del caracter y lo busca en la lista
            # mayuscula y la agrega en lista resultado
            lista_resuelto.append(lista_mayu[lista_minu.index(i)])
        elif i == " ":
            lista_resuelto.append(" ")

    lista_resuelto = "".join(lista_resuelto)

    return lista_resuelto


print(mayusculas())
