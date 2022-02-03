#!/usr/bin/python3.9

import pymongo
from collections import namedtuple


FILENAME='COTAHIST_D27012022.TXT'
ANUAL='COTAHIST_A2021.TXT'

def open_file(file_path: str) -> '_io.TextWrapper':
  return open(file_path)

exemplo = '012022012702A1BB34      010ABB LTD     DRN          R$  000000000460000000000047520000000004600000000000467100000000046560000000004656000000000517500013000000000000001916000000000008950012000000000000009999123100000010000000000000BRA1BBBDR009101'

posicoes = """
# DATAPRG -> 03  - 10
# CODNEG ->  13  - 24
# NOMRES ->  28  - 39
# PREABE ->  57  - 69
# PREMAX ->  70  - 82
# PREMIN ->  83  - 95
# PREMED ->  96  - 108
# PREULT ->  109 - 121
"""

layout = namedtuple('layoutb3', ('offset', 'tipo', 'dec'))

to_str = lambda s: s.strip()
to_float = lambda f: float(f)/100
to_date = lambda s: f'{s[0:4]}-{s[4:6]}-{s[6:]})'

recorte = {
  'DATAPRG': layout(slice(2, 10), to_str, 'data pregao'),
  'CODNEG': layout(slice(12, 24), to_str, 'código do papel'),
  'NOMRES': layout(slice(27, 39), to_str, 'nome da empresa abreviado'),
  'PREABE': layout(slice(56, 69), to_float, 'preço de abertura'),
  'PREMAX': layout(slice(69, 82), to_float, 'preço máximo do papel no dia'),
  'PREMIN': layout(slice(82, 95), to_float, 'preço mínimo do papel no dia'),
  'PREMED': layout(slice(95, 108), to_float, 'preço médio no papel no dia'),
  'PREULT': layout(slice(108, 121), to_float, 'preço de fechamento do papel')
}

registro = {
  key: recorte[key].tipo(exemplo[recorte[key].offset]) for key in recorte.keys()
}

data = []
counter = 0

fp = open_file(FILENAME)

hasNext = True

while hasNext:
  try:
    linha = next(fp)
    if not linha[2:].startswith('COTAHIST'):
      data.append({
        key: recorte[key].tipo(linha[recorte[key].offset]) for key in recorte.keys()
      })

      counter += 1

      print(f'Registro: {counter}')
      print(data[counter - 1])
  except StopIteration:
    hasNext = False
    fp.close()

# data com os valores

MONGO_USER = 'b3_user' # .env/variável de ambiente
MONGO_PASSWD = 'b66c4d8e6990714350b2663ec50af6c1'
MONGO_URI = 'mongodb+srv://{username}:{password}@cluster0.pvetd.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = pymongo.MongoClient(MONGO_URI.format(username = MONGO_USER, password=MONGO_PASSWD))

db = client.get_database('b3')
collection = db.get_collection('historicalData')

# fonte_dados(registro) -> CHAVE, posicao, tipo_de_dado, desc

