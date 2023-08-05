# Crie uma classe chamada Pessoa que tenha o atributo nome.
# Em seguida, crie um método chamado apresentar que imprima
# uma mensagem dizendo "Olá, eu sou {nome}".


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_nome(self):
        print(f"Olá, eu sou {self.nome}")


nome = Pessoa("Luciana")
nome.mostrar_nome()

nome1 = Pessoa("Joana")
nome1.mostrar_nome()

nome2 = Pessoa("Maria")
nome2.mostrar_nome()
