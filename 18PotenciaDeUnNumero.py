
# En Python, puedes hacer que los argumentos de una función
# sean opcionales asignándoles un valor por defecto en la
# definición de la función.

def potencia(numero, exponente=None):
    if exponente is not None:
        return numero ** exponente
    else:
        return numero ** 2


print(potencia(2))
print(potencia(2, 5))
