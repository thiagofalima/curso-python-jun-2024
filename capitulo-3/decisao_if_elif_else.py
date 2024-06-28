nome = input('Entre com seu nome: ').title()
idade = int(input('Entre com sua idade: '))
# print(f'Oi meu nome é {nome} e tenho {idade} anos de idade.')

# contexto 1

if idade >= 65:
    print(f'{nome} é bem experiente.')
elif 65 > idade >= 18:
    print(f'{nome} é um jovem adulto.')
else:
    print(nome + " é " + 3 * "jovem ainda ")



