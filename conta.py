class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo Objetos ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo do Titular {} é {}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor