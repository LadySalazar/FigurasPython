from unittest import TestCase

from Punto import Punto
from Rectangulo import Rectangulo

class TestRectangulo(TestCase):
    def test_hallar_area(self):
        a1 = Punto(-1,0)
        a2 = Punto(1,0)
        a3 = Punto(1,1)
        a4 = Punto(-1,1)
        rectan = Rectangulo(a1, a2, a3, a4)
        dist = rectan.hallarArea()
        self.assertEqual(dist, 2)
    def test_hallar_perimetro(self):
        b1 = Punto(-1,0)
        b2 = Punto(1,0)
        b3 = Punto(1,1)
        b4 = Punto(-1,1)
        rectan2 = Rectangulo(b1, b2, b3,b4)
        dist2 = rectan2.hallarPerimetro()
        self.assertEqual(dist2, 6)
