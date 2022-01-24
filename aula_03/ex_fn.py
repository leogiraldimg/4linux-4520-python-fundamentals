#!/usr/bin/python3

produtos = {
  '1': ('Melão', 5.00),
  '2': ('Uva', 8.00),
  '3': ('Limão', 3.00),
  '4': ('Pera', 4.90),
  '5': ('Maçã', 5.60)
}

##
## Usuário possa escolher os produtos
## E ao final ter o valor total da compra;
## DESAFIO:
##   remover um produto
##   apresentar os itens da cesta
##     se a lista tiver vazia apresentar a mensagem: "Cesta vazia"
##   se a cesta tiver com valor maior ou igual a 50, aplicar um desconto de 10%
##

## Desafio: remover um produto
def remover_fruta(cesta_de_frutas: list) -> None:
  if len(cesta_de_frutas) > 0:
    print("Escolha qual fruta deseja remover:")
    
    for indice in range(len(cesta_de_frutas)):
      print(f" {indice + 1} - {cesta_de_frutas[indice][0]}\n")
    
    fruta_alvo = int(input("Fruta: "))

    if (fruta_alvo - 1) in range(len(cesta_de_frutas)):
      del cesta_de_frutas[(fruta_alvo - 1)]
    else:
      return ("Essa fruta não está na cesta\n")
  else:
    return ("Não há frutas na cesta\n")

## Desafio: apresentar os itens da cesta
def apresentar_cesta(cesta_de_frutas: list) -> None:
  listagem_cesta = ""

  if len(cesta_de_frutas) > 0:
    for item in cesta_de_frutas:
      listagem_cesta += (str(item) + ";")
    return (f"{listagem_cesta}")
  else:
    return ("Cesta vazia")
  

# "Responsabilidades":
## 1: Apresentar o menu principal
def menu_principal() -> None:
  print ("Escolha a opção desejada: \n" \
          " 1. Adicionar frutas\n" \
          " 2. Remover fruta\n" \
          " 3. Ver valor total\n" \
          " 4. Listar itens da cesta\n" \
          " 5. Sair\n")

## 2: Menu de frutas
## 3: Adicionar fruta na cesta
def adicionar_fruta(cesta_de_frutas: list, tabela_produtos = produtos) -> None:
  fruta = input("Escolha a opção desejada:\n" \
                " 1 - Melão\n" \
                " 2 - Uva\n" \
                " 3 - Limão\n" \
                " 4 - Pera\n" \
                " 5 - Maçã\n" \
                " Opção: ")

  if fruta in tabela_produtos.keys():
    cesta_de_frutas.append(tabela_produtos.get(fruta))
    return
  
  return "Opção inválida"

## 4: Consolidar o total
def consolidar_cesta(cesta_de_frutas: list) -> None:
  valor_total = sum([ x[1] for x in cesta_de_frutas])

  # for item in cesta_de_frutas:
  #   valor_total += item[1]

  if valor_total >= 50:
    valor_total = (valor_total * 0.9)

  return valor_total

## 5: Sair do programa
## 6: Apresentar a cesta e o valor total da compra
def sair(cesta_de_frutas: list) -> None:
  print("Produtos: ", cesta_de_frutas)
  consolidar_cesta(cesta_de_frutas)
  exit()

### definir uma função que tem responsabilidade de organizar o fluxo
def main() -> None:
  lista_de_compras = []
  opcoes = {
    '1': adicionar_fruta,
    '2': remover_fruta,
    '3': consolidar_cesta,
    '4': apresentar_cesta,
    '5': sair
  }

  while True:
    menu_principal()

    opcao = input("Opção: ")

    if opcao in opcoes.keys():
      print(opcoes[opcao](lista_de_compras))
    else:
      print("Opção inválida")

# valor = 0
# lista_de_compras = []

# # Loop "infinito"
# while True:
#   print("Escolha a opção desejada: \n" \
#         " 1. Adicionar frutas\n" \
#         " 2. Ver valor total\n" \
#         " 3. Sair\n" \
#         )

#   opcao = input("Opção: ")

#   if (opcao == "1"):
#     for fruta in lista_de_compras:
#       valor += fruta[1]
#     print(f"Valor total da cesta: {valor}\n")
#   elif (opcao == "2"):
#     for fruta in lista_de_compras:
#       valor += fruta[1]
#     print(f"Valor total da cesta: {valor}\n")
#     valor = 0
#   elif (opcao == "3"):
#     print("Obrigado, volte sempre!\n")
#     break
#   else:
#     print("Opção inválida\n")

# print("Produtos: ", lista_de_compras)
# print("Valor total: ", valor)

if __name__ == "__main__":
  main()