from typing import Protocol


class CalculaPerimetro(Protocol):
    def calcular_perimetro(self):
        pass


class Quadrado(CalculaPerimetro):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def calcular_perimetro(self):
        return f"O perímetro do quadrado é de {self.lado * 4} cm"


class Triangulo(CalculaPerimetro):
    def __init__(self, lado1: int, lado2: int, lado3: int) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        return (
            "O perímetro do triângulo é de "
            f"{self.lado1 + self.lado2 + self.lado3} cm"
        )


quadrado = Quadrado(5)
print(quadrado.calcular_perimetro())

triangulo = Triangulo(5, 5, 5)
print(triangulo.calcular_area())
