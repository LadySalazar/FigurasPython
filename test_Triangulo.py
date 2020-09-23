from unittest import TestCase

from Punto import Punto
from Triangulo import Triangulo


class TestTriangulo(TestCase):
    def test_hallar_area(self):
        a1 = Punto(0,-3)
        a2 = Punto(4,0)
        a3 = Punto(0,3)
        triang = Triangulo(a1, a2, a3)
        dist = triang.hallarArea()
        self.assertEqual(dist, 12)
    def test_hallar_perimetro(self):
        b1 = Punto(0,-3)
        b2 = Punto(4,0)
        b3 = Punto(0,3)
        triang2 = Triangulo(b1, b2, b3)
        dist2 = triang2.hallarPerimetro()
        self.assertEqual(dist2, 16)
    def test_hallar_TipoTriangulo(self):
        c1 = Punto(-0.5,0)
        c2 = Punto(0.5,0)
        c3 = Punto(0,1)
        triang3 = Triangulo(c1, c2, c3)
        dist3 = triang3.TipoTriangulo()
        self.assertEqual(dist3,"Equilatero")