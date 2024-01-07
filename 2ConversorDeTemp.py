print('Hola Biencenido al conversor de temperaturas')
opcione = input('Fahrenheit a Celsius [1] y Celsius a Fahrenheit [2]: \n')
# guardo los que el usuario quiere en opciones
# luego segun su opcion elijo uno o otro desarrollo con la estructura de control if
# el valor introducido al no se modificado se guarda como {srt}
# por eso es "1"

if opcione == "1":
    celsius = float(input('Indique los grados de celsius: '))
    print('La temperatura en Fahrenheit es: {0:.2f}'.format(round((celsius * 9 / 5 + 32), 3)))
    # lo que hace "{0:.2f}" es que limita hasta dos decimales en caso de quere mas,
    # cambio el valor de dos a otro.

else:
    fahrenheit = float(input('Indique los grados de fahrenheit: '))
    print('La temperatura en celsius es: {0:.2f}'.format((fahrenheit-32)*5/9))

