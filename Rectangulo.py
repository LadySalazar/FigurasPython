from Figura import Figura

class Rectangulo(Figura):

    def __init__(self, punto1, punto2,punto3,punto4):
        self.punto1=punto1
        self.punto2=punto2
        self.punto3=punto3
        self.punto4=punto4
        self.distancia1=self.punto1.hallarDistancia(self.punto2)
        self.distancia2=self.punto2.hallarDistancia(self.punto3)
        self.distancia3=self.punto3.hallarDistancia(self.punto4)
        self.distancia4=self.punto4.hallarDistancia(self.punto1)

    def hallarArea(self):
        totalArea = self.distancia1*self.distancia2;
        return round(totalArea)

    def hallarPerimetro(self):
        totalPerimetro = self.distancia1 + self.distancia2 + self.distancia3 + self.distancia4
        return round(totalPerimetro)
