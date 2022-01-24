#!/usr/bin/python3

# Coleções

# 3 -> 1) tuplas
#      2) listas
#      3) dicionários

# Tuplas

## ()

print("Tuplas")

##       0 1 2 3 4     5       6       -1
tupla = (1,2,3,4,5, "texto", 10.5, (0,1,2,3))
##                                  0 1 2 3

## Apresentando uma tupla:
### Acessar o valor texto:
print(f"Acessando o índice 5 o qual contém a palavra 'texto': {tupla[5]}")

### Acessar o último valor:
print("O último valor da tupla através do índice -1: {}".format(tupla[-1]))
print(f"Podemos fazer a mesma coisa indicando o índice 7: {tupla[7]}")

### Tamanho:
print(f"O tamanho da tupla é: {len(tupla[7])}")

### Acessando um elemento de coleção dentro da tupla:
print(f"{tupla[-1]}") # apresenta o último elemento -> (0,1,2,3)
print(f"{tupla[-1][2]}")

# Listas

## []

print("Listas")

lista = [0, 1, 2, 3, 4, [0,1,2,3,4], "texto", 10.5, (0,1,2,3,4)]

## É possível alterar o conteúdo dos elementos
## Possui mais comportamentos
## De resto, a forma de acesso é idêntica às das tuplas

# Dicionários

## {}

print("Dicionários")

pessoa = {
  'nome': 'Guido van Rossum',
  'nacionalidade': 'Holandesa',
  'idade': 56
}

print(pessoa['idade']) # 56
print(pessoa['nome']) # Guido van Rossum
print(pessoa["nacionalidade"])# Holandesa