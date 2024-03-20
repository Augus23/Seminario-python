import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_failures = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

failures=0

print("1. Facil")
print("2. Media")
print("3. Dificil")
option = int(input("Seleccione una dificultad: "))

letters = []
match option:
    case 1:
        for letter in secret_word:
            if letter in ['a', 'e', 'i', 'o', 'u','ó']:
                letters.append(letter)
                guessed_letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case 2:
        for cont in range(len(secret_word)):
            if cont == 0 or cont == len(secret_word)-1:
                letters.append(secret_word[cont])
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case 3:
        word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while failures != max_failures: 
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ingresada es vacia
    if letter == "":
        print("Error, no se permiten caracteres vacios")
        continue
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    # Verificar si la letra está en la palabra secreta
    if option == 2:
        if letter in secret_word[1:-1]:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            # Sumo uno a la cantidad de fallos (no tomo el caracter vacio como fallo)
            failures+=1  
    else:
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            # Sumo uno a la cantidad de fallos (no tomo el caracter vacio como fallo)
            failures+=1
    # Mostrar la palabra parcialmente adivinada
    letters = []
    cont = 0
    for letter in secret_word:
        if (letter in guessed_letters) or ((option == 2) and ((cont == 0) or (cont == len(secret_word)-1))):
            letters.append(letter)
        else:
            letters.append("_")
        cont += 1
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado tus {max_failures} fallos.")
    print(f"La palabra secreta era: {secret_word}")