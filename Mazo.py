import Carta
import random as rd


class Baraja():
    def __init__(self):
        self.total = []

    def crearmazo(self):
        for i in range(1, 10):
            for j in ["Azul", "Rojo", "Verde", "Amarillo"] * 2:
                todaslascartas = Carta.Cartas(i, j, )
                self.total.append(todaslascartas)

        for i in range(0, 2):
            i = "@"
            for j in ["negro"] * 2:
                reversa = Carta.Cartas(i, j, )
                self.total.append(reversa)

        for i in range(0, 2):
            i = "+2"
            for j in ["Azul", "Rojo", "Verde", "Amarillo"] * 2:
                masDos = Carta.Cartas(i, j, )
                self.total.append(masDos)

        for i in range(0, 2):
            i = "*"
            for j in ["Azul", "Rojo", "Verde", "Amarillo"] * 2:
                pase = Carta.Cartas(i, j, )
                self.total.append(pase)

        for i in range(0, 2):
            i = "+4"
            for j in ["negro"] * 2:
                masCuatro = Carta.Cartas(i, j, )
                self.total.append(masCuatro)

        rd.shuffle(self.total)

    def tomarcarta(self):
        return self.total.pop()

    def dejarCarta(self, coso):
        self.total.append(coso)

    def __repr__(self):
        return f"{self.total})"

    def __str__(self):
        return f"{self.total})"
