### Declaración de import (1)
import random

### Declaracion de funciones (2)
def cuantos_jugadores():
    cantidad_de_jugadores = 0
    while cantidad_de_jugadores <=0:
        try:
            cantidad_de_jugadores = int(input("Elija la cantidad de jugadores: >"))
        except ValueError:
            ("Ingresaste un caracter diferente de 1 o más")

    jugadores = { }

    x = 0
    while x < cantidad_de_jugadores:
        nombre_de_jugador = input("Ingrese el nombre del jugador: >")
        jugadores.update ({nombre_de_jugador : [0, False]})
        x += 1

        # jugadores[clave][0] -> puntos del jugador.
        # jugadores[clave][1] -> True/False -> si el jugador llegó a 450 puntos o no.

    return jugadores

# dados al azar
def dame_un_dado():
    return random.randrange(1, 7)
def dame_tirada(num_de_dados):
    tirada = []
    for dado in range(num_de_dados):
        tirada.append(dame_un_dado())
    return tirada

# para usar en turno() ->  para borrar los unos (1) al sacar 111, 111+1, 111+11 en el primer turno
def borrar_dado_1(tirada):
    for i in range (tirada.count(1)):
        tirada.remove(1)
# turno
def turno():

    puntos = 0
    num_de_dados = 5
    tirada = dame_tirada(num_de_dados)

    print("")

    while (tirada.count(1) or tirada.count(5) or tirada.count(1) == 3 or tirada.count(2) >= 3 or \
           tirada.count(3) >= 3 or tirada.count(4) >= 3 or tirada.count(5) >= 3 or tirada.count(6) >= 3):
        print("Tirada:", tirada)

        # primer turno only -> 111
        if num_de_dados == 5 and tirada.count(1) == 3:
            borrar_dado_1(tirada)
            puntos += 1000
            num_de_dados -= 3

        if num_de_dados == 5 and tirada.count(1) == 4:
            borrar_dado_1(tirada)
            puntos += 1100
            num_de_dados -= 4

        if num_de_dados == 5 and tirada.count(1) == 5:
            borrar_dado_1(tirada)
            puntos += 1200
            num_de_dados -= 5

        # primer turno only -> 12345 (escalera)
        if num_de_dados == 5 and tirada.count(1) and tirada.count(2) and tirada.count(3) and \
                tirada.count(4) and tirada.count(5):
            puntos += 1500
            num_de_dados -= 5

        # 1 y 5
        while tirada.count(1):
            tirada.remove(1)
            puntos += 100
            num_de_dados -= 1

        while tirada.count(5):
            tirada.remove(5)
            puntos += 50
            num_de_dados -= 1

        # 222, 333, 444, 666
        if tirada.count(2) >= 3:
            puntos += 200
            num_de_dados -= 3

        if tirada.count(3) >= 3:
            puntos += 300
            num_de_dados -= 3

        if tirada.count(4) >= 3:
            puntos += 400
            num_de_dados -= 3

        if tirada.count(6) >= 3:
            puntos += 600
            num_de_dados -= 3

        print("Puntos:", puntos)
        print("Dados restantes:", num_de_dados)

        # restart dice cicle
        if num_de_dados == 0:
            num_de_dados = 5
            print("! Todos tus dados cuentan. Van los 5 de nuevo!")

        tirada = dame_tirada(num_de_dados)
        print("")

    else:
        print("Tirada:", tirada)
        return puntos

def entre_turno(jugadores):
    print("")
    print("--- Puntajes ---")
    for clave in jugadores:
        if (jugadores[clave][1] == True):
            print (clave,"-",jugadores[clave][0],"puntos.")
        if (jugadores[clave][1] == False):
            print (clave,"- No entró. Necesita 450 puntos.")

    input("Presiona [Enter] para continuar.")

def ganador(jugadores):
    for clave in jugadores:
        if jugadores[clave][0] == 10000:
            return True

### Inicio del programa principal(3)

def main():
    print("DIX MILLE: 10.000")
    jugadores = cuantos_jugadores()
    ronda = 0

    while not ganador(jugadores):

        ronda += 1
        print("")
        print("---> Ronda", ronda,"<---")

        for clave in jugadores:
            print("")
            print("-> Turno de",clave)

            puntos = turno()

            if (jugadores[clave][1] == True):

                if (jugadores[clave][0] + puntos) > 10000:
                    print("! Te pasaste de 10000.")
                if (jugadores[clave][0] + puntos) <= 10000:
                    jugadores[clave][0] += puntos
                    print("! Puntos ganados:", puntos)

            if (jugadores[clave][1] == False) and (puntos < 450):
                print("! No llegaste a los 450 puntos.")

            if (jugadores[clave][1] == False) and (puntos >= 450):
                jugadores[clave][1] = True
                print("! 450 puntos. Entraste al juego con 0 puntos.")

            input("! Tu turno terminó. Presiona [Enter] para continuar.")

        entre_turno(jugadores)
    else:
        print("")
        print("El juego terminó!")
        for clave in jugadores:
            if jugadores[clave][0] == 10000:
                print(clave,"es el ganador!")
main()
