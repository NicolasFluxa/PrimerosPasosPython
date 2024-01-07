SALIR = "Salir"
ARCHIVO_LISTA = "Lista compra.txt"


# Es una funcion la cual solo retorna una imput, el cual se debe agregar a alguna variable
# cuando se use la funcion
def preguntar_producto_usuario():
    return input(f"Ingrese el nombre del producto o para salir escriba ({SALIR})")


# Gracias a la siguiente sintaxis creamos un archivo "ARCHIVO_LISTA" variable antes creada
# y escribe en este archivo .txt separado por un salto, el .join pasa de lista a str
def guardar_lista_a_disco(lista_compra):
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


# Comprueba que no este los items dentro de la lista, gracias al list conversation transforma todos
# Valores de la lista a minusculas con el .lower() y si no esta lo introduce.
# problemas cuando pones un espacio luego del item, "pan " y "pan" son lo mismo pero el codigo los
# toma como distintos
def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
        print("Producto ya existe!")
    else:
        lista_compra.append(item_a_guardar)


# Crea la lista de compras y pregunta si quieren usar la lista preguradada
# esta sintaxis lo que hace es intentar abrir un archivo pero en caso de que
# no se encuentre gestiona la excepcion mostrando un mensaje al usuario
def cargar_archivo_o_crear_lista():
    lista_compra = []
    if input("¿Quieres cargar la última lista de la compra? (S/N)") == "S":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo de la compra no encotrado!")
    return lista_compra


# muestra la lista
def motrasr_lista(lista_compra):
    print("\n".join(lista_compra))


# Es donde son llamadas todas las funciones
def main():
    lista_compra = cargar_archivo_o_crear_lista()
    motrasr_lista(lista_compra)
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIR:
        guardar_item_en_lista(lista_compra, input_usuario)
        input_usuario = preguntar_producto_usuario()
        motrasr_lista(lista_compra)
    guardar_lista_a_disco(lista_compra)


# Es donde se ejecuta el codigo
if __name__ == "__main__":
    main()
