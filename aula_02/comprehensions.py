# List comprehension | funcional Haskell, Erlang
lista = [0,1,2,3,4,5,6,7,8,9,10]

# filtros
## retorne uma lista de números, onde cada número está na lista,
## possui resto zero na divisão por dois
pares = [ num for num in lista if num % 2 == 0 ]
impares = [ num for num in lista if num % 2 != 0 ]

# mapeamentos
quadrados = [ num * num for num in lista ]

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

expirados = [ user for user in users if user.get('expired') ]

users_2 = [
  {
  'e-mail': u.get('username'),
  'senha': u.get('password')
  } for u in users
]

# Dict comprehesions

dc = { num: chr(num) for num in range(65,75) }
payload = { key['username']: key.get('expired') for key in users }