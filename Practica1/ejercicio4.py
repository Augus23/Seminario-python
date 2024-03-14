# Cree un programa que dada una lista de números imprima sólo los que son pares.
# Nota: utilice la sentencia continue donde haga falta.

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 != 0:
        continue
    print(numero)