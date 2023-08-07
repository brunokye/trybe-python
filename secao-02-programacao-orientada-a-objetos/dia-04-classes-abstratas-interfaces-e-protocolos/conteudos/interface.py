class Produto:
    def __init__(self, preco):
        self.preco = preco

    def imprimir_preco(self):
        raise NotImplementedError(
            "Classes derivadas de Produto precisam "
            "implementar o método imprimir_preco."
        )


class Livro(Produto):
    def __init__(self, preco):
        super().__init__(preco)

    def imprimir_preco(self):
        print(f"O preço do livro é: {self.preco}")


livro = Livro(10)
livro.imprimir_preco()
