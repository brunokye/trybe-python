class GastoMensal:
    def __init__(
        self,
        internet: float,
        supermercado: float,
        luz: float,
        agua: float,
        aluguel: float
    ) -> None:
        self.internet = internet
        self.supermercado = supermercado
        self._luz = luz
        self._agua = agua
        self.__aluguel = aluguel

    def get_luz(self):
        return self._luz

    def set_luz(self, novo_valor: float) -> float:
        self._luz = novo_valor

    def get_agua(self):
        return self._agua

    def set_agua(self, novo_valor: float) -> float:
        self._agua = novo_valor
