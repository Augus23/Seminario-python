# Implementa un programa que solicite al usuario que ingrese una lista de números.
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
# Nota: utilice la sentencia break cuando haga falta.
list = []
for i in range(10):
    list.append(int(input("Ingrese un numero: ")))
for i in list:
    if (i < 0):
        break
    print(i)