def divisao(num1: int, num2: int) -> float:
  try:
    # trecho de codigo que pode dar ruim
    ## conexoes com banco de dados requisiçoes de API
    ## entrada de usuario

    return num1 / num2

    # print(f'O resultado final da divisao {num1}/{num2} {res}')

  except ZeroDivisionError:
    return 'Nao dividiras por zero'

