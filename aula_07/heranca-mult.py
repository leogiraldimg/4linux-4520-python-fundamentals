class Pai:
  def __init__(self) -> None:
    self.idade = 0
    self.nacionalidade = 'brasileira'

  def apresentacao(self):
    return "Olá, como vai você?"

  def outroMetodo(self):
    return f'Minha idade é {self.idade}'

class Mae:
  def __init__(self) -> None:
    self.idade = 0
    self.nacionalidade = 'inglesa'

  def apresentacao(self):
    return 'Hi, how are you?'

  def ondeMora(self):
    return 'I live in São Paulo'

class Filha(Mae, Pai): # ordem de resolução de métodos -> quem está em primeiro, terá seu método herdado -> MRO (Method Resolution Order)
  pass

class N1(Filha):
  def apresentacao(self):
    return 'E ai mano!'

class N2(Filha):
  def apresentacao(self):
    return 'Bah tchê!'

class B1(N1, N2):
  pass

#   A    C
#   \   /
#     D
#
#     A
#   /  \
#  B    C
#  \   /
#    D