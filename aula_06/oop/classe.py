class Pneu:
  def __init__(self, quantidade = 4, treadwear = 0, ruido = 'F', marca = '', desgaste = 100):
    self.quantidade = quantidade
    self.treadwear = treadwear
    self.ruido = ruido
    self.marca = marca
    self.desgaste = desgaste

  def aplicaDesgaste(self, km: int):
    self.desgaste -= km * (self.treadwear * 0.0001)

class PneuF1(Pneu):
  def aplicaDesgaste(self, km: int):
      self.desgaste -= km * (self.treadwear * 0.01)

class Carro:
  ## Caracteristicas <> variáveis <> atributos

  def __init__(self):         # construtor
    self.cor = ''             # ponteiro <> self <> this
    self.velocidade = 0       # <estado>
    self.modelo = ''
    self.placa = ''
    self.__motor = 1.0 # 1 underline apenas não deixo visível. 2 underlines eu não deixo visível e não permito acesso
    self.combustivel = 'gasolina'
    self.tanque = 40
    self.pneus = Pneu()


  ## Comportamentos                 # métodos <> funções
  def acelerar(self, velocidade: int = 10):
    self.velocidade += velocidade
    self.tanque -= (velocidade * self.__motor) / 10

  def brecar(self, velocidade: int = 10):
    if self.velocidade == 0:
      print('Carro encontra-se parado')
    else:
      self.velocidade -= velocidade

c1 = Carro()
c2 = Carro()