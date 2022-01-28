## Criar uma classe que representa uma conta bancária
## Definam os atributos
## Definam os comportamentos

###
### consultar saldo
### sacar dinheiro
### transferencia entre contas
### deposito em dinheiro
###

from typing import Union

class ContaBancaria():
  def __init__(self) -> None:
    self._saldo = 0
    self._limite = 0

  @property # getter
  def saldo(self) -> float:
    return self._saldo

  @saldo.setter
  def saldo(self, valor: float) -> None:
    if isinstance(valor, float):
      self._saldo = valor

  def verificarSaldo(self) -> float:
    return self._saldo

  def sacar(self, valor: float) -> Union[None, str]:
    if self._limite + self._saldo >= valor:
      self._saldo -= valor
    else:
      return 'Limite indisponível para saque'

  def depositar(self, valor: float) -> None:
    self._saldo += valor

  def transferir(
    self,
    valor: float,
    conta_destino: 'ContaBancaria'
  ) -> None:
    self._saldo -= valor
    conta_destino.depositar(valor)
