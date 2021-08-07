###############################################################################
# EMULADOR DE JUEGOC DE CARTAS(FILLER) "PAJARRACOS"
#
# Kaid-Salah Ferrón, Sheddad (SKF)
# Agosto 2020
# Continuación Agosto 2021
###############################################################################

import constantes as cte


###############################################################################
# CLASE/OBJETO CARTA
#
# PAJARRACOS (8+2)
# ESPANTAPÁJAROS (10+0)
# CEREZAS (8+1)
# MANZANAS (8+1)
# NARANJAS (8+1)
# PLÁTANOS (8+1)
# UVAS (8+1)
###############################################################################

# Clase de objeto Carta
class Carta():
    """Clase de Objeto Carta."""

    def __init__(self, numero, clase, tipo):
        """Este es el docstring del inicializador de la clase Carta."""
        self.n = numero
        """NORMAL, ESPECIAL."""
        self.c = clase
        """ESPANTAPÁJARO, PAJARRACO, CEREZA, MANZANA, NARANJA, PLÁTANO, UVA."""
        self.t = tipo


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


# Función que nos permite crear una cantidad de cartas de una clase y un tipo
def crear_carta (clase, tipo, cantidad):
    """Función para crear una cantidad de cartas de una clase y un tipo"""
    n = len(lista_cartas)
    # Tenemos en cuenta el número de cartas anteriores utilizamos n
    for i in range(cantidad):
        lista_cartas.append(Carta(i + n, tipo, clase))


# Creamos una lista de objetos Carta
lista_cartas = []
# Número de cartas
print(len(lista_cartas))

# Creamos toda la baraja de cartas, en total 65 cartas
crear_carta(cte.NORMAL, cte.PAJARRACO, 8)
crear_carta(cte.ESPECIAL, cte.PAJARRACO, 2)
crear_carta(cte.NORMAL, cte.ESPANTAPAJARO, 10)
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

# imprimimos las cartas
for i in lista_cartas:
    print("Número: " + str(i.n) + " Clase: " + switch_info(i.c) + " Tipo: "
     + switch_info(i.t))
