class Pessoa:
    def diz_nome_e_idade(self, idade: int) -> None:
        print(f"{self.nome} tem {idade} anos.")


maria = Pessoa()
maria.nome = "Maria"
maria.diz_nome_e_idade(20)

jorge = Pessoa()
jorge.nome = "Jorge"
jorge.diz_nome_e_idade(28)


class Carro:
    def identificar(self, modelo: str, marca: str, ano: int, cor: str) -> None:
        print(
            f"Meu carro é um {modelo}, da {marca}. "
            f"Ele é do ano {ano} e tem a cor {cor}."
        )


carro = Carro()
carro.identificar("Uno", "Fiat", 2010, "vermelha")
