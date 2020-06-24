### Declaracion de funciones(2)
def ingresar_jugada():
    global dict
    turno_actual=1

    while (not ganadorX() and not ganadorO() and turno_actual < 10):
        print("Turno",turno_actual)

        jugada = 0
        while jugada not in range(1, 10):
            try:
                jugada = int(input("Ingrese su jugada: >"))
                for key in dict:
                    if jugada == dict[key]:
                        turno_actual = turno_actual + 1 #cambio ayuda del profe
                        dict[key] = determinarJugador(turno_actual)
                        print(dict['p1'], dict['p2'], dict['p3'])
                        print(dict['p4'], dict['p5'], dict['p6'])
                        print(dict['p7'], dict['p8'], dict['p9'])

                        print("")

            except ValueError:
                ("ValueError")

    if ganadorX():
        print ("Ganador: X")
    if ganadorO():
        print ("Ganador: O")
    if turno_actual == 10 and not ganadorX() and not ganadorO():
        print ("Empate")

def ganadorX():
    if dict['p1'] == dict['p2'] == dict['p3'] == "X" or \
                                        dict['p4'] == dict['p5'] == dict['p6'] == "X" or \
                                        dict['p7'] == dict['p8'] == dict['p9'] == "X" or \
                                        dict['p1'] == dict['p4'] == dict['p7'] == "X" or \
                                        dict['p2'] == dict['p5'] == dict['p8'] == "X" or \
                                        dict['p3'] == dict['p6'] == dict['p9'] == "X" or \
                                        dict['p1'] == dict['p5'] == dict['p9'] == "X" or \
                                        dict['p3'] == dict['p5'] == dict['p7'] == "X":
        return True
    else:
        return False

def ganadorO():
    if dict['p1'] == dict['p2'] == dict['p3'] == "O" or \
                                        dict['p4'] == dict['p5'] == dict['p6'] == "O" or \
                                        dict['p7'] == dict['p8'] == dict['p9'] == "O" or \
                                        dict['p1'] == dict['p4'] == dict['p7'] == "O" or \
                                        dict['p2'] == dict['p5'] == dict['p8'] == "O" or \
                                        dict['p3'] == dict['p6'] == dict['p9'] == "O" or \
                                        dict['p1'] == dict['p5'] == dict['p9'] == "O" or \
                                        dict['p3'] == dict['p5'] == dict['p7'] == "O":
        return True
    else:
        return False

def determinarJugador(i): #robado
    if (i % 2 == 0):
        return "X"
    else:
        return "O"

### Inicio del programa principal(3)
print("TA TE TI")
print("Instrucciones: primer jugador es X. Segundo es O. Elija del 1 al 9.")

dict = {'p1': 1, 'p2': 2, 'p3': 3, 'p4': 4, 'p5': 5, 'p6': 6, 'p7': 7, 'p8': 8, 'p9': 9}

print(dict['p1'], dict['p2'], dict['p3'])
print(dict['p4'], dict['p5'], dict['p6'])
print(dict['p7'], dict['p8'], dict['p9'])

print("")

ingresar_jugada()