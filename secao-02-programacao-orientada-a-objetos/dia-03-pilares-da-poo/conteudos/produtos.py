class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def descrever(self):
        pass

    def preço(self):
        pass


class Livro(Produto):
    def __init__(self, nome: str, autor: str, preco: float) -> None:
        super().__init__(nome, preco)
        self.autor = autor

    def descrever(self):
        return f"{self.nome} por {self.autor}"

    def preço(self):
        return self.preco


class DVD(Produto):
    def __init__(self, nome: str, diretor: str, preco: float) -> None:
        super().__init__(nome, preco)
        self.diretor = diretor

    def descrever(self):
        return f"{self.nome} dirigido por {self.diretor}"

    def preço(self):
        return self.preco


def imprimir_detalhes(produto: Produto):
    print(f"Descrição: {produto.descrever()}")
    print(f"Preço: {produto.preco}")


produtos = [
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 29.99),
    DVD("O Poderoso Chefão", "Francis Ford Coppola", 19.99)
]

for produto in produtos:
    imprimir_detalhes(produto)
