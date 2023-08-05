# Crie uma classe chamada Animal que tenha
# o atributo nome. Em seguida, crie um método
# chamado emitir_som que imprima "O {nome} emitiu um som".


class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def emitirSom(self):
        print(f"O {self.nome} emitiu um som!{self.som}")


baleia = Animal("baleia", "iiinnnñññññããããã")
baleia.emitirSom()

burro = Animal("burro", "inhõõõ")
burro.emitirSom()

galinha = Animal("galinha", "cócócó")
galinha.emitirSom()
