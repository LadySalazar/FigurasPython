from unittest import TestCase
from Circulo import Circulo
from Punto import Punto

class TestCirculo(TestCase):
    def test_hallar_area(self):
        a = Punto(0,0)
        c = Circulo(a,5)
        dist = c.hallarArea()
        self.assertEqual(dist,79)
    def test_hallar_perimetro(self):
        b = Punto(0,0)
        c2 = Circulo(b,5)
        dist = c2.hallarPerimetro()
        self.assertEqual(dist,31)
    def test_determinar_punto(self):
        b1 = Punto(-1, 0)
        b2 = Punto(4,0)
        c3 = Circulo(b1,4)
        dist = c3.DeterminarSiHayPunto(b2)
        self.assertEqual(dist,False)
