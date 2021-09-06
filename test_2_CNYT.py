from Biblioteca_2 import *
import unittest


class TestCNYT(unittest.TestCase):

    def test_sumavecomp(self):
        print("-----Test Suma de Vectores-----")
        self.assertEqual(sumavecomp([(1, -2.5), (2, 1)], [(3, 0), (7, -3.8)]), ([(4, -2.5), (9, -2.8)]))
        self.assertEqual(sumavecomp([(0, 0), (0, 0)], [(0, 0), (0, 0)]), ([(0, 0), (0, 0)]))
        self.assertEqual(sumavecomp([(1, 1), (1, 1)], [(1, 1), (1, 1)]), ([(2, 2), (2, 2)]))

    def test_inversoad(self):
        print("-----Test Inverso-----")
        self.assertEqual(inversoad([(1, -2.5), (2, 1)]), ([(-1, 2.5), (-2, -1)]))
        self.assertEqual(inversoad([(-5, -2.5), (7, 0)]), ([(5, 2.5), (-7, 0)]))
        self.assertEqual(inversoad([(9, -15.8), (0, 0)]), ([(-9, 15.8), (0, 0)]))

    def test_mulxc(self):
        print("-----Test de un Vector por un Escalar-----")
        self.assertEqual(mulxc([(1, -2.5), (2, 1)], 3), ([(3, -7.5), (6, 3)]))
        self.assertEqual(mulxc([(8, 9), (1, -5)], 0), ([(0, 0), (0, 0)]))
        self.assertEqual(mulxc([(-15, -2.1), (-0.5, 3)], 1), ([(-15, -2.1), (-0.5, 3)]))

    def test_sumatri(self):
        print("-----Test Adición de Matrices-----")
        self.assertEqual(sumatri([[(1, 5), (1, 3)], [(2, 1), (1, 4)]], [[(1, -2.5), (1, -2.5)], [(2, 1), (1, -2.5)]]), [[(2, 2.5), (2, 0.5)], [(4, 2), (2, 1.5)]])
        self.assertEqual(sumatri([[(0, 0), (0, 0)], [(0, 0), (0, 0)]], [[(0, 0), (0, 0)], [(0, 0), (0, 0)]]), [[(0, 0), (0, 0)], [(0, 0), (0, 0)]])
        self.assertEqual(sumatri([[(1, 2), (3, 4)], [(1, 2), (3, 4)]], [[(4, 3), (2, 1)], [(4, 3), (2, 1)]]), [[(5, 5), (5, 5)], [(5, 5), (5, 5)]])

    def test_multimxc(self):
        print("-----Test Multiplicacion de una Matriz por un Escalar-----")
        self.assertEqual(multimxc([[(1, 5), (1, 3)], [(2, 1), (1, 4)]], 0), [[(0, 0), (0, 0)], [(0, 0), (0, 0)]])
        self.assertEqual(multimxc([[(1, 1), (1, 1)], [(1, 1), (1, 1)]], 10), [[(10, 10), (10, 10)], [(10, 10), (10, 10)]])
        self.assertEqual(multimxc([[(5, -5.6), (7, -4.8)], [(45, -6), (-1, 2)]], 2), [[(10, -11.2), (14, -9.6)], [(90, -12), (-2, 4)]])

    def test_adjunta(self):
        print("-----Test Adjunta de una Matriz-----")
        self.assertEqual(adjunta([[(1, 5), (1, 3)], [(2, 1), (1, 4)]]), [[(1, -5), (2, -1)], [(1, -3), (1, -4)]])
        self.assertEqual(adjunta([[(1, 1), (0, 0)], [(0, 0), (1, 1)]]), [[(1, -1), (0, 0)], [(0, 0), (1, -1)]])
        self.assertEqual(adjunta([[(-5, 1), (4, 3.6)], [(2.1, -8.1), (-1, 43)]]), [[(-5, -1), (2.1, 8.1)], [(4, -3.6), (-1, -43)]])


if __name__ == "__main__":
    unittest.main()