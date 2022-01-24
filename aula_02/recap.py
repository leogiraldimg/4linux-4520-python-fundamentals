# Tipos de dados "Primitivos"
## "carregam uma única informação"
### - Inteiros
### - Floats
## Sequencia
### - Strings

## Coleções
### - Listas
### - Tuplas
## "Mapping"
### - Dicionários

## Coleções

## Listas e Tuplas
        #0   1 2 3 4 5
lista = [10,34,2,5,6,7]
print(lista[3])
#                 4 
tupla = (0,2,1,2,55,60)
print(tupla[4])


## Encadeamento de tuplas/listas
#      1  2  3  
# -------------
###1 | 1  2  3   4: (L2,C1)
###2 | 4  5  6   5: (L2,C2)
###3 | 7  8  9   9: (L3,C3)

#      0  1  2  
# -------------
###0 | 1  2  3   4: (L2-1,C1-1)
###1 | 4  5  6   5: (L2-1,C2-1)
###2 | 7  8  9   9: (L3-1,C3-1)


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# apresentar o número 8
print(matriz[2][1])

## numpy -> mais eficientes 

dic = {
  'L1': [1,2,3],
  'L2': [4,5,6],
  'L3': [7,8,9]
}

# apresenta o elemento central da matriz
print(dic['L2'][1])

