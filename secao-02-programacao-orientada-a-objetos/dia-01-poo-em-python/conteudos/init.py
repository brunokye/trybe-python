class Liquidificador:
    def __init__(
        self,
        cor: str,
        potência: int,
        tensão: int,
        preço: float | int
    ) -> None:
        self.cor = cor
        self.preço = preço
        self.potência = potência
        self.tensão = tensão

        self.ligado = False
        self.velocidade = 0
        self.velocidade_máxima = 3
        self.corrente_atual_no_motor = 0


meu_liquidificador = Liquidificador("Azul", 200, 127, 200)
seu_liquidificador = Liquidificador(
    cor="Vermelho", potência=250, tensão=220, preço=100
)
