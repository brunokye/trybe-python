class Motocicleta:
    def __init__(self, velocidade_maxima: int) -> None:
        self.velocidade_maxima = velocidade_maxima


class Caminhao:
    def __init__(self, velocidade_maxima: int) -> None:
        self.velocidade_maxima = velocidade_maxima


def print_velocidade_maxima(veiculo: int) -> None:
    if isinstance(veiculo, Motocicleta):
        print(
            f"A velocidade máxima do veículo é de {veiculo.velocidade_maxima}"
        )
    else:
        raise TypeError("O objeto precisa ser uma motocicleta")


cg_150 = Motocicleta("120 km/h")
yamaha_R1 = Motocicleta("300 km/h")
ford_C_2042 = Caminhao("140 km/h")

print_velocidade_maxima(cg_150)
print_velocidade_maxima(yamaha_R1)
print_velocidade_maxima(ford_C_2042)
