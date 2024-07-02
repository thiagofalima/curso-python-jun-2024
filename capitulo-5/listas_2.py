nome_completo = []

while True:

    nome = input('Adiciona uma nome (ou enter para sair): ').title()

    nome_completo.append(nome)

    if not nome:
        nome_completo = ' '.join(nome_completo)
        break

print(nome_completo)