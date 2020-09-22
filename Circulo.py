import math

from Figura import Figura
from Punto import Punto


class Circulo(Figura):

    def __init__(self, centro, radio):
        self.centro=centro
        self.radio=radio
    def hallarArea(self):
        totalArea= math.pi * self.radio ** 2
        return round(totalArea)
