import montydb

### implementar a classe para funcionar tanto com banco local como com o pymongo

class MontyDB:

  """
  mdb = MontyDB('testedb', 'user', 'users')
  mdb.setStorage('testedb')
  mdb.setDatabase('user')
  mdb.setCollection('users')

  mdb.collection.find_one(<query>)  # retorna a primeira ocorrência
  mdb.collection.find(<query>)      # procura um conjunto resultados
  mdb.collection.insert_one(<documento>)    # inserir um documento
  mdb.collection.delete_one(<query>)
  mdb.collection.update_one(<query>, {$set : <campo> : <valor_atualizado>})

  """
  def __init__(self
    , storage_name: str
    , database_name : str
    , collection_name: str
  ):
    self.client = None
    self.db = None
    self.collection = None
    self.metadata = {
      'storage_name'  : storage_name,
      'database_name' : database_name,
      'collection_name': collection_name,
    }

  def __enter__(self):
    return self._setUp()

  def __exit__(self, type_, value, traceback):
    self.client.close()

  def _setUp(self):
    self.setStorage(self.metadata.get('storage_name'))
    self.setDatabase(self.metadata.get('database_name'))
    self.setCollection(self.metadata.get('collection_name'))
    return self

  def setStorage(self, storage_name: str) -> None:
    """
      Cria ou Seleciona um diretório local.

      Argumentos:
        storage_name : str ->  nome do diretório com os dados do banco

    """

    montydb.set_storage(storage_name)
    self.client = montydb.MontyClient(storage_name)
  
  def setDatabase(self, database_name: str) -> None :
    """
      Cria ou seleciona uma base de dados

      Args:
          database_name: str ->   nome do banco de dados
    """

    self.db = self.client.get_database(database_name)

  def setCollection(self, collection_name):
    """
      Cria ou seleciona uma collection do banco de dados

    """

    self.collection = self.db.get_collection(collection_name)


if __name__ == '__main__':
  with MontyDB('testedb', 'user', 'users') as mdb:
    print(mdb.collection.find_one({'username': 'alovelace'}))

