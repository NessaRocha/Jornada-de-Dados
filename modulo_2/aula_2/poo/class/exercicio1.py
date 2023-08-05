# Crie uma classe chamada Retangulo que tenha os atributos
# largura e altura. Em seguida, crie um método chamado area
# que retorne a área do retângulo (área = largura * altura).


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def mostrar_area(self):
        mostrar_area = self.altura * self.largura
        print(f"Area do retangulo com total de : {mostrar_area}")


area1 = Retangulo(3, 5)
area1.mostrar_area()
