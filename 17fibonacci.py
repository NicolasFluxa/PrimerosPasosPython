def main(cantidad):
    inicial = 0
    segundo = 1
    for i in range(cantidad):
        aux = inicial + segundo
        inicial = segundo
        segundo = aux
        print(f"{segundo}")


if __name__ == '__main__':
    main(int(input("Dinos la Cantidad")))
