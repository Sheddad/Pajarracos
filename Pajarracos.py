###############################################################################
# EMULADOR DE JUEGOC DE CARTAS(FILLER) "PAJARRACOS"
#
#
# Autores (por orden alfabético):
#
# Kaid-Salah Ferrón, Sheddad (SKF)
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


class miCarta():
    """Clase de Objeto Carta."""

    def __init__(self, numero, clase, tipo):
        """Este es el docstring del inicializador de la clase Carta."""
        self.n = numero
        """NORMAL, ESPECIAL."""
        self.c = clase
        "ESPANTAPÁJARO, PAJARRACO, CEREZA, MANZANA, NARANJA, PLÁTANO, UVA."
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


# Número de cartas
lista_cartas = []
print(len(lista_cartas))

# Creamos las 10 cartas de ESPANTAPÁJAROS (0-9)
for i in range(10):
    lista_cartas.append(miCarta(i, cte.NORMAL, cte.ESPANTAPAJARO))
    print (i) # prueba

# Tenemos en cuenta el número de cartas anteriores utilizamos n
print(len(lista_cartas))
n = len(lista_cartas)
for i in range(8):
    lista_cartas.append(miCarta(i + n, cte.NORMAL, cte.CEREZA))

# imprimimos las cartas
for i in lista_cartas:
    print("Número: " + str(i.n) + " Clase: " + switch_info(i.c) + " Tipo: " + switch_info(i.t))
