class Eletrodoméstico:
    def __init__(
        self,
        cor: str,
        potência: int,
        tensão: int,
        preço: float | int
    ) -> None:
        self.preço = preço
        self.potência = potência
        self.tensão = tensão
        self.velocidade_máxima = 3

        self.cor = cor
        self.desligar()

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor: str) -> None:
        if nova_cor.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__cor = nova_cor

    def ligar(self, velocidade: int) -> None:
        if velocidade > self.velocidade_máxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.velocidade_máxima}"
            )

        self.velocidade = velocidade
        self.__ligado = True

        corrente_máxima = self.potência / self.tensão
        velocidade_percentual = velocidade / self.velocidade_máxima
        self.corrente_atual_no_motor = corrente_máxima * velocidade_percentual

    def desligar(self) -> None:
        self.__ligado = False
        self.velocidade = 0
        self.corrente_atual_no_motor = 0

    def esta_ligado(self):
        return self.__ligado


class Liquidificador(Eletrodoméstico):
    def esta_ligado(self):
        return "Sim" if super().esta_ligado() else "Não"


class Ventilador(Eletrodoméstico):
    def __init__(
        self,
        cor: str,
        potencia: str,
        tensao: str,
        preco: str,
        quantidade_de_portas=1
    ) -> None:
        super().__init__(cor, potencia, tensao, preco)

        self.quantidade_de_portas = quantidade_de_portas


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preço <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preço
            self.eletrodomesticos.append(eletrodomestico)


liquidificador_vermelho = Liquidificador("Vermelho", 250, 220, 100)
pessoa_cozinheira = Pessoa("Jacquin", 1000)

pessoa_cozinheira.comprar_eletrodomestico(liquidificador_vermelho)
print(pessoa_cozinheira.eletrodomesticos[0].cor)

liquidificador_vermelho.ligar(1)
print("Está ligado?", liquidificador_vermelho.esta_ligado())

liquidificador_vermelho.desligar()
print("Está ligado?", liquidificador_vermelho.esta_ligado())
