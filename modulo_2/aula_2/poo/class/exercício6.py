# Crie uma classe chamada Livro que tenha os atributos
# receba do usuario titulo e autor. Em seguida, crie um método chamado
# detalhes que imprima os detalhes do livro (título e autor).


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f"Livro: {self.titulo}")
        print(f"Autor: {self.autor}")


titulo = input("Titulo do Livro:")
autor = input("Autor do Livro: ")
livro1 = Livro(titulo, autor)
livro1.detalhes()
