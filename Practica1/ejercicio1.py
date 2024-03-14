# Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y
# muestre cuántos años le faltan para alcanzar los 100 años.

edad = int(input("Ingrese su edad y le diremos cuanto le falta para alcanzar los 100 años: "))
if edad<=100:
    print("Le falta un total de",100 - edad,"años de edad")
else:
    print("Su edad supera los 100 años")