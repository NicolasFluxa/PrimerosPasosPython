import random

numberUsurious = int(input("Dime un numero: \n"))
numberCorrect = random.randint(1, 10)

if numberUsurious == numberCorrect:
    print("lo has logrado elegiste el mismo numero que la computadora")
else:
    print("Mas suerte la proxima")
    print("El numero correcto era: {}".format(numberCorrect))
