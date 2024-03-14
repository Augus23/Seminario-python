# Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
# luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

temperatura = float(input("Ingrese una temperatura y se la pasaremos a grados Fahrenheit: "))
print(temperatura,"grados celcius es un equivalente a",((9/5)*temperatura)+32,"grados fahrenheit")