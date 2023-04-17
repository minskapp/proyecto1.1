#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
# from time import sleep
import random


def presentacion_1():
    ''' Devuelve nivel de juego '''
    print(" Tres en raya \n \n Seleccione un nivel: ")
    print(" 1. Fácil ")
    print(" 2. Difícil (por definir) \n")
    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input(" --> ")
    return int(nivel)


def presentacion_2():
    ''' Devuelve ficha elegida por el usuario y ficha del ordenador `'''
    print(" \n Juego Tres en raya \n")
    print("~Comienza el juego la ficha O~ \n")
    print(" Elegir ficha: O / X \n")
    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input(" --> ").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else:
        humano = "X"
        ordenador = "O"
    return humano, ordenador


def mostrar_tablero(tablero):
    ''' Muestra e tablero '''
    print("\n Juego Tres en raya \n ")
    print(" 1 | 2 | 3 ")
    print(" {} | {} | {}".format(tablero[0], tablero[1], tablero[2]))
    print(" -----------+----------+-------")
    print(" 4 | 5 | 6 ")
    print(" {} | {} | {}".format(tablero[3], tablero[4], tablero[5]))
    print(" -----------+----------+-------")
    print(" 7 | 8 | 9 ")
    print(" {} | {} | {}".format(tablero[6], tablero[7], tablero[8]))
    print(" -----------+----------+-------")
    print()
    print()


def seguir_jugando():
    ''' devuelve True si el jugador quiere seguir jugando '''
    print()
    respuesta = input(" Desea seguir jugando (s) ? ").lower()
    if respuesta == "s" or respuesta == "si":
        return True

    return False


def hay_ganador(tablero, jugador):
    ''' Comprueba si hay ganador'''
    if (tablero[0] == tablero[1] == tablero[2] == jugador or tablero[3] == tablero[4] == tablero[5] == jugador or
            tablero[6] == tablero[7] == tablero[8] == jugador or tablero[0] == tablero[3] == tablero[6] == jugador or
            tablero[1] == tablero[4] == tablero[7] == jugador or tablero[2] == tablero[5] == tablero[8] == jugador or
            tablero[0] == tablero[4] == tablero[8] == jugador or tablero[2] == tablero[4] == tablero[6] == jugador):
        return True
    return False


## Método mejorado ##
def tablero_lleno(tablero):
    # Regresa un True si el tablero está lleno o False en caso contrario
    for i in tablero:
        if i == " ":
            return False

    return True


def casilla_libre(tablero, casilla):
    '''devuelve True si una casilla dada (seleccionada) está vacia y False en caso contrario
    '''
    return tablero[casilla] == " "


def movimiento_jugador(tablero):
    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input(" Turno para jugar (1 a 9) - Terminar la partida (0) ")
            # implementacion nueva, opcion nueva = 0
            if posicion == "0":
                return "-1"
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print(" Casilla no está libre")
            else:
                return posicion - 1

# Método el cual sirve para atacar o defenderse, dependiendo de la ficha que se le pase (ordenador para atacar,
# humano para defenderse)
def jugada_estrategica(tablero, jugador):
    casilla = -1
    if (tablero[0] == tablero[1] == jugador and tablero[2] == " ") or (tablero[5] == tablero[8] == jugador
        and tablero[2] == " ") or (tablero[6] == tablero[4] == jugador and tablero[2] == " "):
        casilla = 2
    elif (tablero[0] == tablero[2] == jugador and tablero[1] == " ") or (tablero[4] == tablero[7] == jugador
                                                                         and tablero[1] == " "):
        casilla = 1
    elif (tablero[1] == tablero[2] == jugador and tablero[0] == " ") or (tablero[3] == tablero[6] == jugador
         and tablero[0] == " ") or (tablero[4] == tablero[8] == jugador and tablero[0] == " "):
        casilla = 0
    elif (tablero[3] == tablero[4] == jugador and tablero[5] == " ") or (tablero[2] == tablero[8] == jugador
                                                                         and tablero[5] == " "):
        casilla = 5
    elif (tablero[3] == tablero[5] == jugador and tablero[4] == " ") or (tablero[1] == tablero[7] == jugador
          and tablero[4] == " ") or (tablero[2] == tablero[6] == jugador and tablero[4] == " ") or (tablero[0]
          == tablero[8] == jugador and tablero[4] == " "):
        casilla = 4
    elif (tablero[4] == tablero[5] == jugador and tablero[3] == " ") or (tablero[0] == tablero[6] == jugador
                                                                         and tablero[3] == " "):
        casilla = 3
    elif (tablero[6] == tablero[7] == jugador and tablero[8] == " ") or (tablero[2] == tablero[5] == jugador
        and tablero[8] == " ") or (tablero[0] == tablero[4] == jugador and tablero[8] == " "):
        casilla = 8
    elif (tablero[6] == tablero[8] == jugador and tablero[7] == " ") or (tablero[1] == tablero[4] == jugador
        and tablero[7] == " "):
        casilla = 7
    elif (tablero[7] == tablero[8] == jugador and tablero[6] == " ") or (tablero[0] == tablero[3] == jugador
        and tablero[6] == " ") or (tablero[2] == tablero[4] == jugador and tablero[6] == " "):
        casilla = 6
    return casilla


def mov_ordenador_facil(tablero, jugador):
    ''' En este tipo de jugada, el ordenador se defiende de no ser ganado en la siguiente
    jugada '''
    casilla = jugada_estrategica(tablero, jugador)
    if casilla != -1:
        return casilla
    while True:
        casilla = random.randint(0, 8)
        if tablero[casilla] == " ":
            return casilla


# Método que verifica si los extremos del tablero están vacíos y retorna la casilla a jugar
def extremos_vacios(tablero):
    if tablero[1] != " " and tablero[0] == " ":
        return 0
    elif tablero[1] != " " and tablero[2] == " ":
        return 2
    elif tablero[6] == " ":
        return 6
    elif tablero[8] == " ":
        return 8

# Método que retorna la cantidad de fichas que hay en el tablero
def cantidad_fichas_tablero(tablero):
    cantidad = 0
    for casilla in tablero:
        if casilla != " ":
            cantidad += 1
    return cantidad

# Método que retorna la posición de una ficha en el tablero, el parámetro "casillas" solo sirve en caso que sea
# distinto de cero, y sirve para buscar solo en casillas específicas la ficha de un jugador en el tablero, en caso
# contrario, se busca la ficha en todo el tablero sin distinción
def encontrar_ficha(tablero, casillas, jugador):
    if casillas == 0:
        return tablero.index(jugador)
    for i in range(len(casillas)):
        if tablero[casillas[i]] == jugador:
            return casillas[i]

# Método que ataca, hace llamado del método jugada_estrategica() y envía
# por parámetro la ficha con la que el ordenador juega, en caso de no retornar
# ningún elemento, quiere decir que no hay jugadas para atacar
def atacar(tablero, ordenador):
    casilla_ordenador = jugada_estrategica(tablero, ordenador)
    if casilla_ordenador != -1:
        return casilla_ordenador

# Método que defiende, hace llamado del método jugada_estrategica() y envía
# por parámetro la ficha con la que el humano juega, en caso de no retornar
# ningún elemento, quiere decir que no hay jugadas para defender
def defender(tablero, humano):
    casilla_ordenador = jugada_estrategica(tablero, humano)
    if casilla_ordenador != -1:
        return casilla_ordenador


def mov_ordenador_dificil(tablero, ordenador, humano):
    # Comienza atacando
    jugada_atacar = atacar(tablero, ordenador)
    if jugada_atacar != None:
        return jugada_atacar

    # Si no puede atacar, se defiende
    jugada_defender = defender(tablero, humano)
    if jugada_defender != None:
        return jugada_defender

    # Casillas en los extremos, o diagonales
    extremos = [0, 2, 6, 8]
    # Casillas en los laterales (arriba, abajo, derecha, izquierda de casilla de al medio)
    laterales = [1, 3, 5, 7]

    # Si es la primera jugada, juega al medio
    if cantidad_fichas_tablero(tablero) == 0:
        # Si el tablero esta vacío y poner ficha al medio
        return 4
    # Si comienza el humano jugando, entonces intentar poner la ficha al medio, sino entonces en los extremos
    elif cantidad_fichas_tablero(tablero) == 1:
        casilla_humano = encontrar_ficha(tablero, 0, humano)
        if casilla_humano in extremos or casilla_humano in laterales:
            return 4
        while True:
            casilla = random.choice(extremos)
            if tablero[casilla] == " ":
                return casilla
    # Retomando la partida cuando el ordenador juega primero (turno 2 del ordenador),
    # analizar en que casilla jugó el humano y tomar la mejor decisión dependiendo del algortimo
    elif cantidad_fichas_tablero(tablero) == 2:
        casilla_humano = encontrar_ficha(tablero, 0, humano)
        if casilla_humano == 3:
            while True:
                casilla = random.choice([0, 6])
                if tablero[casilla] == " ": return casilla
        elif casilla_humano == 5:
            while True:
                casilla = random.choice([2, 8])
                if tablero[casilla] == " ": return casilla
        elif casilla_humano == 1:
            while True:
                casilla = random.choice([0, 2])
                if tablero[casilla] == " ": return casilla
        elif casilla_humano == 7:
            while True:
                casilla = random.choice([6, 8])
                if tablero[casilla] == " ": return casilla
        elif casilla_humano == 0: return 8
        elif casilla_humano == 2: return 6
        elif casilla_humano == 6: return 2
        elif casilla_humano == 8: return 0
    # Retomando la partida cuando el humano juega primero (turno 2 ordenador) se deberá analizar
    # la casilla de la ficha del humano, y en caso de que el humano haya jugado al medio, jugar
    # en los laterales, en caso contrario, jugar en los extremos
    elif cantidad_fichas_tablero(tablero) == 3:
        casilla_ordenador = encontrar_ficha(tablero, 0, ordenador)
        if casilla_ordenador == 4:
            while True:
                casilla = random.choice(laterales)
                if tablero[casilla] == " ":
                    return casilla
        while True:
            casilla = random.choice(extremos)
            if tablero[casilla] == " ":
                return casilla
    # Retomando la partida cuando el ordenador ha jugado primero (turno 3 ordenador), jugar en el extremo
    # donde no hay fichas en los laterales
    elif cantidad_fichas_tablero(tablero) == 4:
        casilla_ordenador = encontrar_ficha(tablero, extremos, ordenador)
        if (casilla_ordenador == 0 and tablero[3] != " ") or (casilla_ordenador == 8 and tablero[7] != " "):
            return 2
        elif (casilla_ordenador == 0 and tablero[1] != " ") or (casilla_ordenador == 8 and tablero[5] != " "):
            return 6
        elif (casilla_ordenador == 2 and tablero[1] != " ") or (casilla_ordenador == 6 and tablero[3] != " "):
            return 8
        elif (casilla_ordenador == 2 and tablero[5] != " ") or (casilla_ordenador == 6 and tablero[7] != " "):
            return 0
        else:
            while True:
                casilla = random.choice(extremos)
                if tablero[casilla] == " ": return casilla
    # Si no se cumple ningún caso anterior, generar una casilla aleatoria que esté vacía
    while True:
        casilla = random.randint(0, 8)
        if tablero[casilla] == " ":
            return casilla


def estadisticas():
    partidas_totales = partidas_ganadas + partidas_perdidas + partidas_empatadas + partidas_canceladas
    porcentaje_partidas_ganadas = partidas_ganadas / partidas_totales
    print(f"Has ganado el {porcentaje_partidas_ganadas}% de las partidas totales")
    porcentaje_partidas_perdidas = partidas_perdidas / partidas_totales
    print(f"Has perdido el {porcentaje_partidas_perdidas}% de las partidas totales")
    porcentaje_partidas_empatadas = partidas_empatadas / partidas_totales
    print(f"Has empatado el {porcentaje_partidas_empatadas}% de las partidas totales")
    porcentaje_partidas_canceladas = partidas_canceladas / partidas_totales
    print(f"Has cancelado el {porcentaje_partidas_canceladas}% de las partidas totales")
    tiempo_promedio_jugadas = sum(tiempo_jugadas) / partidas_totales
    print(f"El tiempo promedio de tus partidas fue de {tiempo_promedio_jugadas}")


## programa principal ##
tiempo_inicio = 0
tiempo_final = 0
jugador = True
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0
partidas_totales = 0
partidas_canceladas = 0
tiempo_jugadas = []
tiempo_promedio_jugadas = 0

while jugador:
    tablero = [" "] * 9
    nivel = presentacion_1()
    humano, ordenador = presentacion_2()
    mostrar_tablero(tablero)
    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"
    partida = True
    tiempo_inicio = time.time()
    while partida:
        if tablero_lleno(tablero):
            print(" Empate ! ")
            partidas_empatadas += 1
            partida = False
            tiempo_final = time.time()
            tiempo_jugadas.append(tiempo_final - tiempo_inicio)
            print(tiempo_jugadas)

        elif turno == "Humano":
            casilla = movimiento_jugador(tablero)
            # Partida cancelada
            if casilla == "-1":
                print("Partida cancelada")
                partidas_canceladas += 1
                partida = False
                tiempo_final = time.time()
                tiempo_jugadas.append(tiempo_final - tiempo_inicio)

            else:
                tablero[casilla] = humano
                turno = "Ordenador"
                mostrar_tablero(tablero)
                if hay_ganador(tablero, humano):
                    partidas_ganadas += 1
                    print(" Has ganado !! ")
                    partida = False
                    tiempo_final = time.time()
                    tiempo_jugadas.append(tiempo_final - tiempo_inicio)
        elif turno == "Ordenador":
            print(" Ordenador está pensando su jugada ... ")
            time.sleep(1)
            if nivel == 1:
                casilla = mov_ordenador_facil(tablero, humano)
            elif nivel == 2:
                casilla = mov_ordenador_dificil(tablero, ordenador, humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            mostrar_tablero(tablero)
            if hay_ganador(tablero, ordenador):
                partidas_perdidas += 1
                print(" Has perdido ")
                partida = False
                tiempo_final = time.time()
                tiempo_jugadas.append(tiempo_final - tiempo_inicio)

    jugador = seguir_jugando()

estadisticas()
