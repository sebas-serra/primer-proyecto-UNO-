import tkinter as tk


class Cartas:

    def __init__(self, numero, color):
        self.numero = numero
        self.color = color

    def __repr__(self):
        return f"({self.numero!r}, {self.color!r})"

    def __str__(self):
        return f"({self.numero!r}, {self.color!r})"

    def mostrarCarta(self, frame):
        if self.color == "Azul":
            color = "blue"
        elif self.color == "Amarillo":
            color = "yellow"
        elif self.color == "Rojo":
            color = "red"
        elif self.color == "Verde":
            color = "green"
        elif self.color == "negro":
            color = "#352e48"

        boton = tk.Button(frame, bg=color, text=self.numero, font=(
            "Arial", 46), width=2, height=1)

        return boton

    def comprobar(self, pila):
        isinstance(pila, Cartas)
        if self.color == pila.color or self.numero == pila.numero or self.color == "negro":
            return True
        else:
            return False
