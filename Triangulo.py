import math

from Figura import Figura

class Triangulo(Figura):

    def __init__(self, punto1, punto2,punto3):
        self.punto1=punto1
        self.punto2=punto2
        self.punto3=punto3
        self.distancia1=self.punto1.hallarDistancia(self.punto2)
        self.distancia2=self.punto2.hallarDistancia(self.punto3)
        self.distancia3=self.punto3.hallarDistancia(self.punto1)

    def hallarArea(self):
        s= (self.distancia1+self.distancia2+self.distancia3)/2
        totalArea = (s * (s - self.distancia1) * (s - self.distancia2) * (s - self.distancia3))**(1/2);
        return round(totalArea)

    def hallarPerimetro(self):
        totalPerimetro = self.distancia1 + self.distancia2 + self.distancia3
        return round(totalPerimetro)

    def TipoTriangulo(self):
        d1=round(self.distancia1)
        d2=round(self.distancia2)
        d3=round(self.distancia3)
        if d1==d2 & d1==d3:
            TipoT = "Equilatero"
        else:
            if (d1==d2 & d1!=d3)or(d3==d2 & d2!=d3)or(d1==d3 & d2!=d3):
                TipoT = "Isoceles"
            else:
                if (d1!=d2 & d2!=d3 & d3!=d1):
                    TipoT = "Escaleno"
        return TipoT