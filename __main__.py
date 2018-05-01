# Made by Gabr0!
import random
import msvcrt
import sys
import os

ESPACIO = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
           (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
           (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
           (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
           (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def localizacion():
    return random.sample(ESPACIO,3)
def mover_jugador(jugador,movimiento):
    x,y = jugador
    print(movimiento)
    if movimiento == "IZQUIERDA":
        x -=1
    if movimiento == "DERECHA":
        x +=1
    if movimiento == "ARRIBA":
        y -= 1
    if movimiento == "ABAJO":
        y+=1
    return x,y
def obtener_movimientos(jugador):
    movimientos = ["Izquierda","Derecha","Arriba","Abajo"]
    x,y = jugador
    if x == 0:
        movimientos.remove("Izquierda")
    if x ==4:
        movimientos.remove("Derecha")
    if y == 0:
        movimientos.remove("Arriba")
    if y == 4:
        movimientos.remove("Abajo")
    return movimientos
def mapa(jugador):
    print(" _"*5)
    tile = "|{}"
    for cell in ESPACIO:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == jugador:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == jugador:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)
def game():
    monstruo,puerta,jugador = localizacion()
    while True:
            movimientos_validos = obtener_movimientos(jugador)
            mapa(jugador)
            print('Estas en la sala {}'.format(jugador))#posicion
            print('Puedes moverte hacia {}'.format(", ".join(movimientos_validos)))
            print('Usa WASD para moverte o Q para salir del juego')
            movimiento = input("> ")
            movimiento = movimiento.upper()
            movimientos_validos_upper = []
            for m in movimientos_validos:
                movimientos_validos_upper.append(m.upper())
            if movimiento == 'Q':
                break
            if movimiento in movimientos_validos_upper:
                jugador = mover_jugador(jugador, movimiento)

                if jugador == monstruo:
                    print("\n\n *Oh no! El monstruo te ha comido, suerte para el proximo intento!*\n\n")
                    break
                elif jugador == door:
                    print("\n\n Felicidades, has ganado!")
                    break
            else:
                print('\n\n*Cuidado con las paredes, estan bastante duras :3!*')
                clear()
                continue
            clear()

while True:
    print('Bienvenido a la mazmorra')
    input('Pulse enter para empezar')
    clear
    game()
