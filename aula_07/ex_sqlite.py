import sqlite3


### estabelecia uma stream "ligação" <> conectar com o banco
### realizar ações -> leitura do conteúdo, ....
### persistia
### fechava a conexão

# inicializar conexão
conn = sqlite3.connect('arquivo.db')

# executar e coletar os dados do banco
cursor = conn.cursor()

sql_statement = """

CREATE TABLE users(
  id integer primary key autoincrement,
  login text,
  senha text,
  nome text
);

"""

sql_insert_into_users = """

INSERT INTO users(login, senha, nome)
VALUES (?, ?, ?)

"""

sql_update_password = """

UPDATE users
SET senha = {}
WHERE id = {}

"""

sql_delete_users = """

DELETE FROM users
WHERE id = {}

"""

## delete
# cursor.execute(sql_delete_users.format(1))

## update
# cursor.execute(sql_update_password.format('123456', 1))

## select
# print(cursor.execute("SELECT * from users").fetchone())

## insert
# cursor.execute(sql_insert_into_users, ('gcorrea', '123qwe123', 'guilherme correa'))