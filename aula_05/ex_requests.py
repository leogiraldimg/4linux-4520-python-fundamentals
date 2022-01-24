### Criar uma lista de CEPs e montar um arquivo no formato CSV
#### Coletar dados da API do VIACEP
#### Lista de 10 CEPs
#### Realizar a requisiçao via requests
#### Converter a saida json para um formato adequado ao csv
#### Salvar o arquivo localmente

import requests

api_url = 'http://viacep.com.br/ws/{}/json'
