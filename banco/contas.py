class ContaBancaria:
    def __init__(self, titular, senha, saldoinicial = 0):
        self.titular = titular
        self.senha = senha
        self.sald = saldoinicial
        self.extrato = []

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
self.extrato.append("")
    