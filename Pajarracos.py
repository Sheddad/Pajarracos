###############################################################################
# EMULADOR DE JUEGOC DE CARTAS(FILLER) "PAJARRACOS"
#
# Kaid-Salah Ferrón, Sheddad (SKF)
# Agosto 2020
# Continuación Agosto 2021
###############################################################################

import random

import constantes as cte


###############################################################################
# CLASE/OBJETO CARTA
#
# ESPANTAPÁJAROS (10+0)
# PAJARRACOS (8+2)
# CEREZAS (8+1)
# MANZANAS (8+1)
# NARANJAS (8+1)
# PLÁTANOS (8+1)
# UVAS (8+1)
###############################################################################
class Carta():
    """Clase de Objeto Carta."""

    def __init__(self, numero, clase, tipo):
        """Este es el docstring del inicializador de la clase Carta."""
        self.n = numero
        """NORMAL, ESPECIAL."""
        self.c = clase
        """ESPANTAPÁJARO, PAJARRACO, CEREZA, MANZANA, NARANJA, PLÁTANO, UVA."""
        self.t = tipo


###############################################################################
# CLASE/OBJETO JUGADOR
###############################################################################
class Jugador():
    """Clase de Objeto Jugador."""

    def __init__(self, numero):
        """Este es el docstring del inicializador de la clase Jugador."""
        self.n = numero

    # La mano del jugador solo será de 3 cartas
    mano = [3]



###############################################################################
# swich para relacionar constantes con texto
###############################################################################
def switch_info(argument):
    switcher = {
        cte.NORMAL: "NORMAL",
        cte.ESPECIAL: "ESPECIAL",
        cte.PAJARRACO: "PAJARRACO",
        cte.ESPANTAPAJARO: "ESPANTAPAJARO",
        cte.CEREZA: "CEREZA",
        cte.MANZANA: "MANZANA",
        cte.NARANJA: "NARANJA",
        cte.PLATANO: "PLATANO",
        cte.UVA: "UVA",
    }
    return switcher.get(argument, "Carta Inválida")


###############################################################################
# Función que nos permite crear una cantidad de cartas de una clase y un tipo #
###############################################################################
def crear_carta (clase, tipo, cantidad):
    """Función para crear una cantidad de cartas de una clase y un tipo"""
    n = len(lista_cartas)
    # Tenemos en cuenta el número de cartas anteriores; utilizamos n
    for i in range(cantidad):
        lista_cartas.append(Carta(i + n, tipo, clase))

###############################################################################
# Función que nos permite ver una carta
###############################################################################
def ver_carta (carta):
    """Función que nos permite ver una carta"""
    print("Número: " + str(carta.n) + " Clase: " + switch_info(carta.c) + " Tipo: "
    + switch_info(carta.t))

###############################################################################
# Función que nos permite ver una lista de cartas
###############################################################################
def ver_cartas (lista):
    """Función que nos permite ver una lista de cartas"""
    for c in lista:
        ver_carta(c)

###############################################################################
# Función que nos permite ver los jugadores
###############################################################################
def ver_jugadores (lista):
    """Función que nos permite ver una lista de cartas"""
    for j in lista:
        print("Número: " + str(j.n))


###############################################################################
#                                   Main
###############################################################################

# Creamos una lista de objetos Carta
lista_cartas = []
# Número de cartas
print(len(lista_cartas))

# Creamos toda la baraja de cartas, en total 65 cartas
crear_carta(cte.NORMAL, cte.ESPANTAPAJARO, 10)
crear_carta(cte.NORMAL, cte.PAJARRACO, 8)
crear_carta(cte.ESPECIAL, cte.PAJARRACO, 2)
crear_carta(cte.NORMAL, cte.CEREZA, 8)
crear_carta(cte.ESPECIAL, cte.CEREZA, 1)
crear_carta(cte.NORMAL, cte.MANZANA, 8)
crear_carta(cte.ESPECIAL, cte.MANZANA, 1)
crear_carta(cte.NORMAL, cte.NARANJA, 8)
crear_carta(cte.ESPECIAL, cte.NARANJA, 1)
crear_carta(cte.NORMAL, cte.PLATANO, 8)
crear_carta(cte.ESPECIAL, cte.PLATANO, 1)
crear_carta(cte.NORMAL, cte.UVA, 8)
crear_carta(cte.ESPECIAL, cte.UVA, 1)

# Vemos las cartas
ver_cartas(lista_cartas)

# Creamos la baraja y la barajamos
baraja = lista_cartas # Copiamos
# Modifica el orden de la lista de forma aleatoria
random.shuffle(baraja)

# Vemos como han quedado barajadas las cartas
ver_cartas(baraja)

# Creamos la lista de jugadores.
num_jugadores = 3 # De momento empezamos con 3
# Creamos una lista de objetos Jugador
lista_jugadores = []
for i in range(num_jugadores):
    lista_jugadores.append(Jugador(i + 1))
# Visualizamos a los jugadores
ver_jugadores(lista_jugadores)

jugador1 = Jugador(1)
#jugador1.mano[0] = baraja[0]
jugador1.mano[0] = baraja.pop()
#print (jugador1.mano[0])
ver_carta (jugador1.mano[0])
print ("Hola")

ver_cartas(baraja)
