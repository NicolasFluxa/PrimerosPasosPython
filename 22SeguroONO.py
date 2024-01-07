

def estas_seguro():
    # Le pregunta al usuario si esta seguro
    pregunta = input("Estas seguro (si/no)")
    # dependiendo de la respuesta, Si = True; No = False
    if pregunta == "no" or pregunta == "No":
        return False
    else:
        return True


print(estas_seguro())