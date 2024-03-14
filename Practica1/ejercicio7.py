#Escribe un programa que tome una lista de números enteros como entrada del usuario.
#Luego, convierte cada número en la lista a string y únelos en una sola cadena,
#separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
#de 3 de la cadena final.

list = []
cadena = ""
cadena_con_guion = ""
for i in range(10):
    list.append(int(input("Ingrese un numero: ")))
for i in list:
    if (i % 3 == 0):
        continue
    cadena += str(i)+"-"
print(cadena)