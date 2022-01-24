#!/usr/bin/python3
## 
## Usuário possa escolher os produto_s_ 
## E ao final ter o valor total da compra;
## Funcionalidades adicionais:
##   remover um produto
##   apresentar os ítens da cesta 
##      se a lista tiver vazia apresentar a mensagem: "Cesta Vazia"
##   se a cesta tiver com valor maior ou igual a 50:
##      aplicar um desconto de 10%

produtos = {
    '1' : ('Melão', 5.00),
    '2' : ('Uva'  ,  8.00),
    '3' : ('Limão' , 3.00),
    '4' : ('Pera' , 4.90),
    '5' : ('Maçã' , 5.60),
}

## "Responsabilidades":
### 1: Apresentar o Menu
def menu_principal() -> None:
    print("Escolha a opção desejada: \n" \
          " 1. Adicionar frutas \n" \
          " 2. Ver cesta  \n" \
          " 3. Remover Fruta \n" \
          " 4. Ver valor total \n" \
          " 5. Sair \n")

### 2: Menu de frutas

def retorna_indice_frutas(fruta: tuple) -> str:
    for key in produtos: # list comprehension
        if produtos[key] == fruta:
            return key

def menu_frutas(cesta_de_frutas: list = []) -> str:
    # if lista não está vazia?
    if len(cesta_de_frutas) != 0:
        menu = "Escolha a opção desejada: \n"

        for fruta in cesta_de_frutas:
            # descobrir o índice do dicionário
            menu += f'{retorna_indice_frutas(fruta)} - {fruta[0]}\n'# montar a string

        return input(menu)
    
    return input("Escolha a opção desejada: \n" \
            " 1 - Melão \n" \
            " 2 - Uva \n" \
            " 3 - Limão \n" \
            " 4 - Pera \n" \
            " 5 - Maçã \n" \
            "Opção: ")


### 3: Adicionar fruta na cesta
def adicionar_fruta(cesta_de_frutas: list, tabela_produtos = produtos ) -> str: 
    fruta = menu_frutas()

    if fruta in tabela_produtos.keys():
        cesta_de_frutas.append(tabela_produtos.get(fruta))
        return f"Fruta : {tabela_produtos.get(fruta)} foi adicionada com Sucesso!"
    return "Opção Inválida"


### 4: Consolidar o Total
def consolidar_cesta(cesta_de_frutas: list) -> float : 
    return sum([ x[1] for x in cesta_de_frutas ]) # (Nome, Valor)
#    valor_total = 0
#    for item in cesta_de_frutas:
#        valor_total += item[1]
#    print(valor_total)


### 5: Sair do programa
### 6: Apresentar A cesta e Valor total da compra
def sair(cesta_de_frutas: list) -> None:
    print("Produtos:", cesta_de_frutas)
    print("Total:", consolidar_cesta(cesta_de_frutas))
    exit()

### Funcionalidades adicionais
def remover_fruta(cesta_de_frutas: list) -> str:
    if len(cesta_de_frutas) != 0:
        fruta = menu_frutas(cesta_de_frutas)
        cesta_de_frutas.remove(produtos[fruta])
        return f"Item {fruta} removido com sucesso\n"
    return "A cesta está vazia."

def apresentar_cesta(cesta_de_frutas: list) -> str:
    cesta = "Cesta:\nFRUTA\tVALOR\n"
    for item in cesta_de_frutas:
        cesta+= f"{item[0]}\t{item[1]}\n"
    cesta +=("-----------------------------\n")
    cesta +=(f"TOTAL:\t{consolidar_cesta(cesta_de_frutas)}")
    return cesta


### definir uma função que tem reponsabilidade de organizar o fluxo
def main() -> None:
    lista_de_compras = []

    opcoes = {
        '1' : adicionar_fruta,
        '2' : apresentar_cesta,
        '3' : remover_fruta,
        '4' : consolidar_cesta,
        '5' : sair
    }
    
    while True:
        menu_principal() # apresentar as opções

        opcao = input("Opção: ") # seleciono a opção

        # tratamento de exceçoes 
        if opcao in opcoes.keys(): # verifico se a opção é válida
           print(opcoes[opcao](lista_de_compras)) # Executa a opção escolhida
        else:
            print("Opção Inválida") # apresenta mensagem de erro caso não for encontrada

if __name__ == "__main__":
    main()

## Loop "Infinito"

#exit()
#
#
#while True:   # sempre vai ser verdadeiro
#    print("Escolha a opção desejada: \n" \
#          " 1. Adicionar frutas \n" \
#          " 2. Ver valor total \n" \
#          " 3. Sair \n")
#
#    opcao = input("Opção: ")
#
#    if opcao == '1':
#        fruta = input("Escolha a opção desejada: \n" \
#              " 1 - Melão \n" \
#              " 2 - Uva \n" \
#              " 3 - Limão \n" \
#              " 4 - Pera \n" \
#              " 5 - Maçã \n" \
#              "Opção: ")
#        # Validar se as opçoes estão corretas 
#        lista_de_compras.append(produtos.get(fruta))
#    
#    elif opcao == '2':
#        # ver uma forma de apresentar o valor total
#        for fruta in lista_de_compras:
#            valor += fruta[1] # [ ("nome", XX.XX), .... ]
#        print(f"Valor total da cesta: {valor}")
#        valor = 0
#    
#    elif opcao == '3': 
#        print("Obrigado, volte sempre!")
#        break
#
#    else:
#        print("Opção Inválida")
#