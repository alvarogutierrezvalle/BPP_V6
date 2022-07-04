import pytest
import unittest

#FUNCIONES
def capital(x):
    if not isinstance(x, str):
        raise TypeError("El dato introducido no es de tipo String")
    return x.capitalize()

def es_par(x):
    if x%2 == 0:
        return True
    else:
        return False

def ordenar(a,b,c):
    lista = [a,b,c]
    lista.sort()
    return lista

# TEST CON PYTEST

def test_capital():
    assert capital("hola") == "Hola"

def test_es_par():
    assert es_par(26) == True

def test_ordenar():
    lista = ordenar(3,6,1)
    assert lista[0] < lista[2]
    

def test_control_type():
    with pytest.raises(TypeError):
        capital(True)
        es_par("hola")
        ordenar("hola",True,3)

# TEST CON UNITTEST

class MisTest(unittest.TestCase):
    def check_in(self):
        self.assertIn('s', 'spain')

    def check_instance(self):
        self.assertIsInstance('a', str)

    def check_true(self):
        resultado = es_par(44)
        self.assertTrue(resultado)

    def check_is_greater(self):
        edad = 20
        self.assertGreaterEqual(edad, 18)

    def test_exception(self):
        with self.assertRaises(TypeError):
            capital(35)

if __name__ == '__main__':
    unittest.main()