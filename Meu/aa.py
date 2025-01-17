class Personagem:

    def __init__(self, nome, altura, peso, resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

personagem1 = Personagem(nome='Luca', altura=1.85, peso=75, resistencia=100)
print(personagem1)