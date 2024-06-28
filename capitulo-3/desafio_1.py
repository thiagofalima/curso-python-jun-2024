# TODO: receber qs notas

n1 = int(input("Entre com a nota da P1: "))
n2 = int(input("Entre com a nota da P2: "))

# TODO: calcular a média

media = (n1 + n2) / 2
print(f'Sua média final é {media}.')

# TODO: Dar o status a partir da média

if media == 10:
    print("Aprovado com distinção!")
elif media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
