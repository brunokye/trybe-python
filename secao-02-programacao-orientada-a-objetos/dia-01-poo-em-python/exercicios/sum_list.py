from typing import List


def soma_lista(valores: List[int]) -> int:
    soma = 0
    for valor in valores:
        soma += valor
    return soma


valores = [1, 2, 3, 4, 5]
print(soma_lista(valores))
