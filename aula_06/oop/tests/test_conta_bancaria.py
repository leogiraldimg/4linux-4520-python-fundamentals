from unittest import TestCase
from ex_oop import ContaBancaria

class TesteContaBancaria(TestCase):
  def setUp(self):
    self.conta = ContaBancaria()
    self.conta_destino = ContaBancaria()

  def testConsultarSaldo(self):
    """ Deve apresentar o saldo em conta """
    self.assertEqual(0, self.conta.verificarSaldo())

  def testSacarDinheiro(self):
    """ Possibilita retirada de valores da conta """
    self.conta.depositar(200)
    saque = 100.0
    valor_inicial = self.conta.verificarSaldo()
    self.conta.sacar(saque)
    self.assertEqual(valor_inicial - saque,
                     self.conta.verificarSaldo()
                     )

  def testChecaLimiteAntesDeSacar(self):
    valor = 100000000
    valor_inicial = self.conta.verificarSaldo()

    resultado_saque = self.conta.sacar(valor)
    
    self.assertEqual('Limite indisponível para saque', resultado_saque)
    self.assertEqual(valor_inicial, self.conta.verificarSaldo())

  def testRealizarDeposito(self):
    """ Possibilita adicionar valor em conta """
    deposito = 100
    self.conta.depositar(deposito)
    self.assertEqual(100, self.conta.verificarSaldo())

  def testRealizarTransferencia(self):
    """ Possibilita a realização de transferência de valores entre contas """
    valor_inicial = 0
    transferencia = 100

    self.conta.transferir(transferencia, self.conta_destino)

    self.assertEqual(
      valor_inicial - transferencia,
      self.conta.verificarSaldo()
    )
    self.assertEqual(
      valor_inicial + transferencia,
      self.conta_destino.verificarSaldo()
    )
