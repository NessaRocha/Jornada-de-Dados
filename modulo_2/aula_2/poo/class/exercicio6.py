# Crie uma classe chamada ContaBancaria que tenha os atributos
# titular e saldo. Em seguida, crie um método chamado
# mostrar_saldo que imprima o saldo da conta.


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = ""
        self.saldo = saldo

    def nome_titular(self):
        self.titular = input("Nome do titular da conta:")

    def saldo_conta(self):
        print(f"O saldo da conta do {self.titular} é {self.saldo}")


Correntista = ContaBancaria("", 340)
Correntista.nome_titular()
Correntista.saldo_conta()
