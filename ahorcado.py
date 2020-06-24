### Declaración de import (1)
import random

### Declaracion de funciones(2)
def buscar_indice(palabra, letra):
    indices = [i for i, ltr in enumerate(palabra) if ltr == letra]
    return indices

def split(word): # Python3 program to Split string into characters
    return [char for char in word]

def elegir_modo():
    print("1: Modo temático. 2: Modo extremo.")
    modo_elegido=0
    while modo_elegido !=1 and modo_elegido !=2:
        try:
            modo_elegido = int(input("Elija el modo ingresando 1 o 2: >"))
        except ValueError:
            ("Ingresaste un caracter diferente de 1 ó 2")
        if modo_elegido == 1:
            print("Modo temático!")
        if modo_elegido == 2:
            print("Modo extremo!")
    return modo_elegido

def randomizar_palabra(modo_elegido):
    global arte, ciencia, deportes, entretenimiento, geografia, historia

    todas_las_listas = (arte + ciencia + deportes + entretenimiento + geografia + historia)

    palabra_a_adivinar = (random.choice(todas_las_listas))

    palabra_oculta = (len(palabra_a_adivinar) * "_")

    if modo_elegido == 2:

        palabra_oculta = completar_inicio_y_fin(palabra_a_adivinar, palabra_oculta)

    return palabra_a_adivinar, palabra_oculta

def completar_inicio_y_fin(palabra_a_adivinar, palabra_oculta):
    yourIndexToReplace = 0
    newLetter = palabra_a_adivinar[0]
    palabra_oculta = "".join((palabra_oculta[:yourIndexToReplace], newLetter, palabra_oculta[yourIndexToReplace + 1:]))
    # https://stackoverflow.com/questions/38856180/python-string-replace-index
    yourIndexToReplace = len(palabra_oculta) - 1
    newLetter = palabra_a_adivinar[-1]
    palabra_oculta = "".join((palabra_oculta[:yourIndexToReplace], newLetter, palabra_oculta[yourIndexToReplace + 1:]))
    return palabra_oculta

def modo_tematico(palabra_a_adivinar):
    global arte, ciencia, deportes, entretenimiento, geografia, historia

    if palabra_a_adivinar in arte:
        print ("El tema es 'Arte'")
    if palabra_a_adivinar in ciencia:
        print("El tema es 'Ciencia'")
    if palabra_a_adivinar in deportes:
        print("El tema es 'Deportes'")
    if palabra_a_adivinar in entretenimiento:
        print("El tema es 'Entretenimiento'")
    if palabra_a_adivinar in geografia:
        print("El tema es 'Geografía'")
    if palabra_a_adivinar in historia:
        print("El tema es 'Historia'")

def ingresar_jugada(palabra_a_adivinar, palabra_oculta):

    errores = 0
    ganador = False
    letras_erroneas = []

    while (not ganador and errores < 6):
        print("")
        if letras_erroneas:
            print(letras_erroneas)
        if errores == 0:
            print("   +----+  ")  # 1
            print("   |       ")  # 2
            print("   |       ")  # 3
            print("   |       ")  # 4
            print("   |       ")  # 5
            print("   |       ")  # 6
            print("+--+--+    ")  # 7
        if errores == 1:
            print("   +----+  ")  # 1
            print("   |    O  ")  # 2
            print("   |       ")  # 3
            print("   |       ")  # 4
            print("   |       ")  # 5
            print("   |       ")  # 6
            print("+--+--+    ")  # 7
        if errores == 2:
            print("   +----+  ")  # 1
            print("   |    O  ")  # 2
            print("   |    |  ")  # 3
            print("   |    |  ")  # 4
            print("   |       ")  # 5
            print("   |       ")  # 6
            print("+--+--+    ")  # 7
        if errores == 3:
            print("   +----+  ")  # 1
            print("   |    O  ")  # 2
            print("   |    |\ ")  # 3
            print("   |    |  ")  # 4
            print("   |       ")  # 5
            print("   |       ")  # 6
            print("+--+--+    ")  # 7
        if errores == 4:
            print("   +----+  ")  # 1
            print("   |    O  ")  # 2
            print("   |   /|\ ")  # 3
            print("   |    |  ")  # 4
            print("   |       ")  # 5
            print("   |       ")  # 6
            print("+--+--+    ")  # 7
        if errores == 5:
            print("   +----+  ")  # 1
            print("   |    O  ")  # 2
            print("   |   /|\ ")  # 3
            print("   |    |  ")  # 4
            print("   |     \ ")  # 5
            print("   |       ")  # 6
            print("+--+--+    ")  # 7

        for i in palabra_oculta:
            print(i, end=" ")
        print("Total:", len(palabra_a_adivinar), "letras.")

        print("1: Adivinar una letra. 2: Adivinar la palabra.")

        opcion_de_turno=0
        while opcion_de_turno != 1 and opcion_de_turno != 2:
            try:
                opcion_de_turno = int(input("Elija ingresando 1 o 2: >"))
            except ValueError:
                ("Ingresaste un caracter diferente de 1 ó 2")

            # Adivinar letra
            if opcion_de_turno == 1:
                intento_adivinar_letra = ""
                while (intento_adivinar_letra == ""):
                    try:
                        intento_adivinar_letra = input("Ingrese la letra: >")[0]
                    except IndexError:
                        ("No ingresaste nada.")

                indices = buscar_indice(palabra_a_adivinar, intento_adivinar_letra)

                for i in indices:
                    # https://stackoverflow.com
                    # /questions/49046241/python-beginner-here-typeerror-str-object-does-not-support-item-assignment
                    palabra_oculta = palabra_oculta[:i] + intento_adivinar_letra + palabra_oculta[i + 1:]

                if intento_adivinar_letra not in palabra_a_adivinar:
                    errores = errores + 1
                    letras_erroneas.append(intento_adivinar_letra)

                if palabra_oculta == palabra_a_adivinar:
                    ganador = True

            # Adivinar palabra
            if opcion_de_turno == 2:
                intento_adivinar_palabra = ""
                while (intento_adivinar_palabra == ""):
                        intento_adivinar_palabra = input("Ingrese la palabra: >")

                if intento_adivinar_palabra == palabra_a_adivinar:
                    ganador = True
                if intento_adivinar_palabra != palabra_a_adivinar:
                    errores = errores + 1

    if errores == 6:
        print("")
        print("   +----+  ")  # 1
        print("   |    O  ")  # 2
        print("   |   /|\ ")  # 3
        print("   |    |  ")  # 4
        print("   |   / \ ")  # 5
        print("   |       ")  # 6
        print("+--+--+    ")  # 7
        print(" Perdiste. ")  # 8

    if ganador == True:
        print()
        print("¡Ganaste!")

### Inicio del programa principal(3)

arte = ('Arquitectura', 'Escultura', 'Pintura', 'Música', 'Literatura',
             'Danza', 'Cine', 'Impresionismo', 'Dostoievski', 'Origami')
ciencia = ('Matemática', 'Lógica', 'Física', 'Química', 'Astronomía',
           'Geología', 'Biología', 'Epistemología', 'Lógica', 'Ingeniería')
deportes = ('Atletismo', 'Ciclismo', 'Fútbol', 'Básket', 'Rugby',
            'Tenis', 'Volley', 'Karate', 'Taekwondo', 'Gimnasia')
entretenimiento = ('Shakespeare', 'Casablanca', 'Batman', 'RoboCop', 'Beatles',
                   'Animé', 'Nintendo', 'Simpsons', 'Concierto', 'Calesita')
geografia = ('América', 'Europa', 'Asia', 'África', 'Oceanía',
             'Antártica', 'Antártida', 'Groenlandia', 'Kasajistán', 'Noruega')
historia = ('Agricultura', 'Civilización', 'Mesopotamia', 'Atenas', 'Esparta',
            'Napoleón', 'Trafalgar', 'Belgrano', 'Hitler', 'Stalingrado')

print("AHORCADO")

modo_elegido = elegir_modo()

palabra_a_adivinar, palabra_oculta = randomizar_palabra(modo_elegido)

if modo_elegido==1:
    modo_tematico(palabra_a_adivinar)

ingresar_jugada(palabra_a_adivinar, palabra_oculta)
