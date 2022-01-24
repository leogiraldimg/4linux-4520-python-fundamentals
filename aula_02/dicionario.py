users = [
  {
    'username': 'gvrossum@4linux.com.br',
    'password': '1234567',
    'expired': True
  },
  {
    'username': 'gvrossum_2@4linux.com.br',
    'password': '2132312',
  },
  {
    'username': 'gvrossum_3@4linux.com.br',
    'password': 'lakdj21',
    'expired': True
  }
]

### Como validar as credenciais a partir da lista users?
username = input('username: ')
password = input('password: ')

for user in users:
  if user['username'] == username:
    if password == user['password']:
      if not user.get('expired'):
        print('Usuário validado com sucesso!')
        break
      else:
        print('Usuário bloqueado. Entrar em contato com o administrador')
        break
    else:
      print('Usuário/senha inválidos')
      break
else:
  print("Usuário não encontrado")

dic = {
  'nome': 'Guido Van Rossum',
  'idade': 45,
  'linguagem': ['Python', 'C'],
  'nacionalidade': 'Holandesa',
  'empresas': {
    'microsoft': { 'data-inicio': '17/09/2017', 'data-fim': '' },
    'ABC': { 'data-inicio': '10/04/1991', 'data-fim': '10/08/1999' }
  }
}

# Apresentar nome, idade e nacionalidade a partir do dicionário
print("Funcionário")

for key in dic.keys():
  if key in ['nome', 'idade', 'nacionalidade']:
    print(f'{key}: {dic[key]}')

for key in dic.keys():
  if key == 'linguagem':
    if 'C' in dic[key]:
      print('Achei!')

for key, value in dic.items():
  print(f'{key}: {value}')