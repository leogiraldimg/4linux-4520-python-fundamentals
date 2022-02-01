import requests
import datetime
from MontyDB import MontyDB
from time import sleep


### definir uma lista de cep - pelo menos 10
### consultar na api do viacep
### persistir no mongodb local -> storage cep / db cep/ collection cep
### estrutura de dicionário:
####
#### { cep, logradouro, bairro, uf, etc. }
#### não precisa pegar siagi, ibge, gia, etc.
###
### adicionar timestamp da coleta

FILE_NAME = 'lista_ceps.txt'
API_URL = 'http://viacep.com.br/ws/{}/json/'
KEYS = ['cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf']

def get_data(filename: str) -> "TextIOWrapper":
  return open(filename)

hasNext = True
fp = get_data(FILE_NAME)
data = []

while hasNext:
  try:
    cep = next(fp).strip()
    response = requests.get(API_URL.format(cep))
    response.raise_for_status()

  except StopIteration:
    hasNext = False
    fp.close()

  except requests.exceptions.HTTPError as e:
    print(e)

  else:
    response_data = response.json()
    target = { key: response_data.get(key) for key in KEYS }
    target['timestamp'] = datetime.datetime.utcnow()
    data.append(target)
    sleep(0.5)
    print(target)

try:
  with MontyDB('cep', 'cep', 'cep') as mdb:
    mdb.collection.insert_many([ dic for dic in data if None not in dic.values() ])
except Exception as e:
  print(e)
