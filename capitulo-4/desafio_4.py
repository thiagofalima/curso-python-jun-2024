# TODO: Receber a quantidade de itens

quantidade = int(input("Quantos itens deseja em sua lista?\n"))
lista_mercado = []

for i in range(quantidade):

    #  TODO: Receber os itens

    item = input("Digite o item do mercado: ")

    # TODO: Adicionar à lista

    lista_mercado.append(item)

print(lista_mercado)
