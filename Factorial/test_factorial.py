import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    
    def test_factorial_0(self):
        # El factorial de 0 debe ser 1
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_enteros(self):
        # El factorial de 1 , 10 y 5 debe ser 1,3628800 y 120
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_negativo(self):
        # Los números negativos deberían dar error
        with self.assertRaises(ValueError):
            factorial(-1)
    
    def test_factorial_decimal(self):
        # Los números decimales deberían dar error
        with self.assertRaises(ValueError):
            factorial(1.5)


# Para poder ejecutar los tests
if __name__ == "__main__":
    unittest.main()