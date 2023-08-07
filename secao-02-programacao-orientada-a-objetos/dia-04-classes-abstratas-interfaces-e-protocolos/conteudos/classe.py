from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def imprimir_cargo(self):
        pass


class Vendedor(Pessoa):
    def imprimir_cargo(self):
        print("Meu cargo é de vendedor.")


class Gerente(Pessoa):
    def imprimir_cargo(self):
        print("Meu cargo é de gerente.")


vendedor = Vendedor()
vendedor.imprimir_cargo()

gerente = Gerente()
gerente.imprimir_cargo()
