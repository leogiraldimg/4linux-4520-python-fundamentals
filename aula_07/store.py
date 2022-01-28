import sqlite3

## repository pattern
class ProductStore(Store):
  def add_product():
    pass

  def list_product():
    pass

class UserStore(Store):
  def add_user():
    pass

  def remove_user():
    pass

user = UserStore()
user.add() # escreveria no banco

class Store:
  def __init__(self,
               database = 'arquivo.db') -> None:
    self.conn = sqlite3.connect(database)
    self._complete = False

  def __enter__(self):
    return self

  def __exit__(self, type_, value, traceback):
    self.close()

  def complete(self):
    self._complete = True

  def close(self):
    if self.conn is not None:
      if self._complete:
        self.conn.commit()
      else:
        self.conn.rollback()

  def __str__(self) -> str:
    return "SQLite 3 Class Store"

with Store() as store:
  cursor = store.conn.cursor()
  cursor.execute('INSERT INTO users (login, senha, nome) VALUES ("teste", "12345", "teste")')
  store.complete()