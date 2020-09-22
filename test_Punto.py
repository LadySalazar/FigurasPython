from unittest import TestCase

from Punto import Punto

class TestPunto(TestCase):
    def test_punto(self):
        a = Punto(1, 0)
        b = Punto(-1, 0)
        dist = a.hallarDistancia(b)
        self.assertEqual(dist,2)
