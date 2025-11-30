import Mazo


class Player:
    def __init__(self):
        self.mano = []

    def robar(self, mazo):
        isinstance(mazo, Mazo.Baraja)
        self.mano.append(mazo.tomarcarta())

    def iniciar(self, mazo):
        isinstance(mazo, Mazo.Baraja)
        for _ in range(7):
            self.mano.append(mazo.tomarcarta())

    def dejar(self, mazo, carta):
        isinstance(mazo, Player)
        mazo.mano.append(self.mano.pop(carta))

    def __repr__(self):
        return f"{self.mano}"

    def __str__(self):
        return f"{self.mano}"
