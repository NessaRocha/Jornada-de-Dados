class TRIANGULO:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def area(self):
        area = (self.altura * self.base) / 2
        print(f"A área do seu triangulo é :{area}")


triangulo1 = TRIANGULO(12, 2)
triangulo1.area()
