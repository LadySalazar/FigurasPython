from unittest import TestCase

from Circulo import Circulo
from Punto import Punto


class TestCirculo(TestCase):
    def test_hallar_area(self):
        a = Punto(0,0)
        c = Circulo(a,5)
        dist = c.hallarArea()
        self.assertEqual(dist,79)
