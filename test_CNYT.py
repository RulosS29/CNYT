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


if __name__ == "__main__":
    unittest.main()