import unittest
from Guia7 import saldoActual, cantidadDigitosImpares,longMayorASiete

class testSaldo(unittest.TestCase):
    def testSaldo(self):
        self.assertEqual(saldoActual([('I',2000),('R',20),('I',300),('R',1000)]),1280)


class testDigImpares(unittest.TestCase):
    def testDigImpares(self):
        self.assertEqual(cantidadDigitosImpares([57,2383,812,246]),5)

class testLong(unittest.TestCase):
    def testLong(self):
        self.assertFalse(longMayorASiete(["termo","gato","tener","jirafas"]))


if __name__ == '__main__' :
    unittest.main(verbosity=2)