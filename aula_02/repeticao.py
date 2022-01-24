# Repetições

## for

carrinho = [
  ('SKU#1928', 10.90),
  ('SKU#1772', 5.50),
  ('SKU#2012', 9.50),
  ('SKU#1203', 7.50)
]

### Perguntas:
#### i) qual o produto de maior valor?
#### ii) qual a soma total dos produtos do carrinho?
#### iii) qual o valor médio dos produtos?
#### iv) qual o produto de menor valor?

#### problema i):
##### olhar cada elemento por vez (LOOP)
##### ter um valor inicial de referência -> 0
##### comparar cada valor e definir se é o maior ou não
##### armazenar o maior valor e ir para o próximo item da lista
# foreach

maior_valor = 0
produto_de_maior_valor = ""
# para cada item no carrinho: <- faça
for produto in carrinho:
  if maior_valor < produto[1]:
    maior_valor = produto[1]
    produto_de_maior_valor = produto[0]

print(f"Item de maior valor: {produto_de_maior_valor}")

maior_valor = 0
produto_de_maior_valor = ""

for indice in range(len(carrinho)):
  if carrinho[indice][1] > maior_valor:
    maior_valor = carrinho[indice][1]
    produto_de_maior_valor = carrinho[indice][0]

print(f"Item de maior valor: {produto_de_maior_valor}")

print("Fim da lista de compras")
print(f"Maior valor encontrado na lista: {maior_valor}")

# [ item1, item2, item3, item4 ]
# 1: produto = item1 0 < 5.50? Sim, vou assumir que 5.50 é o maior valor
# 2: produto = item2 5.50 < 6.50? Sim, ...
# ....
# 4: produto = item4

## while

# variável de controle do loop
contador = 0

while contador < len(carrinho):
  print(carrinho[contador])
  contador += 1 # lembrar de atualizar

# Se não atualizamos o contador:
# 1: contador: 0 
#       0 < 4? SIM:
#         print(carrinho[0])
# 2: contador: 0
#       0 < 4? SIM:
#         print(carrinho[0])
# ...
# Se atualizamos o contador:
# 1: contador: 0 
#       0 < 4? SIM:
#         print(carrinho[0])
#         contador = contador + 1 (0 = 0 + 1)
# 2: contador: 1
#       1 < 4? SIM:
#         print(carrinho[1])
#         contador = contador + 1 (1 = 1 + 1)
# 3: contador: 2
#       2 < 4? ...
# ...
# 5: contador: 4
#       4 < 4? NÂO

#### problema ii):

soma = 0

for produto in carrinho:
  soma += produto[1]

print(f"Soma total dos produtos do carrinho: {soma}")

#### problema iii):
soma = 0

for produto in carrinho:
  soma += produto[1]

valor_medio = soma / len(carrinho)

print(f"Valor médio dos produtos: {valor_medio}")

#### problema iv):
menor_valor = carrinho[0][1]
produto_de_menor_valor = ""

for produto in carrinho:
  if menor_valor > produto[1]:
    menor_valor = produto[1]
    produto_de_menor_valor = produto[0]

print(f"Produto de menor valor: {produto_de_menor_valor}")
print(f"Valor do produto de menor valor: {menor_valor}")

