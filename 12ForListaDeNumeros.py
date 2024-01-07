from random import randint
listaNumeros = []

numeroMenor = 10
numeroMayor = 0

for i in range(10):
    listaNumeros.append(randint(1, 10))
    if listaNumeros[i] <= numeroMenor:
        numeroMenor = listaNumeros[i]
    elif listaNumeros[i] > numeroMayor:
        numeroMayor = listaNumeros[i]

print(listaNumeros)
print(numeroMayor, numeroMenor)

