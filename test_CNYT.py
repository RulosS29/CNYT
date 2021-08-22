from CNYT import*
import unittest


class TestCNYT(unittest.TestCase):

    def test_suma(self):
        print("-----Test Suma-----")
        self.assertEqual(suma(0j, 0j), 0)
        self.assertEqual(suma(5+6j, 5), 10+6j)
        self.assertEqual(suma(5, 1j), 5+1j)
        self.assertEqual(suma(0, 7-9j), 7-9j)
        self.assertEqual(suma(2j, -2j), 0)
        self.assertEqual(suma(481-9597j, -486251+9862j), -485770+265j)

    def test_producto(self):
        print("-----Test producto-----")
        self.assertEqual(producto(0j, 0j), 0)
        self.assertEqual(producto(5 + 6j, 8), 40 + 48j)
        self.assertEqual(producto(5, 1j), 5j)
        self.assertEqual(producto(0, 7 - 9j), 0)
        self.assertEqual(producto(2j, -2j), 4)
        self.assertEqual(producto(481 - 959j, -486 + 986j), 711808 + 940340j)

    def test_resta(self):
        print("-----Test resta-----")
        self.assertEqual(resta(0j, 0j), 0)
        self.assertEqual(resta(5 + 6j, 8), -3 + 6j)
        self.assertEqual(resta(5, 1j), 5-1j)
        self.assertEqual(resta(0, 7 - 9j), -7+9j)
        self.assertEqual(resta(2j, -2j), 4j)
        self.assertEqual(resta(481 - 959j, -486 + 986j), 967 - 1945j)

    def test_division(self):
        print("-----Test division-----")
        self.assertEqual(division(0j, 0j), "No es posible")
        self.assertEqual(division(5 + 6j, 8), 0.625 + 0.75j)
        self.assertEqual(division(5, 1j), -5j)
        self.assertEqual(division(0, 7 - 9j), "No es posible")
        self.assertEqual(division(2j, -2j), -1)
        self.assertEqual(division(481 - 959j, -486 + 986j), -0.9759581327913458-0.006779257062277804j)

    def test_modulo(self):
        print("-----Test modulo-----")
        self.assertEqual(modulo(0+0j), 0)
        self.assertAlmostEqual(modulo(5 + 6j), 7.81024967590)
        self.assertEqual(modulo(5), 5)
        self.assertEqual(modulo(0+1j), 1)
        self.assertEqual(modulo(2j), 2)
        self.assertAlmostEqual(modulo(481 - 959j), 1072.866254479)

    def test_conjugado(self):
        print("-----Test conjugado-----")
        self.assertEqual(conjugado(0+0j), 0)
        self.assertEqual(conjugado(5 + 6j), 5-6j)
        self.assertEqual(conjugado(5), 5)
        self.assertEqual(conjugado(0+1j), -1j)
        self.assertEqual(conjugado(-2j), 2j)
        self.assertEqual(conjugado(481 - 959j), 481 + 959j)

    def test_conversionp(self):
        print("-----Test Conversion Polar-----")
        self.assertEqual(conversionp(0+0j), (0, 0))
        self.assertEqual(conversionp(0 + 6j), "No es posible")
        self.assertEqual(conversionp(10-4j), (10.770329614269007, -0.3805063771123649))

    def test_conjugadoc(self):
        print("-----Test Conversion Cartesianas-----")
        self.assertEqual(conversionc(0, 0), 0)
        self.assertEqual(conversionc(1.03, 1.25), (-0.8280574348472294+0.6125527606616648j))
        self.assertEqual(conversionc(0.23, 0), (0.23+0j))

    def test_retonar(self):
        print("-----Test Conversion Cartesianas-----")
        self.assertEqual(retonar(0+0j), 0)
        self.assertAlmostEqual(retonar(5 + 8j), 1.01219701)
        self.assertAlmostEqual(retonar(12-3j), -0.24497866)




if __name__ == "__main__":
    unittest.main()