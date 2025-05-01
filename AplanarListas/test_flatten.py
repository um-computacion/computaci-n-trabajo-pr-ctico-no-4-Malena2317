import unittest
from flatten import aplanar_lista

class TestAplanarLista(unittest.TestCase):

    def test_lista_simple(self):
        """
        Prueba para una lista simple, sin elementos anidados.
        """
        lista = [1, 2, 3, 4]
        resultado_esperado = [1, 2, 3, 4]
        self.assertEqual(aplanar_lista(lista), resultado_esperado)
    
    def test_lista_anidada(self):
        """
        Prueba para una lista anidada, que contiene sublistas dentro de ella.
        """
        lista = [1, [2, 3], [4, [5, 6]]]
        resultado_esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(aplanar_lista(lista), resultado_esperado)
    
    def test_lista_compleja(self):
        """
        Prueba para una lista que contiene una mezcla de listas, tuplas y diccionarios.
        """
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(aplanar_lista(lista), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
