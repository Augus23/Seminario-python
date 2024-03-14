# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
# con los número pares y otras con los que son impares. Imprima las listas al terminar de
# procesarlas.
numeros = [1,2,3,4,5,6,7,8,9,10]
odd_list = []
pairs_list = []

for numero in numeros:
    if numero % 2 != 0:
        odd_list.append(numero)
    else:
        pairs_list.append(numero)
print("Numeros impares:",odd_list)
print("Numeros pares:",pairs_list)