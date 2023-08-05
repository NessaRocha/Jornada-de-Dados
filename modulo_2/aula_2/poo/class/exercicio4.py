# Crie uma classe chamada Carro que tenha o atributo marca.
# Em seguida, crie um método chamado info que imprima uma
# mensagem dizendo "Este carro é da marca {marca}"


class Carro:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_marca(self):
        print(f"Este carro é da marca {self.marca}")


carro = Carro("BMW")
carro.mostrar_marca()
