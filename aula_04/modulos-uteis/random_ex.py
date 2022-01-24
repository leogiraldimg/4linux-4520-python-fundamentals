import random
import time
from random import randint as ri

# gerar números inteiros aleatórios
n1 = random.randint(0, 199)

print(n1)

# embaralhar listas
lista = [ x for x in range(100) ]
random.shuffle(lista)

print(lista)

# selecionar amostras
amostra = [ lista[random.randint(0, len(lista) - 1)] for x in range(0, 10) ]
print(amostra)

# dados mocks
names = ['Julio', 'Andre', 'Felipe', 'Fernando', 'Maria', 'Cecilia']

users = [
  {
    'id': f'{ri(0,9)}{ri(0,9)}{ri(0,9)}',
    'name': names[ri(0, len(names) - 1)],
  }  for x in range(0, 100)
]

print(users)

# jogos

cadeiras = len(names) - 1

while cadeiras >= 1:
  print("Musica rolando")
  time.sleep(1)
  print("...............")
  time.sleep(2)
  print("...............")
  time.sleep(1)

  print("Musica parou")
  time.sleep(1)

  print("Os participantes se movimentam")
  time.sleep(2)

  # algum jogador tem que ser retirado
  random.shuffle(names)

  print(f"O jogador {names.pop()} saiu do jogo!")

  cadeiras -= 1

print(f"O jogador {names[0]} Venceu!")
