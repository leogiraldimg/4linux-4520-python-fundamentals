matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

l = 3
c = 3

#                 (0,1,2)
for linha in range(l):
  for coluna in range(c): # (0,1,2)
    print(matriz[linha][coluna])

# Iteração 1: linha = 0
#   segundo for:
#     iteração 1:
#       linha = 0
#       coluna = 0
#     iteração 2:
#       linha = 0
#       coluna = 1
#     iteração 3:
#       linha = 0
#       coluna = 2
# Iteração 2: linha = 1
#   segundo for:
#     iteração 1:
#       linha = 1
#       coluna = 0
#     iteração 2:
#       linha = 1
#       coluna = 1
#     iteração 3:
#       linha = 1
#       coluna = 2
# Iteração 3: linha = 2
#   segundo for:
#     iteração 1:
#       linha = 2
#       coluna = 0
#     iteração 2:
#       linha = 2
#       coluna = 1
#     iteração 3:
#       linha = 2
#       coluna = 2

# Exercício: calcular o valor da diagonal 1,5,9 e da diagonal 3,5,7

l = 3
c = 3

dp = 0
ds = 0

for linha in range(l):
  for coluna in range(c):
    if (linha == coluna):
      dp += matriz[linha][coluna]
    if ((linha + coluna) == (l-1)):
      ds += matriz[linha][coluna]


print(f'Soma diagonal 1,5,9: {dp}')
print(f'Soma diagonal 3,5,7: {ds}')
