
class Caixa:

    def __init__(self, item, item1, item2, item3, item4):
        self.item = item
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4


minha_caixa = Caixa("Cebola", "Caneta", "Sapato", "Garrafa",
                    "Celular")

print(minha_caixa.item1)
