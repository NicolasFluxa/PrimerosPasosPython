def suma_de_caracteres(texto):
    largo = 0
    for i in texto:
        largo += 1
    return largo


texto = input("dime un texto para contar los caracteres")

print(suma_de_caracteres(texto))
