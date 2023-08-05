class BonecaBarbie:
    def __init__(self, nome, cor_cabelo, acessorios):
        self.nome = nome
        self.cor_cabelo = cor_cabelo
        self.acessorios = acessorios

    def mostrar_informacoes(self):
        print(
            f"Boneca: {self.nome}, Cor de Cabelo: {self.cor_cabelo}, Acessório: {self.acessorios}"
        )


barbie1 = BonecaBarbie("Barbie Fashion", "loiro", "colar")
barbie1.mostrar_informacoes()

barbie1 = BonecaBarbie("Barbie Maluca", "castanho", "pulseira")
barbie1.mostrar_informacoes()
