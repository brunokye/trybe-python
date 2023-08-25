from models.joke_model import JokeModel

jokes = [
    "Porque a galinha atravessou a rua? Para chegar do outro lado",
    "Qual o contrário de volátil? Vem cá sobrinho",
    "O que é um pontinho amarelo no céu? Um Yellowcóptero",
    "O que é um pontinho azul no canto da sala? Um smurfs fazendo exercício"
]

for joke in jokes:
    JokeModel({'joke': joke}).save()
