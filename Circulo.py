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

    def hallarPerimetro(self):
        totalPerimetro= 2 * math.pi * self.radio
        return round(totalPerimetro)
    def DeterminarSiHayPunto(self,p):
        distancia1 = p.hallarDistancia(self.centro)
        if distancia1<=self.radio:
            respuesta = True;
        else:
            respuesta = False;
        return (respuesta)