#!/usr/bin/python3

#
#
# Que receba dois números e apresente a sua soma
#
#

## Problema -> Problema de computação -> linguagem (python) 

## Algoritmo

## Passo 1: receber o primeiro número <> input()
## Passo 2: armazenar o número informado <> <variável> = o que vai ser atribuído

n1 = input("Informe o primeiro número:")

## Passo 3: receber o segundo número
## Passo 4: armazenar o número informado

n2 = input("Informe o segundo número:")

## Passo 5: efetuar a soma e armazenar o seu resultado em um formato numérico

soma = float(n1) + float(n2)

## Passo 6: apresenta a soma para o usuário final

# print("O resultado da soma {} + {} = {}".format(n1, n2, soma))
print("O resultado da soma {} + {} = {:.2f}".format(n1, n2, soma))

# F'string
print(f"O resultado da soma {n1} + {n2} = {soma}")
print("O resultado da soma {pri} + {sec} = {sum}".format(pri=n1, sec=n2, sum=soma))