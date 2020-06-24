# Declaración de import (1)
import random


# Declaración de funciones (2)
def cuantos_jugadores():
    cantidad_de_jugadores = 0
    while cantidad_de_jugadores < 1 or cantidad_de_jugadores > 4:
        try:
            cantidad_de_jugadores = int(input("Elija la cantidad de jugadores, de 1 a 4: >"))
        except ValueError:
            "Ingresaste un caracter diferente de 1 a 4."
    jugadores = {}
    x = 0
    while x < cantidad_de_jugadores:
        nombre_de_jugador = input("Ingrese el nombre del jugador " + str(x+1) + ": >")
        jugadores.update({nombre_de_jugador: [[], 0]})
        x += 1
        # jugadores[clave][0] -> lista de dados.
        # jugadores[clave][1] -> puntos.
    return jugadores


def cuantos_dados():
    num_de_dados = 0
    while num_de_dados < 3 or num_de_dados > 5:
        try:
            num_de_dados = int(input("Elija la cantidad de dados, de 3 a 5: >"))
        except ValueError:
            "Ingresaste un caracter diferente de 3 a 5."
    return num_de_dados


# Dados al azar
def dame_un_dado():
    return random.randrange(1, 7)


def dame_tirada(num_de_dados):
    tirada = []
    for dado in range(num_de_dados):
        tirada.append(dame_un_dado())
    return tirada


# Inicio del programa principal(3)
def main():
    dice_graphics = [
        (" ------- ",
         "|       |",
         "|   0   |",
         "|       |",
         " ------- ",),
        (" ------- ",
         "|       |",
         "| 0   0 |",
         "|       |",
         " ------- ",),
        (" ------- ",
         "| 0     |",
         "|   0   |",
         "|     0 |",
         " ------- ",),
        (" ------- ",
         "| 0   0 |",
         "|       |",
         "| 0   0 |",
         " ------- ",),
        (" ------- ",
         "| 0   0 |",
         "|   0   |",
         "| 0   0 |",
         " ------- ",),
        (" ------- ",
         "| 0   0 |",
         "| 0   0 |",
         "| 0   0 |",
         " ------- ",),
    ]

    print("Juego de dados")
    jugadores = cuantos_jugadores()
    num_de_dados = cuantos_dados()

    print("")

    # append dados a jugadores[clave][0]
    for jugador in jugadores:
        tirada = dame_tirada(num_de_dados)
        for dado in tirada:
            jugadores[jugador][0].append(dado)
        # print(jugador)
        # print(tirada)

    # Calcular máximo valor de dados
    n = 0
    for i in range(num_de_dados):
        item_max_value = max(jugadores.items(), key=lambda x: x[1][0][n])
        # print('Mayor valor del', str(n+1)+'° dado:', item_max_value[1][0][n])

        # Asignar puntos a jugadores[clave][1]
        lista_dado_max_values = list()
        for index, (key, (dados, puntos)) in enumerate(jugadores.items()):
            if dados[n] == item_max_value[1][0][n]:
                lista_dado_max_values.append(key)

        for jugador in jugadores:
            if jugador in lista_dado_max_values:
                if len(lista_dado_max_values) == 1:
                    jugadores[jugador][1] += 1
                if len(lista_dado_max_values) == 2:
                    jugadores[jugador][1] += 0.5
                if len(lista_dado_max_values) == 3:
                    jugadores[jugador][1] += 0.33
                if len(lista_dado_max_values) == 4:
                    jugadores[jugador][1] += 0.25

        # print("Puntos para:", lista_keys_con_max_values)
        # print ("len de lista:",len(lista_keys_con_max_values))
        n += 1

    # print("jugadores:",jugadores)
    # print("")

    # Mayor suma gana 1 punto
    item_max_suma = max(jugadores.items(), key=lambda x: sum(x[1][0]))
    lista_items_max_suma = list()
    for index, (key, (dados, puntos)) in enumerate(jugadores.items()):
        if sum(dados) == sum(item_max_suma[1][0]):
            lista_items_max_suma.append(key)
    # print("Lista de jugadores con max suma de dados:",lista_items_max_suma)
    for jugador in jugadores:
        if jugador in lista_items_max_suma:
            if len(lista_items_max_suma) == 1:
                jugadores[jugador][1] += 1
            if len(lista_items_max_suma) == 2:
                jugadores[jugador][1] += 0.5
            if len(lista_items_max_suma) == 3:
                jugadores[jugador][1] += 0.33
            if len(lista_items_max_suma) == 4:
                jugadores[jugador][1] += 0.25

    # Print de nombre de jugador, tiradas de dados, y suma de dados
    for jugador in jugadores:
        print(jugador+":")
        # print (jugadores[jugador][0])
        print(', '.join(map(str, (jugadores[jugador][0]))), "- Suma:", sum(jugadores[jugador][0]))
        for i in range(5):  # 5 is the height of the die.
            for die in jugadores[jugador][0]:
                # Now get the corresponding die in the DICE list
                # and print its first line, then the first line of
                # the next die and so on.
                print(dice_graphics[die - 1][i], end=' ')
            print()
    print("")
    # Print de puntos
    print("Puntajes:")
    for jugador in jugadores:
        if jugadores[jugador][1] != 1:
            print(jugador, "-", jugadores[jugador][1], "puntos.")
        if jugadores[jugador][1] == 1:
            print(jugador, "-", jugadores[jugador][1], "punto.")

    # Declarar el ganador
    item_max_puntos = max(jugadores.items(), key=lambda x: x[1][1])
    lista_max_puntos = list()
    for index, (key, (dados, puntos)) in enumerate(jugadores.items()):
        if puntos == item_max_puntos[1][1]:
            lista_max_puntos.append(key)
    for jugador in jugadores:
        if jugador in lista_max_puntos:
            print("!", jugador, "ganó.")


main()

print("")
input("Presione ENTER para finalizar.")
