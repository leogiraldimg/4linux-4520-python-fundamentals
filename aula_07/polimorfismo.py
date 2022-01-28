class ContaBancaria:
  def __init__(self) -> None:
    self.saldo = 0
    self.limite = 0

  def sacar(self, valor):
    if self.saldo + self.limite >= valor:
      self.saldo -= valor

class ContaPremium(ContaBancaria):
  def __init__(self) -> None:
    self.saldo = 0
    self.limite = 0
    self.pontos = 0

  def sacar(self, valor):
    if self.saldo + self.limite >= valor:
      self.saldo -= valor
      self.pontos += 1

c1 = ContaBancaria()
cp = ContaPremium()