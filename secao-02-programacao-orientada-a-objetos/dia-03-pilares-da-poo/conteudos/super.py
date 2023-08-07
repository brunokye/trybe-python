from typing import Any


class Pai:
    def faz_algo(self, valor: Any) -> None:
        print(valor)


class Filha(Pai):
    def faz_outra_coisa(self) -> None:
        print("Método da classe Pai")

        # Pai.faz_algo(self, valor=1)
        super().faz_algo(valor=1)


sub_objeto = Filha()
sub_objeto.faz_outra_coisa()
