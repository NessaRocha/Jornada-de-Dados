# Crie uma classe chamada Calculadora que
# tenha os métodos somar, subtrair, multiplicar e
#  dividir. Cada método deve receber dois números como parâmetros e
# retornar o resultado da operação correspondente.
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        soma = self.numero1 + self.numero2
        print(f"A soma dos numeros são : {soma}")

    def subtrair(self):
        soma = self.numero1 - self.numero2
        print(f"A subtração dos numeros são : {soma}")

    def multiplicar(self):
        soma = self.numero1 * self.numero2
        print(f"A multiplicação dos numeros são : {soma}")

    def dividir(self):
        soma = self.numero1 / self.numero2
        print(f"A divisão dos numeros são : {soma}")


calculo1 = Calculadora(3, 5)
calculo1.somar()

calculo1 = Calculadora(8, 3)
calculo1.subtrair()

calculo1 = Calculadora(3, 5)
calculo1.multiplicar()

calculo1 = Calculadora(15, 5)
calculo1.dividir()
