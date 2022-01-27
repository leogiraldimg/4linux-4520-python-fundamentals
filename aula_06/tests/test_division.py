import unittest

from exceptions import divisao

class TesteDivisao(unittest.TestCase):
  def setUp(self):
    self.x = 20
    self.y = 10

  def makeAssertions(self):
    self.assertEqual(2, divisao(self.x, self.y))
    self.assertEqual('Nao dividiras por zero', divisao(self.x, 0))

  def test_exceptions(self):
    """ Nao realiza divisoes por zero """
    self.makeAssertions()

  def test_exemplo(self):
    """ realiza divisao com numeros """
    self.assertEqual(2, divisao(self.x, self.y))
