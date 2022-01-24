# PEP484

####### Função customizada

CONSTANTES = "letra maiuscula"

# objetivo -> unidade mínima de modularização
## -> organização; definir responsabilidades
### do one thing and do it well;

## Spreads

dic = { 'n1': 10, 'n2': 20 }
tupla = (0,1,2,3,4,5)

#### -> trecho de código generalizável / reutilizar
                              # keyword arguments
                              # key = value, key2 = value, ...
def soma_a_partir_de_keywords(**kwargs):
  print(kwargs)
  print(kwargs.keys()) # exemplo: { n1: 2, n2: "jujuba" }

# soma_a_partir_de_keywords(n1=2, n2="jujuba", "jujuba"="teste")

                                  # transforma em uma tupla
                                  # multiple arguments
                                  # value1, value2, value3, ...
def soma_com_multiplos_argumentos(*args):
  print(args)
  print(type(args))
  print(args[0])
  soma = 0
  for i in args: # operações com as tuplas
    soma += i
  return soma

                                # spreading para dicionários
print(soma_a_partir_de_keywords(**dic))
                                    # spreading para tuplas
print(soma_com_multiplos_argumentos(*tupla))

                         # esse type hint não impoe uma tipagem dos dados
                         # valor padrão -> depois dos valores obrigatórios
def soma_de_dois_numeros(n2: int = 2, n1: int = 2) -> int: # parametros
  print(n1)
  print(n2)
  # n1 += 10
  return n1 + n2
  # instruções do que a função faz
  # mais de uma instrução

# num1 = "aaaaaa"
num1 = 13
num2 = 1234

print(soma_de_dois_numeros(num1, num2))
print(num1) # 13 por conta de ser imutável. Elementos imutáveis, terão seu valor alterado por uma função (passagem por cópia)
               # argumentos
# nome_da_funcao(1, 2) # call operator

def soma_a_partir_de_uma_lista(lista_de_numeros):
  soma = 0
  lista_de_numeros[0] = lista_de_numeros[0] + 10
  for num in lista_de_numeros:
    soma += num
  return soma

lista = [1,2,3,4,5,6]

print(soma_a_partir_de_uma_lista(lista))
print(f'valor do primeiro elemento da lista: {lista[0]}') # elementos mutáveis, terão seu valor alterado por uma função (passagem por referência)

# tipos imutáveis -> passagem de valores por cópia -> o valo será alterado
# tipos mutáveis -> passagem por referência -> o objeto em si é passível de alteração

# Simplesmente um hint
def qualquer(string: str):
  print(f"Valor informado: {string}")

####### Função anônima
# uma única instrução
variavel_qualquer = lambda param1, param2: param1 + param2 # instrução do que a função realiza
variavel_qualquer(1,2)