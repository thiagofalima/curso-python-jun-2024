class Carro:

    def __init__(self, marca: str, modelo: str, ano: int):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano


meu_carro = Carro('BMW', 'X6', 2023)

print(meu_carro.marca)
print(meu_carro.modelo)
print(meu_carro.ano)
