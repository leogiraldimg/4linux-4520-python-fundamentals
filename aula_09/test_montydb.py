
from unittest import TestCase

from MontyDB import MontyDB

class TestMontyClass(TestCase):
  def setUp(self):
    self.mdb = MontyDB(storage_name = "testedb"
                      , database_name= "user"
                      , collection_name="users")

    self.mock = { 
      'username': 'alovelace',
      'password': 'Babbage'
    }

  def makeAssertions(self):
    # definir o storage
    self.mdb.setStorage(self.mdb.metadata.get('storage_name'))
    # acessar um banco de dados
    self.mdb.setDatabase(self.mdb.metadata.get('database_name'))
    # selecionar uma collection
    self.mdb.setCollection(self.mdb.metadata.get('collection_name'))
    # inserção de um doc de teste
    self.mdb.collection.insert_one(self.mock)
    self.assertEqual(self.mock, self.mdb.collection.find_one(
        {'username' : self.mock['username']}))

  def test_Global(self):
    """
      MontyDB realiza:
        - Seleção de storage local
        - Acesso a um determinado banco de dados
        - Seleciona uma collection
        - Insere um documento
          
    """
    self.makeAssertions()
