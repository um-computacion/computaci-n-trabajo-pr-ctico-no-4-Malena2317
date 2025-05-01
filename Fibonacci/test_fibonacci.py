import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_valores_positivos(self):

            """
            Prueba valores positivos comunes de la función fibonacci.
            Verifica que los primeros términos de la serie sean correctos.
            """

            self.assertEqual(fibonacci(1), 1)
            self.assertEqual(fibonacci(2), 1)
            self.assertEqual(fibonacci(3), 2)
            self.assertEqual(fibonacci(4), 3)
            self.assertEqual(fibonacci(5), 5)
            self.assertEqual(fibonacci(6), 8)
            self.assertEqual(fibonacci(10), 55)

    def test_cero(self):

            """
            Prueba el caso base cuando n = 0.
            El resultado debe ser 0.
            """
            self.assertEqual(fibonacci(0), 0)

    def test_negativo(self):

            """
            Verifica que la función lance un ValueError cuando se le pasa un número negativo.
            """
            with self.assertRaises(ValueError):
                fibonacci(-1)

if __name__ == '__main__':
    unittest.main()