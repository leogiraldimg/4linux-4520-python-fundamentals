### Criar uma lista de CEPs e montar um arquivo no formato CSV
#### Coletar dados da API do VIACEP
#### Lista de 10 CEPs
#### Realizar a requisiçao via requests
#### Converter a saida json para um formato adequado ao csv
#### Salvar o arquivo localmente

import requests

ceps_list = [
 '08090-284',
 '04849-529',
 '04843-425',
 '08226-021',
 '04180-112',
 '04236-094',
 '02317-262',
 '03047-000',
 '03807-020',
 '08240-001'
]

file_header = ''
file_content = []

for cep in ceps_list:
  response = requests.get(f'http://viacep.com.br/ws/{cep}/json')

  if 'erro' not in response.json().keys():
    if not file_header:
      file_header = ';'.join(list(response.json().keys())) + '\n'
      file_content.append(file_header)

    file_content.append(';'.join(list(response.json().values())) + '\n')

with open('lista_ceps.csv', 'w') as file:
  file.writelines(file_content)

