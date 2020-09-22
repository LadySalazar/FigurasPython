import math

from Figura import Figura

class Circulo(Figura):

    def __init__(self, centro, radio):
        self.centro=centro
        self.radio=radio
    def hallarArea(self):
        totalArea= math.pi * self.radio ** 2
        return round(totalArea)
    def hallarPerimetro(self):
        totalPerimetro= 2 * math.pi * self.radio
        return round(totalPerimetro)
    def DeterminarSiHayPunto(self,p):
        return (p.hallarDistancia(self.centro)<=self.radio)